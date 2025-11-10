"""
Módulo de datos para la cobertura de vacunación contra el sarampión
en niños de 12 a 23 meses en Panamá.

Los datos se basan en el indicador SH.IMM.MEAS (Banco Mundial) y
se representan de forma simplificada para uso didáctico.
"""

VACUNAS_PANAMA = [
    {"anio": 2000, "pais": "Panamá", "codigo_pais": "PAN", "indicador": "SH.IMM.MEAS", "cobertura": 84.0},
    {"anio": 2001, "pais": "Panamá", "codigo_pais": "PAN", "indicador": "SH.IMM.MEAS", "cobertura": 86.0},
    {"anio": 2002, "pais": "Panamá", "codigo_pais": "PAN", "indicador": "SH.IMM.MEAS", "cobertura": 88.0},
    {"anio": 2003, "pais": "Panamá", "codigo_pais": "PAN", "indicador": "SH.IMM.MEAS", "cobertura": 90.0},
    {"anio": 2004, "pais": "Panamá", "codigo_pais": "PAN", "indicador": "SH.IMM.MEAS", "cobertura": 92.0},
    {"anio": 2005, "pais": "Panamá", "codigo_pais": "PAN", "indicador": "SH.IMM.MEAS", "cobertura": 93.0},
    {"anio": 2006, "pais": "Panamá", "codigo_pais": "PAN", "indicador": "SH.IMM.MEAS", "cobertura": 94.0},
    {"anio": 2007, "pais": "Panamá", "codigo_pais": "PAN", "indicador": "SH.IMM.MEAS", "cobertura": 95.0},
    {"anio": 2008, "pais": "Panamá", "codigo_pais": "PAN", "indicador": "SH.IMM.MEAS", "cobertura": 95.0},
    {"anio": 2009, "pais": "Panamá", "codigo_pais": "PAN", "indicador": "SH.IMM.MEAS", "cobertura": 96.0},
    {"anio": 2010, "pais": "Panamá", "codigo_pais": "PAN", "indicador": "SH.IMM.MEAS", "cobertura": 96.0},
]

def obtener_todos():
    """
    Devuelve todos los registros nacionales disponibles.
    """
    return VACUNAS_PANAMA


def obtener_por_anio(anio: int):
    """
    Devuelve el registro correspondiente a un año específico.
    Si no existe, retorna None.
    """
    for registro in VACUNAS_PANAMA:
        if registro["anio"] == anio:
            return registro
    return None
