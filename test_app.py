"""
Pruebas unitarias para la API de vacunación usando unittest.
"""

import unittest
from app import app


class VacunasApiTestCase(unittest.TestCase):
    """
    Conjunto de pruebas para los endpoints de la API.
    """

    def setUp(self):
        """
        Configura un cliente de pruebas de Flask antes de cada test.
        """
        self.app = app.test_client()
        self.app.testing = True

    def test_get_vacunas_status_code(self):
        """
        Verifica que GET /vacunas responde con código 200.
        """
        respuesta = self.app.get("/vacunas")
        self.assertEqual(respuesta.status_code, 200)

    def test_get_vacuna_por_anio_existente(self):
        """
        Verifica que GET /vacunas/2005 devuelve código 200
        cuando el año existe en los datos.
        """
        respuesta = self.app.get("/vacunas/2005")
        self.assertEqual(respuesta.status_code, 200)
        data = respuesta.get_json()
        self.assertEqual(data["anio"], 2005)

    def test_get_vacuna_por_anio_inexistente(self):
        """
        Verifica que GET /vacunas/1900 devuelve código 404
        cuando el año no existe en los datos.
        """
        respuesta = self.app.get("/vacunas/1900")
        self.assertEqual(respuesta.status_code, 404)

    def test_get_vacunas_por_provincia_existente(self):
        """
        Verifica que GET /vacunas/provincia/Chiriquí devuelve código 200
        y una lista de registros.
        """
        respuesta = self.app.get("/vacunas/provincia/Chiriquí")
        self.assertEqual(respuesta.status_code, 200)
        data = respuesta.get_json()
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)
        self.assertEqual(data[0]["provincia"], "Chiriquí")

    def test_get_vacunas_por_provincia_inexistente(self):
        """
        Verifica que GET /vacunas/provincia/Desconocida devuelve 404
        si la provincia no está soportada.
        """
        respuesta = self.app.get("/vacunas/provincia/ProvinciaInvalida")
        self.assertEqual(respuesta.status_code, 404)


if __name__ == "__main__":
    unittest.main()
