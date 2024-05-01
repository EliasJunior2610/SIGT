import pandas as pd # type: ignore

# Dados fictícios de entregas
data = {
    'Data': ['2024-04-01', '2024-04-02', '2024-04-03'],
    'Total_Entregas': [50, 60, 70],
    'Tempo_Médio_Entrega': ['2 horas', '2.5 horas', '3 horas']
}

# Criar DataFrame
df = pd.DataFrame(data)

# Gerar relatório
print("Relatório de Entregas:")
print(df)
