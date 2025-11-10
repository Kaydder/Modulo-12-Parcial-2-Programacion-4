"""
Servicios de consulta y transformación de datos de vacunación
contra el sarampión en Panamá.
"""

from typing import List, Dict, Optional
from data_vacunas import obtener_todos, obtener_por_anio


PROVINCIAS_PANAMA = [
    "Bocas del Toro",
    "Coclé",
    "Colón",
    "Chiriquí",
    "Darién",
    "Herrera",
    "Los Santos",
    "Panamá",
    "Panamá Oeste",
    "Veraguas",
]


def listar_vacunas() -> List[Dict]:
    """
    Devuelve la lista completa de registros nacionales.
    """
    return obtener_todos()


def vacuna_por_anio(anio: int) -> Optional[Dict]:
    """
    Devuelve el registro nacional de un año concreto.
    """
    return obtener_por_anio(anio)


def vacunas_por_provincia(nombre_provincia: str) -> List[Dict]:
    """
    Simula los datos de vacunación por provincia para todos los años disponibles.

    Como los datos del Banco Mundial son nacionales, aquí se genera
    una distribución ficticia a partir de la cobertura nacional:
    - Se aplica un pequeño ajuste porcentual por provincia.

    Retorna una lista de registros (uno por año) para la provincia solicitada.
    Si la provincia no existe, retorna una lista vacía.
    """
    nombre_normalizado = nombre_provincia.strip().lower()

    provincias_normalizadas = {p.lower(): p for p in PROVINCIAS_PANAMA}
    if nombre_normalizado not in provincias_normalizadas:
        return []

    provincia_oficial = provincias_normalizadas[nombre_normalizado]

    registros_nacionales = obtener_todos()
    resultado = []

    factor_base = (len(provincia_oficial) % 3) - 1  # -1, 0 o 1

    for reg in registros_nacionales:
        cobertura_provincial = reg["cobertura"] + factor_base * 1.5
        cobertura_provincial = max(0.0, min(100.0, cobertura_provincial))

        resultado.append(
            {
                "anio": reg["anio"],
                "pais": reg["pais"],
                "codigo_pais": reg["codigo_pais"],
                "indicador": reg["indicador"],
                "provincia": provincia_oficial,
                "cobertura": round(cobertura_provincial, 1),
            }
        )

    return resultado
