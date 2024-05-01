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
