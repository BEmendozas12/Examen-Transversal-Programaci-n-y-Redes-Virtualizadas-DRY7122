# geolocalizacion.py
import requests

def calcular_ruta(ciudad_origen, ciudad_destino, vehiculo):
    url = "https://graphhopper.com/api/1/route"
    params = {
        "point": [ciudad_origen, ciudad_destino],
        "vehicle": vehiculo, transporte publico, a pie, avion, motocicleta
        "locale": "es",
        "instructions": "true",
        "key": "TU_API_KEY"
    }
    r = requests.get(url, params=params)
    data = r.json()
    distancia_km = data['paths'][0]['distance'] / 1000
    duracion = data['paths'][0]['time'] / 60000
    narrativa = data['paths'][0]['instructions']
    print(f"Distancia: {distancia_km:.2f} km / {distancia_km*0.621:.2f} mi")
    print(f"Duración estimada: {duracion:.2f} minutos")
    for paso in narrativa:
        print(paso['text'])

# Loop de interacción
while True:
    origen = input("Ciudad de origen: ")
    if origen.lower() == "s":
        break
    destino = input("Ciudad de destino: ")
    vehiculo = input("Medio de transporte (car, bike, foot): ")
    calcular_ruta(origen, destino, vehiculo)
