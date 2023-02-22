# exercicio-pandas  
##  Tratando arquivo csv com a biblioteca Pandas e executando o script no Power BI  
###  1.  Importando a biblioteca Pandas:    
---
import pandas as pd

###  2.  Importando arquivo csv:
---
import csv
---
###  3.  Leitura do arquivo csv, codificando e skipando linhas com erro:
---
df = pd.read_csv('C:/Users/Win10/Desktop/nova tentativa/Exercicio-Pandas-powerBi/arquivo1.csv', encoding='utf-8',sep = ';', on_bad_lines='skip')
###  4.   Removendo colunas:
---
df.drop(columns=['Mean Software Developer Salary (unadjusted)' , 'Mean Unadjusted Salary (all occupations)' , 'Median Home Price'], inplace=True)
### 5.  Renomeando colunas:
---
df.rename(columns={'Index': 'índice'}, inplace=True)  
df.rename(columns={'Metro': 'Cidade-Capital'}, inplace=True)  
df.rename(columns={'Mean Software Developer Salary (adjusted)': 'Salário do Desenvolvedor (ajustado)'}, inplace=True)  
df.rename(columns={'Number of Software Developer Jobs': 'Número de empregos de desenvolvedor de software'}, inplace=True)  
df.rename(columns={'City': 'Cidade'}, inplace=True)  
df.rename(columns={'Cost of Living avg': 'Custo de vida médio'}, inplace=True)  
df.rename(columns={'Rent avg' : 'Aluguel médio'}, inplace=True)  
df.rename(columns={'Cost of Living Plus Rent avg' : 'Custo de vida mais aluguel médio'}, inplace=True)  
### 6. imprimindo:
---
print(df)

###  Imagem do script python inserido no Power BI:
---
![script01](https://user-images.githubusercontent.com/125930758/220777303-e1a08293-abd7-435e-8802-2aa84d138198.png)
---
![script02](https://user-images.githubusercontent.com/125930758/220777414-a5adead7-9072-4db5-85b0-000df56fa955.png)
---
### Imagem da tabela no Power Query:
---
![tabelapowequery01](https://user-images.githubusercontent.com/125930758/220778759-3835229a-b4e5-4de6-a872-49ad76a6eb3d.png)

![tabelapowequery02](https://user-images.githubusercontent.com/125930758/220778858-49259c89-5235-4801-9143-e325122fa1cb.png)

---
### Imagem  da tabela final no Power BI:
---
![tabela final](https://user-images.githubusercontent.com/125930758/220777831-f50b82bb-c92d-4935-88a5-8e9cab215068.png)
### Gráfico pizza e de barra com resultado alcançado no Power Bi:
___
![grafico01](https://user-images.githubusercontent.com/125930758/220778312-d9823d91-7e55-4548-85af-f8f8364efaea.png)
![grafico02](https://user-images.githubusercontent.com/125930758/220778343-10ca9523-c73e-4128-b15e-307e2dc2a165.png)
