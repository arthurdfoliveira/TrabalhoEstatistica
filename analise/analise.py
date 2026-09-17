import pandas

df = pandas.read_csv("student_exam_performance.csv",usecols=['exam_score','sleep_hours','study_hours_per_day','attendance_percentage','pass_status'])
# parte do codigo responsável por verificar e remover linhas com valores nulos do arquivo csv
quantitative_lines_NULL= df.isnull().any(axis=1).sum()
print("quantidade de linhas com alguma coluna vazia:",quantitative_lines_NULL)
df=df.dropna()
print("quantidade de linhas vazias após a remoção",df.isnull().any(axis=1).sum())

#parte do codigo responsável por verificar e remover linhas duplicadas do arquivo csv
linhas_duplicadas = df.duplicated().sum()
print("quantidade de linhas duplicadas",linhas_duplicadas)
df=df.drop_duplicates()
print("quantidade de linhas após a remoção de duplicadas",df.duplicated().sum())
#modificação do tipo de dado da coluna "pass_status" de string para category, a fim de dinuir o seu tamanho de memoria  
df['pass_status'] = df['pass_status'].astype('category')

print(df.dtypes)