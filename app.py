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

from flask import render_template_string

@app.route("/", methods=["GET"])
def inicio():
    """
    Página principal con formato HTML para documentación de la API.
    """
    html = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>API de Vacunación - Panamá</title>
        <style>
            body { font-family: 'Segoe UI', sans-serif; background-color: #f4f6f8; color: #333; margin: 40px; }
            h1 { color: #0078D4; }
            h2 { color: #444; margin-top: 30px; }
            code { background-color: #eee; padding: 3px 6px; border-radius: 4px; }
            .box { background: white; padding: 25px; border-radius: 12px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
            .endpoint { background-color: #fafafa; border-left: 4px solid #0078D4; padding: 10px; margin-top: 10px; }
            .footer { margin-top: 40px; font-size: 14px; color: #777; }
            a { color: #0078D4; text-decoration: none; }
            a:hover { text-decoration: underline; }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>API de Vacunación contra el Sarampión en Panamá</h1>
            <p>Esta API proporciona datos históricos sobre la vacunación en niños de 12 a 23 meses, 
            basados en el indicador <strong>SH.IMM.MEAS</strong> del Banco Mundial.</p>

            <h2>Endpoints disponibles</h2>
            <div class="endpoint"><strong>GET</strong> <code>/vacunas</code> — Lista todos los registros nacionales</div>
            <div class="endpoint"><strong>GET</strong> <code>/vacunas/&lt;año&gt;</code> — Datos del año especificado</div>
            <div class="endpoint"><strong>GET</strong> <code>/vacunas/provincia/&lt;nombre&gt;</code> — Datos simulados por provincia</div>

            <h2>Ejemplos rápidos</h2>
            <ul>
                <li><a href="/vacunas" target="_blank">http://127.0.0.1:5000/vacunas</a></li>
                <li><a href="/vacunas/2005" target="_blank">http://127.0.0.1:5000/vacunas/2005</a></li>
                <li><a href="/vacunas/provincia/Chiriquí" target="_blank">http://127.0.0.1:5000/vacunas/provincia/Chiriquí</a></li>
            </ul>

            <div class="footer">
                <p><strong>Autor:</strong> Kayder Murillo — Universidad Interamericana de Panamá</p>
                <p>Proyecto de Programación 4 — Módulo 12 — Parcial 2</p>
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html)

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
