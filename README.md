# Trabalho de Estatistica - Análise Exploratória de Dados

## Grupo 6:
* Arthur da Fonte
* Bruno Holanda
* Matheus Freire
* Matheus Fialho
* Pablo Coelho
* Raul Maia
* Rodrigo Vinhas
* Vitor Gadelha

## Executar a exploração

Instale as dependências com `python -m pip install -r requirements.txt`.
Baixe o [dataset no Kaggle](https://www.kaggle.com/datasets/mobeenfatimah/student-exam-performance-and-success-dataset)
e coloque `student_exam_performance.csv` na raiz deste repositório. O CSV não é versionado.

```bash
python analise/analise.py
# Ou indique a localização do arquivo:
python analise/analise.py --csv "caminho/student_exam_performance.csv"
```

O script salva quatro figuras PNG, matrizes de Pearson e Spearman, uma tabela de
associações com a nota, a verificação do Z-score e uma interpretação em `resultados/`.
Use `--saida` para escolher outra pasta.

Para o relatório com texto e gráficos, abra `EDA_Desempenho_Academico.ipynb`
na raiz do repositório e execute as células em ordem. Mantenha a pasta `analise/`
junto ao notebook: ambos usam `analise/exploracao.py`, evitando diferenças entre
os cálculos. No Colab, disponibilize o repositório completo e o CSV, e use sua raiz
como diretório de trabalho.

### Critérios da análise

- As cinco variáveis selecionadas seguem o tratamento do script do grupo:
  exclusão de registros incompletos e de duplicatas nesses campos. A ausência
  de frequência exclui 9.863 registros do arquivo original; isso pode introduzir viés.
- Pearson descreve associações lineares; Spearman descreve associações monotônicas.
  Os cálculos e os gráficos de densidade usam todos os registros tratados.
- Sono, estudo e frequência são padronizados por Z-score com desvio padrão
  amostral (`ddof=1`) para comparar suas distribuições no boxplot. As variáveis
  originais são preservadas. Essa etapa não é necessária para calcular correlação.
- A aprovação deriva do corte da nota em 50 neste arquivo e não é tratada como
  fator explicativo independente na matriz de correlação.
- Associações bivariadas não demonstram causalidade ou influência independente.
  As conclusões específicas das hipóteses continuam sob revisão dos responsáveis.
