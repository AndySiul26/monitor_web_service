#!/bin/bash

# Instala dependencias
pip install -r requirements.txt

echo "Iniciando servidor WSGI con Gunicorn..."
exec gunicorn -w 1 -b 0.0.0.0:3000 app:app
