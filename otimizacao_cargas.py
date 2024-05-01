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
