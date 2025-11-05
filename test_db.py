#!/usr/bin/env python3
"""
Script de prueba para verificar la funcionalidad de la aplicación
"""

from src.models.database import DatabaseModel

def test_database_connection():
    """Prueba la conexión y funcionamiento de la base de datos"""
    print("=== PRUEBA DE CONEXIÓN A BASE DE DATOS ===")
    
    # Crear instancia del modelo
    db = DatabaseModel()
    
    # Probar obtener productos
    print("\n--- Productos en la base de datos ---")
    productos = db.get_all_productos()
    if productos:
        print(f"Se encontraron {len(productos)} productos:")
        for i, producto in enumerate(productos[:5], 1):  # Mostrar solo los primeros 5
            print(f"  {i}. ID: {producto[0]}, Nombre: {producto[1]}, Precio: ${producto[2]}")
        if len(productos) > 5:
            print(f"  ... y {len(productos) - 5} productos más")
    else:
        print("No se encontraron productos en la base de datos")
    
    # Probar obtener almacenes
    print("\n--- Almacenes en la base de datos ---")
    almacenes = db.get_all_almacenes()
    if almacenes:
        print(f"Se encontraron {len(almacenes)} almacenes:")
        for i, almacen in enumerate(almacenes, 1):
            print(f"  {i}. ID: {almacen[0]}, Nombre: {almacen[1]}")
    else:
        print("No se encontraron almacenes en la base de datos")
    
    # Cerrar conexión
    db.disconnect()
    print("\n=== PRUEBA COMPLETADA ===")

if __name__ == "__main__":
    test_database_connection()