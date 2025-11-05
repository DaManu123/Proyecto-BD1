#!/usr/bin/env python3
"""
Script de prueba para validar contraseñas de usuarios
"""

import sys
import os
import hashlib

# Agregar el directorio del proyecto al path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

try:
    from models.database import DatabaseModel
except ImportError:
    print("No se puede importar DatabaseModel, ejecutando prueba manual...")

def verificar_password(password_input, stored_hash):
    """Verifica si la contraseña ingresada coincide con el hash almacenado"""
    hash_input = hashlib.sha256(password_input.encode('utf-8')).hexdigest()
    return hash_input == stored_hash

def test_usuarios_login():
    """Prueba el sistema de login de usuarios"""
    print("=== PRUEBA DE VALIDACIÓN DE USUARIOS ===")
    print()
    
    # Datos de prueba
    test_cases = [
        {"usuario": "Admin", "password": "admin23", "esperado": True},
        {"usuario": "Admin", "password": "admin24", "esperado": False},
        {"usuario": "almacen", "password": "almacen11", "esperado": True},
        {"usuario": "almacen", "password": "almacen12", "esperado": False},
        {"usuario": "productos", "password": "producto19", "esperado": True},
        {"usuario": "productos", "password": "producto20", "esperado": False},
    ]
    
    # Obtener datos de la base de datos
    try:
        # Conectar a la base de datos manualmente
        import sqlite3
        conn = sqlite3.connect('database/InventarioBD_2.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT nombre, contraseña FROM usuarios")
        usuarios_db = {row[0]: row[1] for row in cursor.fetchall()}
        conn.close()
        
        print("Usuarios en base de datos:")
        for nombre in usuarios_db.keys():
            print(f"  - {nombre}")
        print()
        
    except Exception as e:
        print(f"Error al conectar con la base de datos: {e}")
        return
    
    # Ejecutar pruebas
    resultados = []
    for test in test_cases:
        usuario = test["usuario"]
        password = test["password"]
        esperado = test["esperado"]
        
        if usuario in usuarios_db:
            stored_hash = usuarios_db[usuario]
            resultado = verificar_password(password, stored_hash)
            
            status = "✅ PASS" if resultado == esperado else "❌ FAIL"
            resultados.append(resultado == esperado)
            
            print(f"{status} - Usuario: {usuario}, Password: {password}")
            print(f"      Esperado: {esperado}, Obtenido: {resultado}")
        else:
            print(f"❌ FAIL - Usuario {usuario} no encontrado en BD")
            resultados.append(False)
        
        print()
    
    # Resumen
    exitosos = sum(resultados)
    total = len(resultados)
    
    print("=" * 50)
    print(f"RESULTADOS: {exitosos}/{total} pruebas exitosas")
    
    if exitosos == total:
        print("🎉 ¡Todas las pruebas pasaron correctamente!")
    else:
        print("⚠️  Algunas pruebas fallaron")
    
    print("=" * 50)

if __name__ == "__main__":
    test_usuarios_login()