#!/usr/bin/env python3
"""
Script para generar hashes de contraseñas y crear tabla usuarios
"""

import hashlib
import sys
import os

# Para este proyecto educativo, usaremos SHA256 por simplicidad
# En producción se recomendaría bcrypt o argon2

def generar_hash_sha256(password):
    """Genera un hash SHA256 de la contraseña"""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def crear_sql_usuarios():
    """Crea el archivo SQL con los usuarios y contraseñas hasheadas"""
    
    # Datos de usuarios
    usuarios = [
        {"nombre": "Admin", "password": "admin23"},
        {"nombre": "almacen", "password": "almacen11"},
        {"nombre": "productos", "password": "producto19"}
    ]
    
    print("=== GENERACIÓN DE TABLA USUARIOS ===")
    print()
    
    # Generar hashes
    for usuario in usuarios:
        hash_password = generar_hash_sha256(usuario["password"])
        usuario["hash"] = hash_password
        print(f"Usuario: {usuario['nombre']}")
        print(f"Contraseña: {usuario['password']}")
        print(f"Hash SHA256: {hash_password}")
        print("-" * 50)
    
    # Crear contenido SQL
    sql_content = """-- ================================================
-- CREACIÓN DE TABLA USUARIOS
-- Sistema de Inventario - Universidad de Sonora
-- ================================================

-- Crear tabla usuarios con campos requeridos
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL UNIQUE,
    contraseña TEXT NOT NULL,
    ultimo_inicio_sesion DATETIME DEFAULT NULL
);

-- ================================================
-- INSERTAR USUARIOS INICIALES CON CONTRASEÑAS ENCRIPTADAS (SHA256)
-- ================================================

"""
    
    # Agregar inserts para cada usuario
    for usuario in usuarios:
        sql_content += f"""-- Usuario: {usuario['nombre']} (contraseña: {usuario['password']})
INSERT INTO usuarios (nombre, contraseña) 
VALUES ('{usuario['nombre']}', '{usuario['hash']}');

"""
    
    sql_content += """-- ================================================
-- VERIFICACIÓN DE TABLA CREADA
-- ================================================

-- Ver estructura de la tabla
.schema usuarios

-- Ver usuarios insertados
SELECT id, nombre, 
       SUBSTR(contraseña, 1, 16) || '...' as contraseña_hash,
       ultimo_inicio_sesion 
FROM usuarios;

-- ================================================
-- NOTAS IMPORTANTES:
-- 
-- 1. Las contraseñas están encriptadas con SHA256
-- 2. El campo ultimo_inicio_sesion se actualiza al hacer login
-- 3. El campo nombre tiene restricción UNIQUE
-- 4. Para verificar contraseñas en Python:
--    import hashlib
--    hash_input = hashlib.sha256(password.encode('utf-8')).hexdigest()
--    if hash_input == stored_hash:
--        # Contraseña correcta
-- ================================================"""
    
    # Escribir archivo SQL
    with open('crear_tabla_usuarios_final.sql', 'w', encoding='utf-8') as f:
        f.write(sql_content)
    
    print(f"✅ Archivo SQL generado: crear_tabla_usuarios_final.sql")
    print(f"✅ Total de usuarios: {len(usuarios)}")
    
if __name__ == "__main__":
    crear_sql_usuarios()