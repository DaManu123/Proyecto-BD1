-- ================================================
-- CONSULTA SQL PARA AUMENTAR PRECIOS
-- Incrementar $1000 pesos a TODOS los productos
-- ================================================

-- Actualizar el precio de todos los productos sumando $1000
UPDATE productos 
SET precio = precio + 1000.0;

-- ================================================
-- Esta consulta aumentará $1000 pesos al precio actual
-- de todos los productos en la base de datos
-- ================================================