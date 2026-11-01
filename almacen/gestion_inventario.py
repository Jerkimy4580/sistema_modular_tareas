# Módulo: Gestión de Inventario en un Almacén
# Propósito: Controlar stock, entradas/salidas y calcular alertas de reabastecimiento.

def registrar_entrada(inventario, producto_id, cantidad):
    """
    Registra la entrada de nuevos productos al inventario sumando la cantidad al stock actual.
    """
    # Suma unidades al producto existente o crea un producto nuevo.
    if producto_id in inventario:
        inventario[producto_id]["stock"] += cantidad
    else:
        inventario[producto_id] = {"stock": cantidad, "minimo": 10}
    return inventario

def registrar_salida(inventario, producto_id, cantidad):
    """
    Registra la salida de productos restando del stock disponible, validando que exista suficiente.
    """
    # Verifica que el producto exista y tenga stock suficiente.
    if producto_id in inventario and inventario[producto_id]["stock"] >= cantidad:
        inventario[producto_id]["stock"] -= cantidad
        return True
    return False

def calcular_nivel_optimo(demanda_promedio, tiempo_entrega_dias):
    """
    Calcula el stock de seguridad y nivel óptimo de inventario basado en la demanda y tiempos logísticos.
    """
    # Reserva unidades adicionales para cubrir imprevistos.
    stock_seguridad = demanda_promedio * 2
    # Calcula el nivel necesario durante el tiempo de entrega.
    nivel_optimo = (demanda_promedio * tiempo_entrega_dias) + stock_seguridad
    return nivel_optimo

def generar_alertas_reabastecimiento(inventario):
    """
    Verifica el inventario general y genera una lista de productos que requieren reabastecimiento urgente.
    """
    # Guarda los productos que llegaron al minimo permitido.
    alertas = []
    # Revisa el stock de cada producto del inventario.
    for producto_id, datos in inventario.items():
        if datos["stock"] <= datos.get("minimo", 10):
            alertas.append(f"Alerta: Producto '{producto_id}' bajo en stock ({datos['stock']} unidades).")
    return alertas

# --- Ejecución Directa del Problema 2 ---
# Ejecuta las operaciones principales de control de inventario.
print("=== EJECUCIÓN PROBLEMA 2: Gestión de Inventario ===")
inventario_actual = {"Laptop": {"stock": 5, "minimo": 8}, "Mouse": {"stock": 25, "minimo": 10}}
print(f"Inventario Inicial: {inventario_actual}")

registrar_entrada(inventario_actual, "Laptop", 15)
print(f"Inventario tras entrada de Laptops: {inventario_actual}")

salida_exitosa = registrar_salida(inventario_actual, "Mouse", 20)
print(f"Salida de 20 Mouses exitosa?: {salida_exitosa}")

nivel_opt = calcular_nivel_optimo(demanda_promedio=5, tiempo_entrega_dias=4)
print(f"Nivel óptimo calculado para nuevo producto: {nivel_opt}")

alertas = generar_alertas_reabastecimiento(inventario_actual)
print(f"Alertas Generadas: {alertas}\n")