import requests, threading, os
from dotenv import load_dotenv
import time

load_dotenv()  # Cargar variables desde .env si estás en local
URL_SERVIDOR = os.environ.get("URL_SERVIDOR","") 

def ping_otro_servidor():
    try:
        print("Esperando 60 segundos antes de llamar al otro servidor...")
        threading.Timer(60.0, lambda: requests.get(URL_SERVIDOR)).start()
    except Exception as e:
        print(f"Error al llamar al otro servidor: {e}")

def esperar_servidor_pareja():
    print(f"Esperando a que {URL_SERVIDOR} esté disponible...")

    while True:
        try:
            response = requests.get(URL_SERVIDOR, timeout=10)
            if response.status_code == 200:
                print(f"Servidor pareja respondió correctamente: {response.status_code}")
                break
            else:
                print(f"Respuesta recibida pero no OK: {response.status_code}")
        except Exception as e:
            print(f"No se pudo conectar con {URL_SERVIDOR}: {e}")

        print("Reintentando en 10 segundos...")
        time.sleep(10)
