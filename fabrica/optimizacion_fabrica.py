# Módulo: Optimización de la Producción en una Fábrica
# Propósito: Monitorear maquinaria, programar mantenimiento preventivo y alinear producción con la demanda.

def monitorear_estado_maquinas(maquina_id):
    """
    Monitorea métricas en tiempo real de una máquina (temperatura de motor, vibración, estado operativo).
    """
    estado = {
        "id": maquina_id,
        "operativa": True,
        "temperatura_motor_c": 82.0,
        "vibracion_hz": 4.1
    }
    return estado

def planificar_mantenimiento(horas_operacion_acumuladas):
    """
    Determina si una máquina requiere mantenimiento preventivo basándose en sus horas acumuladas de uso.
    """
    limite_mantenimiento = 500
    requiere_revision = horas_operacion_acumuladas >= limite_mantenimiento
    return requiere_revision

def analizar_rendimiento_produccion(unidades_producidas, tiempo_horas):
    """
    Calcula la eficiencia general midiendo la tasa de producción por hora.
    """
    if tiempo_horas == 0:
        return 0.0
    tasa_rendimiento = unidades_producidas / tiempo_horas
    return round(tasa_rendimiento, 2)

def ajustar_programacion_demanda(demanda_mercado_unidades, capacidad_actual):
    """
    Procedimiento para recalcular turnos y velocidad de las líneas de ensamblaje en función de los pedidos.
    """
    if demanda_mercado_unidades > capacidad_actual:
        print("Activando turno extra de producción para cubrir exceso de demanda.")
    else:
        print("Capacidad actual suficiente. Manteniendo ritmo estándar.")

# --- Ejecución Directa del Problema 4 ---
print("=== EJECUCIÓN PROBLEMA 4: Optimización de Fábrica ===")
estado_maq = monitorear_estado_maquinas("CNC-03")
print(f"Estado de Máquina CNC-03: {estado_maq}")

necesita_mant = planificar_mantenimiento(520)
print(f"¿Requiere mantenimiento preventivo (520 hrs acumuladas)?: {necesita_mant}")

rendimiento = analizar_rendimiento_produccion(1250, 8)
print(f"Rendimiento de producción: {rendimiento} unidades/hora")

print("Ejecutando ajuste por demanda:")
ajustar_programacion_demanda(1500, 1200)
print()