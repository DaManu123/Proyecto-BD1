-- ================================================
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

-- Usuario: Admin (contraseña: admin23)
INSERT INTO usuarios (nombre, contraseña) 
VALUES ('Admin', 'a91f03728b77f15f1398d392928c3c6d64e3c2123e6f0af415008962c91d871d');

-- Usuario: almacen (contraseña: almacen11)
INSERT INTO usuarios (nombre, contraseña) 
VALUES ('almacen', '4b16dfdfada4260fdc51e551a59ba002acafb6bfd6ec28e25a8d1f813496c7af');

-- Usuario: productos (contraseña: producto19)
INSERT INTO usuarios (nombre, contraseña) 
VALUES ('productos', '967afe6101d91405da25f4a85ab128db33e26b47c35508a3339bc423e7cf79f8');

-- ================================================
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
-- ================================================