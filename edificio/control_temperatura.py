# Módulo: Control de Temperatura en Edificio Inteligente
# Propósito: Optimizar el consumo energético ajustando zonas según clima, hora y ocupación.

def leer_datos_sensores(zona_id):
    """
    Simula la lectura de sensores físicos de temperatura y ocupación para una zona específica.
    Retorna un diccionario con la temperatura actual y el porcentaje de ocupación.
    """
    datos_zona = {
        "zona": zona_id,
        "temperatura_actual": 24.5,
        "ocupacion_porcentaje": 85
    }
    return datos_zona

def calcular_temperatura_optima(hora_actual, ocupacion, temperatura_exterior):
    """
    Calcula la temperatura de confort ideal basándose en la hora, ocupación y clima exterior.
    """
    base_optima = 21.0
    
    if ocupacion > 80:
        base_optima -= 1.5
    elif ocupacion < 20:
        base_optima += 1.0

    if temperatura_exterior > 30:
        base_optima += 0.5
    
    return round(base_optima, 2)

def enviar_senales_ajuste(zona_id, temperatura_objetivo):
    """
    Procedimiento que envía comandos físicos a los actuadores de calefacción o refrigeración.
    """
    comando = f"Enviando señal al HVAC de la Zona {zona_id}: Fijar temperatura a {temperatura_objetivo}°C"
    print(comando)

def registrar_analizar_consumo(zona_id, kwh_consumidos):
    """
    Registra el consumo energético actual y analiza si supera los límites ecológicos permitidos.
    """
    limite_permitido = 50.0
    eficiente = kwh_consumidos <= limite_permitido
    
    reporte = {
        "zona": zona_id,
        "consumo_kwh": kwh_consumidos,
        "estado_eficiencia": "Óptimo" if eficiente else "Alerta: Consumo elevado"
    }
    return reporte

# --- Ejecución Directa del Problema 1 ---
print("=== EJECUCIÓN PROBLEMA 1: Control de Temperatura ===")
zona_prueba = 101
datos_sensores = leer_datos_sensores(zona_prueba)
print(f"1. Lectura de Sensores: {datos_sensores}")

temp_ideal = calcular_temperatura_optima(14, datos_sensores["ocupacion_porcentaje"], 32.0)
print(f"2. Temperatura Óptima Calculada: {temp_ideal}°C")

print("3. Ejecutando Actuadores:")
enviar_senales_ajuste(zona_prueba, temp_ideal)

resultado_consumo = registrar_analizar_consumo(zona_prueba, 42.8)
print(f"4. Análisis de Consumo: {resultado_consumo}\n")