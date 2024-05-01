import numpy as np # type: ignore
from sklearn.model_selection import train_test_split # type: ignore
from sklearn.linear_model import LinearRegression # type: ignore

# Dados fictícios de demanda de transporte (X) e datas/horários correspondentes (y)
X = np.array([[1, 2, 3, 4, 5]]).T
y = np.array([10, 20, 30, 40, 50])

# Dividir os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar o modelo de regressão linear
model = LinearRegression()
model.fit(X_train, y_train)

# Prever a demanda para uma nova data/horário
new_data = np.array([[6]])
predicted_demand = model.predict(new_data)
print("Previsão de demanda:", predicted_demand)
