"""
API RESTful de solo lectura para consultar datos históricos
de vacunación contra el sarampión en niños de 12 a 23 meses en Panamá.

Framework: Flask
Métodos permitidos: solo GET
"""

from flask import Flask, jsonify, abort, Response
from vacunas_service import (
    listar_vacunas,
    vacuna_por_anio,
    vacunas_por_provincia,
)
import json

app = Flask(__name__)

@app.route("/vacunas", methods=["GET"])
def get_vacunas():
    """
    GET /vacunas
    Devuelve todos los registros disponibles a nivel nacional.
    """
    datos = listar_vacunas()
    return jsonify(datos), 200


@app.route("/vacunas/<int:anio>", methods=["GET"])
def get_vacuna_por_anio(anio):
    """
    GET /vacunas/<anio>
    Devuelve el registro correspondiente al año especificado.
    Si no existe registro para ese año, devuelve 404.
    """
    registro = vacuna_por_anio(anio)
    if registro is None:
        abort(404, description=f"No hay datos de vacunación para el año {anio}.")
    return jsonify(registro), 200


@app.route("/vacunas/provincia/<string:nombre>", methods=["GET"])
def get_vacunas_por_provincia(nombre):
    """
    GET /vacunas/provincia/<nombre>
    Devuelve los datos de vacunación simulados para la provincia especificada.
    Si la provincia no existe en la lista soportada, devuelve 404.
    """
    registros = vacunas_por_provincia(nombre)
    if not registros:
        abort(404, description=f"No se encontraron datos para la provincia '{nombre}'.")
    return jsonify(registros), 200

@app.route("/", methods=["GET"])
def inicio():
    """
    Ruta principal (raíz) de la API.
    Muestra un mensaje de bienvenida y los endpoints disponibles, con formato legible.
    """
    contenido = {
        "titulo": "API de Vacunación contra el Sarampión en Panamá",
        "descripcion": (
            "Esta API proporciona datos históricos de vacunación en niños de 12 a 23 meses, "
            "basada en el indicador SH.IMM.MEAS del Banco Mundial."
        ),
        "autor": "Kayder Murillo - Universidad Interamericana de Panamá",
        "endpoints_disponibles": {
            "Listado completo": "/vacunas",
            "Por año": "/vacunas/<año>",
            "Por provincia": "/vacunas/provincia/<nombre>"
        },
        "ejemplos": {
            "1": "http://127.0.0.1:5000/vacunas",
            "2": "http://127.0.0.1:5000/vacunas/2005",
            "3": "http://127.0.0.1:5000/vacunas/provincia/Chiriquí"
        },
        "mensaje": "Bienvenido a la API. Utilice los endpoints anteriores para acceder a los datos."
    }

    return Response(
        json.dumps(contenido, ensure_ascii=False, indent=4),
        mimetype='application/json'
    )

@app.errorhandler(404)
def recurso_no_encontrado(error):
    """
    Manejo de errores 404 con respuesta JSON.
    """
    respuesta = jsonify(
        {
            "error": "Recurso no encontrado",
            "detalle": error.description if hasattr(error, "description") else "",
        }
    )
    return respuesta, 404


@app.errorhandler(500)
def error_interno(error):
    """
    Manejo genérico de errores 500.
    """
    respuesta = jsonify(
        {
            "error": "Error interno del servidor",
        }
    )
    return respuesta, 500

if __name__ == "__main__":
    app.run(debug=True)
