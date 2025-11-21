-- Script para agregar columna 'rol' a la tabla usuarios
-- y asignar roles según el nombre de usuario

-- Agregar columna rol si no existe
ALTER TABLE usuarios ADD COLUMN rol TEXT DEFAULT 'PRODUCTOS';

-- Asignar roles según el nombre de usuario
UPDATE usuarios SET rol = 'ADMIN' WHERE nombre = 'Admin';
UPDATE usuarios SET rol = 'ALMACEN' WHERE nombre = 'almacen';
UPDATE usuarios SET rol = 'PRODUCTOS' WHERE nombre = 'productos';

-- Verificar los cambios
SELECT id, nombre, rol FROM usuarios;
