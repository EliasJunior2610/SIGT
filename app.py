from flask import Flask, render_template # type: ignore

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/previsao_demanda')
def previsao_demanda():
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

    return render_template('previsao_demanda.html')

@app.route('/roteirizacao')
def roteirizacao():
    from ortools.constraint_solver import routing_enums_pb2 # type: ignore
    from ortools.constraint_solver import pywrapcp # type: ignore

    # Dados fictícios de distâncias entre locais
    distances = [
        [0, 10, 20, 30],
        [10, 0, 25, 35],
        [20, 25, 0, 15],
        [30, 35, 15, 0]
    ]

    def create_data_model():
        data = {}
        data['distance_matrix'] = distances
        data['num_vehicles'] = 1
        data['depot'] = 0
        return data

    def main():
        data = create_data_model()

        manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                            data['num_vehicles'], data['depot'])
        routing = pywrapcp.RoutingModel(manager)

        def distance_callback(from_index, to_index):
            from_node = manager.IndexToNode(from_index)
            to_node = manager.IndexToNode(to_index)
            return data['distance_matrix'][from_node][to_node]

        transit_callback_index = routing.RegisterTransitCallback(distance_callback)
        routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

        search_parameters = pywrapcp.DefaultRoutingSearchParameters()
        search_parameters.first_solution_strategy = (
            routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

        solution = routing.SolveWithParameters(search_parameters)

        if solution:
            print_solution(manager, routing, solution)

    def print_solution(manager, routing, solution):
        print('Distância total: {} km'.format(solution.ObjectiveValue()))
        index = routing.Start(0)
        plan_output = 'Rota:'
        route_distance = 0
        while not routing.IsEnd(index):
            plan_output += ' {} ->'.format(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
        plan_output += ' {}\n'.format(manager.IndexToNode(index))
        print(plan_output)

    if __name__ == '__main__':
        main()

    return render_template('roteirizacao.html')

@app.route('/manutencao_preditiva')
def manutencao_preditiva():
    from sklearn.ensemble import IsolationForest # type: ignore

    # Dados fictícios de sensores
    sensor_data = [[0.5], [0.6], [0.7], [0.8], [0.9], [2.0]]  # Exemplo com uma anomalia em 2.0

    # Treinar o modelo de detecção de anomalias
    model = IsolationForest(contamination=0.1)  # 10% de dados anômalos
    model.fit(sensor_data)

    # Detectar anomalias
    anomaly_preds = model.predict(sensor_data)
    print("Anomalias detectadas:", anomaly_preds)

    return render_template('manutencao_preditiva.html')

@app.route('/gestao_frota')
def gestao_frota():
    import random
    import time

    def generate_gps_data():
        while True:
            latitude = random.uniform(-90, 90)
            longitude = random.uniform(-180, 180)
            yield (latitude, longitude)
            time.sleep(1)

    def main():
        gps_generator = generate_gps_data()
        for i in range(10):  # Simula 10 atualizações de localização
            latitude, longitude = next(gps_generator)
            print(f"Veículo {i+1}: Latitude {latitude}, Longitude {longitude}")
            # Aqui você pode enviar os dados de localização para o sistema de gestão de frota em tempo real

    if __name__ == "__main__":
        main()

    return render_template('gestao_frota.html')


@app.route('/otimizacao_cargas')
def otimizacao_cargas():
    def allocate_cargo(vehicle_capacity, cargo_list):
        allocated_cargo = []
        remaining_capacity = vehicle_capacity
        for cargo in cargo_list:
            if cargo <= remaining_capacity:
                allocated_cargo.append(cargo)
                remaining_capacity -= cargo
        return allocated_cargo

    def main():
        vehicle_capacity = 1000  # Capacidade máxima do veículo em kg
        cargo_list = [300, 400, 200, 600, 500]  # Lista de cargas disponíveis em kg
        allocated_cargo = allocate_cargo(vehicle_capacity, cargo_list)
        print("Cargas alocadas aos veículos:", allocated_cargo)

    if __name__ == "__main__":
        main()
    return render_template('otimizacao_cargas.html')

@app.route('/analise_dados')
def analise_dados():
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

    return render_template('analise_dados.html')

if __name__ == '__main__':
    app.run(debug=True)
