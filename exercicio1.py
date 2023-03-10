# importando a biblioteca Pandas:
import pandas as pd
# importando arquivo csv:
import csv

#leitura do arquivo de dados, e skipando linhas com erro:
df = pd.read_csv('C:/Users/Win10/Desktop/nova tentativa/Exercicio-Pandas-powerBi/arquivo1.csv', encoding='utf-8',sep = ';', on_bad_lines='skip')

# removendo colunas
df.drop(columns=['Mean Software Developer Salary (unadjusted)' , 'Mean Unadjusted Salary (all occupations)' , 'Median Home Price'], inplace=True)


# renomeando colunas:
df.rename(columns={'Index': 'índice'}, inplace=True)
df.rename(columns={'Metro': 'Cidade-Capital'}, inplace=True)
df.rename(columns={'Mean Software Developer Salary (adjusted)': 'Salário do Desenvolvedor (ajustado)'}, inplace=True)
df.rename(columns={'Number of Software Developer Jobs': 'Número de empregos de desenvolvedor de software'}, inplace=True)
df.rename(columns={'City': 'Cidade'}, inplace=True)
df.rename(columns={'Cost of Living avg': 'Custo de vida médio'}, inplace=True)
df.rename(columns={'Rent avg' : 'Aluguel médio'}, inplace=True)
df.rename(columns={'Cost of Living Plus Rent avg' : 'Custo de vida mais aluguel médio'}, inplace=True)

print(df)




