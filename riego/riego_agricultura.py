# Módulo: Sistema de Riego Automatizado para Agricultura
# Propósito: Optimizar el recurso hídrico analizando humedad del suelo, clima y necesidades del cultivo.

def leer_datos_sensores_humedad(seccion_id):
    """
    Lee el porcentaje actual de humedad en el suelo mediante sensores instalados en campo.
    """
    lectura_suelo = {
        "seccion": seccion_id,
        "humedad_porcentaje": 22.0
    }
    return lectura_suelo

def consultar_prevision_meteorologica(ubicacion):
    """
    Consulta la previsión meteorológica externa para evaluar la probabilidad de lluvia.
    """
    prevision = {
        "ubicacion": ubicacion,
        "probabilidad_lluvia": 10,
        "temperatura_ambiente": 25.0
    }
    return prevision

def calcular_cantidad_riego(humedad_actual, probabilidad_lluvia):
    """
    Calcula los litros exactos de agua necesarios por metro cuadrado según la sequedad del suelo y clima.
    """
    if probabilidad_lluvia > 60:
        return 0.0
    
    deficit = max(0.0, 60.0 - humedad_actual)
    litros_por_m2 = deficit * 0.4
    return round(litros_por_m2, 2)

def controlar_valvulas_riego(seccion_id, volumen_agua_litros):
    """
    Procedimiento que abre o cierra las electroválvulas de riego automatizado en secciones específicas.
    """
    if volumen_agua_litros > 0:
        print(f"Abriendo válvulas de la sección {seccion_id}. Suministrando {volumen_agua_litros} L/m².")
    else:
        print(f"Cerrando válvulas de la sección {seccion_id}: Riego suspendido.")

# --- Ejecución Directa del Problema 5 ---
print("=== EJECUCIÓN PROBLEMA 5: Sistema de Riego ===")
seccion = "Sector Norte"
suelo = leer_datos_sensores_humedad(seccion)
print(f"Lectura de humedad: {suelo}")

clima = consultar_prevision_meteorologica("Valle Agrícola")
print(f"Previsión meteorológica: {clima}")

agua_necesaria = calcular_cantidad_riego(suelo["humedad_porcentaje"], clima["probabilidad_lluvia"])
print(f"Cantidad de agua calculada: {agua_necesaria} L/m²")

print("Ejecutando actuadores:")
controlar_valvulas_riego(seccion, agua_necesaria)
print()