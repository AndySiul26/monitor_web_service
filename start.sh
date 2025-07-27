#!/bin/bash

# Instala dependencias
pip install -r requirements.txt

echo "Iniciando servidor WSGI con Gunicorn..."
gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 app:app
