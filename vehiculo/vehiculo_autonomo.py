# Módulo: Sistema de Navegación para Vehículo Autónomo
# Propósito: Procesar sensores, calcular rutas, evitar obstáculos y ajustar velocidad en tiempo real.

def leer_datos_sensores():
    """
    Lee datos en tiempo real de cámaras y sensores LiDAR o de proximidad ultrasónicos.
    """
    # Simula las lecturas recibidas desde los sensores del vehiculo.
    lecturas = {
        "distancia_frontal_metros": 12.0,
        "objetos_detectados": ["peaton_cruzando"],
        "calidad_vision_camara": "Alta"
    }
    return lecturas

def calcular_ruta_optima(punto_partida, punto_destino):
    """
    Calcula la ruta más eficiente entre dos puntos geográficos evitando tráfico denso.
    """
    # Construye una ruta con puntos intermedios.
    ruta_generada = [punto_partida, "Avenida Simón Bolívar", "Desvío Norte", punto_destino]
    return ruta_generada

def detectar_evitar_obstaculos(datos_sensores):
    """
    Analiza la distancia frontal y objetos cercanos para determinar si se requiere una maniobra evasiva.
    """
    # Obtiene la distancia frontal o usa un valor seguro por defecto.
    distancia = datos_sensores.get("distancia_frontal_metros", 100)
    # Decide la accion segun la cercania del obstaculo.
    if distancia < 5.0:
        return "Maniobra de emergencia: Frenado total y viraje evasivo"
    elif distancia < 15.0:
        return "Precaución: Reducir velocidad y mantener carril"
    return "Trayectoria libre"

def ajustar_velocidad_trafico(condicion_trafico):
    """
    Procedimiento que ajusta la velocidad máxima permitida del vehículo autónomo según el tráfico.
    """
    # Define la velocidad maxima para cada condicion de trafico.
    velocidades = {
        "fluido": 60,
        "denso": 30,
        "congestionado": 10,
        "detenido": 0
    }
    # Usa una velocidad moderada si la condicion no esta registrada.
    velocidad_objetivo = velocidades.get(condicion_trafico, 40)
    print(f"Ajustando velocidad crucero a {velocidad_objetivo} km/h por tráfico: {condicion_trafico}")

# --- Ejecución Directa del Problema 3 ---
# Ejecuta el flujo completo de navegacion del vehiculo.
print("=== EJECUCIÓN PROBLEMA 3: Vehículo Autónomo ===")
sensores = leer_datos_sensores()
print(f"Lectura de sensores: {sensores}")

ruta = calcular_ruta_optima("Sur", "Norte")
print(f"Ruta óptima calculada: {ruta}")

estado_obstaculo = detectar_evitar_obstaculos(sensores)
print(f"Estado de obstáculos: {estado_obstaculo}")

print("Ejecutando ajuste de velocidad:")
ajustar_velocidad_trafico("denso")
print()