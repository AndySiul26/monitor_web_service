# -*- coding: utf-8 -*-

from flask import Blueprint
from mantener import ping_otro_servidor

main_bp = Blueprint("main", __name__)

@main_bp.route("/monitor", methods=["GET"])
def monitor_activo():
    print("Se recibió ping del servidor a mantener activo")
    ping_otro_servidor()
    return "ok", 200

@main_bp.route("/", methods=["GET"])
def principal():
    return "Monitor Activo"
