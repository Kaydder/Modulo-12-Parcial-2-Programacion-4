# Modulo-12-Parcial-2-Programacion-4
# API de Vacunación contra el Sarampión en Panamá

**Autor:** Kayder Murillo  
**Materia:** Programación 4 - Módulo 12  
**Proyecto:** Parcial 2 - API RESTful en Flask  
**Universidad:** Universidad Interamericana de Panamá  

---

##  Descripción General

Esta API RESTful fue desarrollada en **Python 3** utilizando el framework **Flask**.  
Su propósito es **consultar datos históricos sobre la vacunación contra el sarampión** en niños de **12 a 23 meses** en Panamá, con base en el indicador **SH.IMM.MEAS** del Banco Mundial.

El sistema permite realizar consultas por **año**, **provincia** (simulada) o listar todos los registros disponibles.

---

## Funcionalidades Principales

| Método | Endpoint | Descripción |
|---------|-----------|-------------|
| **GET** | `/vacunas` | Devuelve todos los registros de vacunación a nivel nacional. |
| **GET** | `/vacunas/<año>` | Devuelve los datos del año especificado (por ejemplo, 2005). |
| **GET** | `/vacunas/provincia/<nombre>` | Devuelve los datos simulados para una provincia específica. |
| **GET** | `/` | Muestra información general sobre la API y los endpoints disponibles. |
