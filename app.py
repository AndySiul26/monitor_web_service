# -*- coding: utf-8 -*-

import os
from flask import Flask
from dotenv import load_dotenv
from routes import main_bp
from mantener import esperar_servidor_pareja

# Ejecutar verificación antes de levantar el servidor Flask
esperar_servidor_pareja()

# Cargar variables del archivo .env en entorno local
load_dotenv()

app = Flask(__name__)
app.register_blueprint(main_bp)
# Ejecutar servidor local solo si DEBUG=true
if __name__ == "__main__" and os.getenv("DEBUG", "false").lower() == "true":
    app.run(port=5000, debug=True, use_reloader=False)
