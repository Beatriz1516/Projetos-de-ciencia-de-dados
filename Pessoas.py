import pandas as pd

dados = {
    "Nome": ["Ana, Maria", "João", "Pedro", "Lucas", None],
    "Cidade": ["Londrina", "Maringá", "Londrina", None, "Cascavel"],
    "Idade": [18, 19, 18, 20, 19],
    "Nota": [8.5, 7.0, 9.0, 6.5, 8.0]
}

#EXEMPLO
mauricio = {
    "nome": "Mauricio",
    "cabelo": "cacheado",
    "cor_do_cabelo": "castanho médio",
    "altura": "1.10m",
    "aura": 10000000,
    "idade": 17,
    "capital": "R$ 0,00"
}

#TRANSFORMANDO A LISTA EM UM DATAFRAME DO PANDAS
df = pd.DataFrame(dados)
print("=== DATAFRAME ===")
print(df)


#ESTATÍSTICAS DAS NOTAS
print("\n\n=== ESTATÍSTICAS ===")
print("A média das notas", df['Nota'].mean())
print("A nota máxima", df['Nota'].max())
print("A nota mínima", df['Nota'].min())
print("A soma de todas as notas", df['Nota'].sum())


print("\n\n=== DESCRIBE ===")
print(df.describe())

#FILTRAGEM
print("\n\n=== NOTAS SUPERIORES QUE 8 ===")
print(df[df['Nota'] > 8])

print("\n\n=== FREQUÊNCIA DAS CIDADES ===")
print(df['Cidade'].value_counts())

print("\n\n=== DADOS FALTANTES ===")
print(df.isnull())
print(df.isnull().sum())


print("\n\n=== NOMES DAS PESSOAS ===")
pessoas = df['Nome']
print(f"{pessoas}")


print("\n\n=== IDADES ===")
idades = df['Idade']
print(f"{idades}")