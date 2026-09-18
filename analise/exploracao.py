"""Correlação, padronização e figuras da exploração descritiva."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


VARIAVEIS = ["exam_score", "sleep_hours", "study_hours_per_day", "attendance_percentage"]
FATORES = VARIAVEIS[1:]
ROTULOS = {
    "exam_score": "Nota da prova",
    "sleep_hours": "Sono (horas)",
    "study_hours_per_day": "Estudo (horas/dia)",
    "attendance_percentage": "Frequência (%)",
}


def analisar(df):
    """Usa todas as linhas tratadas, sem alterar o DataFrame recebido."""
    dados = df[VARIAVEIS].copy()
    if len(dados) < 3 or dados.isna().any().any():
        raise ValueError("A análise requer ao menos três registros completos.")
    if not np.isfinite(dados.to_numpy(dtype=float)).all():
        raise ValueError("As variáveis numéricas precisam conter valores finitos.")
    desvios = dados.std(ddof=1)
    if (desvios == 0).any():
        raise ValueError("Não é possível padronizar ou correlacionar coluna constante.")

    # Pearson mede associação linear; Spearman usa postos e mede associação
    # monotônica. Ambos usam a base completa, sem amostragem para o cálculo.
    pearson = dados.corr(method="pearson")
    spearman = dados.corr(method="spearman")
    associacoes = pd.DataFrame({
        "Pearson": pearson.loc[FATORES, "exam_score"],
        "Spearman": spearman.loc[FATORES, "exam_score"],
        "n": len(dados),
    })

    # Z-score amostral: z = (x - média) / desvio padrão, com ddof=1.
    # A nota permanece como desfecho; padronizamos os três fatores para
    # comparar suas distribuições em unidades de desvio padrão.
    padronizados = (dados[FATORES] - dados[FATORES].mean()) / desvios[FATORES]
    verificacao = pd.DataFrame({
        "media_z": padronizados.mean(),
        "desvio_padrao_z": padronizados.std(ddof=1),
    })
    return {"pearson": pearson, "spearman": spearman,
            "associacoes": associacoes, "padronizados": padronizados,
            "verificacao": verificacao}


def interpretar(resultados):
    tabela = resultados["associacoes"]
    linhas = [f"Análise de {int(tabela['n'].iloc[0]):,} registros completos."]
    for coluna, valores in tabela.iterrows():
        linhas.append(
            f"{ROTULOS[coluna]} e nota: Pearson = {valores['Pearson']:.3f}; "
            f"Spearman = {valores['Spearman']:.3f}."
        )
    maior = tabela["Pearson"].abs().idxmax()
    linhas.extend([
        f"Entre os fatores selecionados, {ROTULOS[maior].lower()} apresenta "
        "a maior associação linear em módulo com a nota nesta base.",
        "Os coeficientes são associações bivariadas: não controlam outros fatores "
        "e não demonstram causalidade nem importância independente. Valores próximos "
        "de zero não descartam relações não lineares.",
        "O Z-score permite comparar mediana, assimetria e extremos das distribuições "
        "de sono, estudo e frequência, apesar das unidades diferentes. Média zero "
        "e desvio padrão um são resultados da transformação, não descobertas sobre "
        "igualdade dos hábitos. Padronização não torna os dados normalmente distribuídos.",
        "Pearson e Spearman não exigem Z-score e não mudam com essa transformação "
        "linear de escala positiva. O boxplot padronizado não mede efeito sobre a nota.",
        "A exclusão de registros incompletos pode introduzir viés. As conclusões "
        "descrevem apenas a base utilizada; não estabelecem uma intervenção eficaz.",
    ])
    return "\n\n".join(linhas)


def gerar_graficos(df, resultados, pasta):
    """Salva figuras e as retorna para apresentação inline no notebook."""
    pasta = Path(pasta)
    pasta.mkdir(parents=True, exist_ok=True)
    sns.set_theme(style="whitegrid", context="notebook")
    figuras = {}

    fig, axes = plt.subplots(1, 2, figsize=(13, 5), constrained_layout=True)
    for ax, metodo in zip(axes, ["pearson", "spearman"]):
        matriz = resultados[metodo].rename(index=ROTULOS, columns=ROTULOS)
        sns.heatmap(matriz, annot=True, fmt=".3f", cmap="RdBu_r",
                    vmin=-1, vmax=1, center=0, square=True, ax=ax)
        ax.set_title(metodo.capitalize())
        ax.tick_params(axis="x", rotation=35)
        ax.tick_params(axis="y", rotation=0)
    fig.suptitle(f"Associações entre variáveis | n = {len(df):,}")
    figuras["01_correlacoes"] = fig

    # Densidade hexagonal usa todos os registros e evita sobreposição de pontos.
    fig, axes = plt.subplots(1, 3, figsize=(15, 4.5), constrained_layout=True)
    for ax, coluna in zip(axes, FATORES):
        pontos = ax.hexbin(df[coluna], df["exam_score"], gridsize=35,
                           mincnt=1, bins="log", cmap="viridis")
        ax.set(xlabel=ROTULOS[coluna], ylabel="Nota da prova",
               title=f"Pearson = {resultados['pearson'].loc[coluna, 'exam_score']:.3f}")
        fig.colorbar(pontos, ax=ax, label="Registros (escala log)")
    fig.suptitle("Fatores e nota | densidade de todos os registros")
    figuras["02_fatores_e_nota"] = fig

    fig, axes = plt.subplots(2, 2, figsize=(11, 7), constrained_layout=True)
    for ax, coluna in zip(axes.flat, VARIAVEIS):
        ax.hist(df[coluna], bins=35, color="#307e9a", edgecolor="white")
        ax.axvline(df[coluna].mean(), color="#9c2e2e", label="Média")
        ax.axvline(df[coluna].median(), color="#252525", linestyle="--", label="Mediana")
        ax.set(xlabel=ROTULOS[coluna], ylabel="Número de registros")
        ax.legend()
    fig.suptitle("Distribuições na base tratada")
    figuras["03_distribuicoes"] = fig

    fig, ax = plt.subplots(figsize=(9, 5), constrained_layout=True)
    sns.boxplot(data=resultados["padronizados"].rename(columns=ROTULOS),
                color="#82b9cf", ax=ax, fliersize=2)
    ax.axhline(0, color="#555555", linestyle="--", linewidth=1)
    ax.set(title="Comparação das distribuições após padronização",
           ylabel="Z-score (desvios padrão em relação à média)", xlabel="")
    figuras["04_padronizacao"] = fig

    for nome, figura in figuras.items():
        figura.savefig(pasta / f"{nome}.png", dpi=160, bbox_inches="tight")
    return figuras


def exportar_tabelas(resultados, pasta):
    pasta = Path(pasta)
    pasta.mkdir(parents=True, exist_ok=True)
    for nome in ["pearson", "spearman", "associacoes", "verificacao"]:
        resultados[nome].to_csv(pasta / f"{nome}.csv", encoding="utf-8-sig")
    (pasta / "interpretacao.txt").write_text(interpretar(resultados), encoding="utf-8")
