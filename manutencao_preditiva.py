from sklearn.ensemble import IsolationForest # type: ignore

# Dados fictícios de sensores
sensor_data = [[0.5], [0.6], [0.7], [0.8], [0.9], [2.0]]  # Exemplo com uma anomalia em 2.0

# Treinar o modelo de detecção de anomalias
model = IsolationForest(contamination=0.1)  # 10% de dados anômalos
model.fit(sensor_data)

# Detectar anomalias
anomaly_preds = model.predict(sensor_data)
print("Anomalias detectadas:", anomaly_preds)
