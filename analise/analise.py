```python
import pandas

df = pandas.read_csv("student_exam_performance.csv", usecols=['exam_score','sleep_hours','study_hours_per_day','attendance_percentage','pass_status'])

# valores nulos
quantitative_lines_NULL = df.isnull().any(axis=1).sum()
print("quantidade de linhas com alguma coluna vazia:", quantitative_lines_NULL)
df = df.dropna()
print("quantidade de linhas vazias após a remoção", df.isnull().any(axis=1).sum())

# duplicatas
linhas_duplicadas = df.duplicated().sum()
print("quantidade de linhas duplicadas", linhas_duplicadas)
df = df.drop_duplicates()
print("quantidade de linhas após a remoção de duplicadas", df.duplicated().sum())

# conversão de tipo: string -> category (reduz memória, indica variável categórica)
df['pass_status'] = df['pass_status'].astype('category')

print(df.dtypes)

# exam_score
media_exam_score = df['exam_score'].mean()
moda_exam_score = df['exam_score'].mode().tolist()  # lista cobre caso de empate
mediana_exam_score = df['exam_score'].median()
print("média exam_score:", media_exam_score)
print("moda exam_score:", moda_exam_score)
print("mediana exam_score:", mediana_exam_score)

# sleep_hours
media_sleep_hours = df['sleep_hours'].mean()
moda_sleep_hours = df['sleep_hours'].mode().tolist()
mediana_sleep_hours = df['sleep_hours'].median()
print("média sleep_hours:", media_sleep_hours)
print("moda sleep_hours:", moda_sleep_hours)
print("mediana sleep_hours:", mediana_sleep_hours)

# study_hours_per_day
media_study_hours_per_day = df['study_hours_per_day'].mean()
moda_study_hours_per_day = df['study_hours_per_day'].mode().tolist()
mediana_study_hours_per_day = df['study_hours_per_day'].median()
print("média study_hours_per_day:", media_study_hours_per_day)
print("moda study_hours_per_day:", moda_study_hours_per_day)
print("mediana study_hours_per_day:", mediana_study_hours_per_day)

# attendance_percentage
media_attendance_percentage = df['attendance_percentage'].mean()
moda_attendance_percentage = df['attendance_percentage'].mode().tolist()
mediana_attendance_percentage = df['attendance_percentage'].median()
print("média attendance_percentage:", media_attendance_percentage)
print("moda attendance_percentage:", moda_attendance_percentage)
print("mediana attendance_percentage:", mediana_attendance_percentage)

# pass_status é categórica -> só moda se aplica
moda_pass_status = df['pass_status'].mode().tolist()
print("moda pass_status:", moda_pass_status)

# exam_score: posição e dispersão
q1_exam_score = df['exam_score'].quantile(0.25)
q3_exam_score = df['exam_score'].quantile(0.75)
amplitude_exam_score = df['exam_score'].max() - df['exam_score'].min()
variancia_exam_score = df['exam_score'].var()
desvio_padrao_exam_score = df['exam_score'].std()
print("Q1 exam_score:", q1_exam_score)
print("Q3 exam_score:", q3_exam_score)
print("amplitude exam_score:", amplitude_exam_score)
print("variância exam_score:", variancia_exam_score)
print("desvio padrão exam_score:", desvio_padrao_exam_score)

# sleep_hours: posição e dispersão
q1_sleep_hours = df['sleep_hours'].quantile(0.25)
q3_sleep_hours = df['sleep_hours'].quantile(0.75)
amplitude_sleep_hours = df['sleep_hours'].max() - df['sleep_hours'].min()
variancia_sleep_hours = df['sleep_hours'].var()
desvio_padrao_sleep_hours = df['sleep_hours'].std()
print("Q1 sleep_hours:", q1_sleep_hours)
print("Q3 sleep_hours:", q3_sleep_hours)
print("amplitude sleep_hours:", amplitude_sleep_hours)
print("variância sleep_hours:", variancia_sleep_hours)
print("desvio padrão sleep_hours:", desvio_padrao_sleep_hours)

# study_hours_per_day: posição e dispersão
q1_study_hours_per_day = df['study_hours_per_day'].quantile(0.25)
q3_study_hours_per_day = df['study_hours_per_day'].quantile(0.75)
amplitude_study_hours_per_day = df['study_hours_per_day'].max() - df['study_hours_per_day'].min()
variancia_study_hours_per_day = df['study_hours_per_day'].var()
desvio_padrao_study_hours_per_day = df['study_hours_per_day'].std()
print("Q1 study_hours_per_day:", q1_study_hours_per_day)
print("Q3 study_hours_per_day:", q3_study_hours_per_day)
print("amplitude study_hours_per_day:", amplitude_study_hours_per_day)
print("variância study_hours_per_day:", variancia_study_hours_per_day)
print("desvio padrão study_hours_per_day:", desvio_padrao_study_hours_per_day)

# attendance_percentage: posição e dispersão
q1_attendance_percentage = df['attendance_percentage'].quantile(0.25)
q3_attendance_percentage = df['attendance_percentage'].quantile(0.75)
amplitude_attendance_percentage = df['attendance_percentage'].max() - df['attendance_percentage'].min()
variancia_attendance_percentage = df['attendance_percentage'].var()
desvio_padrao_attendance_percentage = df['attendance_percentage'].std()
print("Q1 attendance_percentage:", q1_attendance_percentage)
print("Q3 attendance_percentage:", q3_attendance_percentage)
print("amplitude attendance_percentage:", amplitude_attendance_percentage)
print("variância attendance_percentage:", variancia_attendance_percentage)
print("desvio padrão attendance_percentage:", desvio_padrao_attendance_percentage)
