-- Script para agregar columnas de auditoría a productos y almacenes

-- Agregar columnas a la tabla productos
ALTER TABLE productos ADD COLUMN fecha_ultima_modificacion DATETIME;
ALTER TABLE productos ADD COLUMN ultimo_usuario_modificacion TEXT;

-- Agregar columnas a la tabla almacenes
ALTER TABLE almacenes ADD COLUMN fecha_ultima_modificacion DATETIME;
ALTER TABLE almacenes ADD COLUMN ultimo_usuario_modificacion TEXT;

-- Inicializar las fechas con la fecha actual para registros existentes
UPDATE productos SET fecha_ultima_modificacion = datetime('now') WHERE fecha_ultima_modificacion IS NULL;
UPDATE almacenes SET fecha_ultima_modificacion = datetime('now') WHERE fecha_ultima_modificacion IS NULL;

-- Verificar los cambios en productos
SELECT id, nombre, fecha_ultima_modificacion, ultimo_usuario_modificacion FROM productos LIMIT 5;

-- Verificar los cambios en almacenes
SELECT id, nombre, fecha_ultima_modificacion, ultimo_usuario_modificacion FROM almacenes LIMIT 5;
