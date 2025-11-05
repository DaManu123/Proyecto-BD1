-- ================================================
-- 50 CONSULTAS SQL PARA AGREGAR DATOS
-- 45 Nuevos Productos + 5 Nuevos Almacenes
-- ================================================

-- PRIMERO: 5 NUEVOS ALMACENES
-- ================================================

-- Almacén 6: Puerto Peñasco
INSERT INTO almacenes (id, nombre) VALUES (6, 'puerto peñasco');

-- Almacén 7: Agua Prieta
INSERT INTO almacenes (id, nombre) VALUES (7, 'agua prieta');

-- Almacén 8: Navojoa
INSERT INTO almacenes (id, nombre) VALUES (8, 'navojoa');

-- Almacén 9: Ciudad Obregón
INSERT INTO almacenes (id, nombre) VALUES (9, 'ciudad obregon');

-- Almacén 10: San Luis Río Colorado
INSERT INTO almacenes (id, nombre) VALUES (10, 'san luis rio colorado');

-- ================================================
-- AHORA: 45 NUEVOS PRODUCTOS
-- ================================================

-- Productos 63-107 (45 productos nuevos)

-- Producto 63: Monitor Gaming 24"
INSERT INTO productos (id, nombre, precio, cantidad, departamento, almacen) 
VALUES (63, 'Monitor Gaming 24 pulgadas', 4500.0, 15, 'electronica', 1);

-- Producto 64: Teclado Mecánico RGB
INSERT INTO productos (id, nombre, precio, cantidad, departamento, almacen) 
VALUES (64, 'Teclado Mecánico RGB', 1200.0, 25, 'electronica', 2);

-- Producto 65: Mouse Gaming Inalámbrico
INSERT INTO productos (id, nombre, precio, cantidad, departamento, almacen) 
VALUES (65, 'Mouse Gaming Inalámbrico', 800.0, 30, 'electronica', 3);

-- Producto 66: Headset Gamer 7.1
INSERT INTO productos (id, nombre, precio, cantidad, departamento, almacen) 
VALUES (66, 'Headset Gamer 7.1', 1500.0, 20, 'electronica', 4);

-- Producto 67: Webcam HD 1080p
INSERT INTO productos (id, nombre, precio, cantidad, departamento, almacen) 
VALUES (67, 'Webcam HD 1080p', 900.0, 18, 'electronica', 5);

-- Producto 68: SSD 1TB NVMe
INSERT INTO productos (id, nombre, precio, cantidad, departamento, almacen) 
VALUES (68, 'SSD 1TB NVMe', 2200.0, 12, 'almacenamiento', 6);

-- Producto 69: Memoria RAM DDR4 16GB
INSERT INTO productos (id, nombre, precio, cantidad, departamento, almacen) 
VALUES (69, 'Memoria RAM DDR4 16GB', 1800.0, 22, 'componentes', 7);

-- Producto 70: Tarjeta Gráfica GTX 1660
INSERT INTO productos (id, nombre, precio, cantidad, departamento, almacen) 
VALUES (70, 'Tarjeta Gráfica GTX 1660', 8500.0, 8, 'componentes', 8);

-- Producto 71: Procesador Intel i5
INSERT INTO productos (id, nombre, precio, cantidad, departamento, almacen) 
VALUES (71, 'Procesador Intel i5', 5500.0, 10, 'componentes', 9);

-- Producto 72: Placa Madre ATX
INSERT INTO productos (id, nombre, precio, cantidad, departamento, almacen) 
VALUES (72, 'Placa Madre ATX', 2800.0, 14, 'componentes', 10);

-- Producto 73: Fuente de Poder 650W
INSERT INTO productos (id, nombre, precio, cantidad, departamento, almacen) 
VALUES (73, 'Fuente de Poder 650W', 1600.0, 16, 'componentes', 1);

-- Producto 74: Case Gaming RGB
INSERT INTO productos (id, nombre, precio, cantidad, departamento, almacen) 
VALUES (74, 'Case Gaming RGB', 2200.0, 12, 'gabinetes', 2);

-- Producto 75: Cooler CPU Líquido
INSERT INTO productos (id, nombre, precio, cantidad, departamento, almacen) 
VALUES (75, 'Cooler CPU Líquido', 2500.0, 9, 'enfriamiento', 3);

-- Producto 76: Ventilador Case 120mm
INSERT INTO productos (id, nombre, precio, cantidad, departamento, almacen) 
VALUES (76, 'Ventilador Case 120mm', 350.0, 40, 'enfriamiento', 4);

-- Producto 77: Pasta Térmica Premium
INSERT INTO productos (id, nombre, precio, cantidad, departamento, almacen) 
VALUES (77, 'Pasta Térmica Premium', 180.0, 50, 'enfriamiento', 5);

-- Producto 78: Cable HDMI 4K 2m
INSERT INTO productos (id, nombre, precio, cantidad, departamento, almacen) 
VALUES (78, 'Cable HDMI 4K 2m', 250.0, 60, 'cables', 6);

-- Producto 79: Cable USB-C 3.0
INSERT INTO productos (id, nombre, precio, cantidad, departamento, almacen) 
VALUES (79, 'Cable USB-C 3.0', 180.0, 45, 'cables', 7);

-- Producto 80: Hub USB 4 Puertos
INSERT INTO productos (id, nombre, precio, cantidad, departamento, almacen) 
VALUES (80, 'Hub USB 4 Puertos', 320.0, 25, 'accesorios', 8);

-- Producto 81: Adaptador WiFi USB
INSERT INTO productos (id, nombre, precio, cantidad, departamento, almacen) 
VALUES (81, 'Adaptador WiFi USB', 450.0, 35, 'conectividad', 9);

-- Producto 82: Router WiFi 6
INSERT INTO productos (id, nombre, precio, cantidad, departamento, almacen) 
VALUES (82, 'Router WiFi 6', 2800.0, 11, 'conectividad', 10);

-- Producto 83: Switch Ethernet 8 Puertos
INSERT INTO productos (id, nombre, precio, cantidad, departamento, almacen) 
VALUES (83, 'Switch Ethernet 8 Puertos', 650.0, 18, 'conectividad', 1);

-- Producto 84: Cable Ethernet Cat6 5m
INSERT INTO productos (id, nombre, precio, cantidad, departamento, almacen) 
VALUES (84, 'Cable Ethernet Cat6 5m', 120.0, 80, 'cables', 2);

-- Producto 85: Impresora Láser Monocromática
INSERT INTO productos (id, nombre, precio, cantidad, departamento, almacen) 
VALUES (85, 'Impresora Láser Monocromática', 3200.0, 7, 'oficina', 3);

-- Producto 86: Escáner Documentos A4
INSERT INTO productos (id, nombre, precio, cantidad, departamento, almacen) 
VALUES (86, 'Escáner Documentos A4', 1800.0, 9, 'oficina', 4);

-- Producto 87: Proyector HD 3000 Lúmenes
INSERT INTO productos (id, nombre, precio, cantidad, departamento, almacen) 
VALUES (87, 'Proyector HD 3000 Lúmenes', 8500.0, 5, 'presentacion', 5);

-- Producto 88: Pizarra Interactiva
INSERT INTO productos (id, nombre, precio, cantidad, departamento, almacen) 
VALUES (88, 'Pizarra Interactiva', 12000.0, 3, 'educacion', 6);

-- Producto 89: Tablet 10 pulgadas 128GB
INSERT INTO productos (id, nombre, precio, cantidad, departamento, almacen) 
VALUES (89, 'Tablet 10 pulgadas 128GB', 4200.0, 12, 'moviles', 7);

-- Producto 90: Smartphone 6.5" 256GB
INSERT INTO productos (id, nombre, precio, cantidad, departamento, almacen) 
VALUES (90, 'Smartphone 6.5 pulgadas 256GB', 8900.0, 8, 'moviles', 8);

-- Producto 91: Smartwatch Deportivo
INSERT INTO productos (id, nombre, precio, cantidad, departamento, almacen) 
VALUES (91, 'Smartwatch Deportivo', 2800.0, 15, 'wearables', 9);

-- Producto 92: Auriculares Bluetooth
INSERT INTO productos (id, nombre, precio, cantidad, departamento, almacen) 
VALUES (92, 'Auriculares Bluetooth', 1200.0, 28, 'audio', 10);

-- Producto 93: Bocina Portátil 20W
INSERT INTO productos (id, nombre, precio, cantidad, departamento, almacen) 
VALUES (93, 'Bocina Portátil 20W', 850.0, 22, 'audio', 1);

-- Producto 94: Micrófono Condensador USB
INSERT INTO productos (id, nombre, precio, cantidad, departamento, almacen) 
VALUES (94, 'Micrófono Condensador USB', 1500.0, 13, 'audio', 2);

-- Producto 95: Cámara Web 4K
INSERT INTO productos (id, nombre, precio, cantidad, departamento, almacen) 
VALUES (95, 'Cámara Web 4K', 2200.0, 10, 'video', 3);

-- Producto 96: Trípode Profesional
INSERT INTO productos (id, nombre, precio, cantidad, departamento, almacen) 
VALUES (96, 'Trípode Profesional', 950.0, 16, 'fotografia', 4);

-- Producto 97: Lámpara Ring Light
INSERT INTO productos (id, nombre, precio, cantidad, departamento, almacen) 
VALUES (97, 'Lámpara Ring Light', 680.0, 20, 'iluminacion', 5);

-- Producto 98: Batería Externa 20000mAh
INSERT INTO productos (id, nombre, precio, cantidad, departamento, almacen) 
VALUES (98, 'Batería Externa 20000mAh', 750.0, 25, 'energia', 6);

-- Producto 99: Cargador Inalámbrico Rápido
INSERT INTO productos (id, nombre, precio, cantidad, departamento, almacen) 
VALUES (99, 'Cargador Inalámbrico Rápido', 420.0, 30, 'energia', 7);

-- Producto 100: UPS 1200VA
INSERT INTO productos (id, nombre, precio, cantidad, departamento, almacen) 
VALUES (100, 'UPS 1200VA', 2800.0, 8, 'energia', 8);

-- Producto 101: Multímetro Digital
INSERT INTO productos (id, nombre, precio, cantidad, departamento, almacen) 
VALUES (101, 'Multímetro Digital', 580.0, 12, 'herramientas', 9);

-- Producto 102: Kit Destornilladores Precisión
INSERT INTO productos (id, nombre, precio, cantidad, departamento, almacen) 
VALUES (102, 'Kit Destornilladores Precisión', 320.0, 35, 'herramientas', 10);

-- Producto 103: Pistola de Calor
INSERT INTO productos (id, nombre, precio, cantidad, departamento, almacen) 
VALUES (103, 'Pistola de Calor', 850.0, 14, 'herramientas', 1);

-- Producto 104: Protoboard 830 Puntos
INSERT INTO productos (id, nombre, precio, cantidad, departamento, almacen) 
VALUES (104, 'Protoboard 830 Puntos', 180.0, 40, 'electronica', 2);

-- Producto 105: Arduino Uno R3
INSERT INTO productos (id, nombre, precio, cantidad, departamento, almacen) 
VALUES (105, 'Arduino Uno R3', 650.0, 25, 'microcontroladores', 3);

-- Producto 106: Raspberry Pi 4 8GB
INSERT INTO productos (id, nombre, precio, cantidad, departamento, almacen) 
VALUES (106, 'Raspberry Pi 4 8GB', 2200.0, 12, 'microcontroladores', 4);

-- Producto 107: Sensor Ultrasónico HC-SR04
INSERT INTO productos (id, nombre, precio, cantidad, departamento, almacen) 
VALUES (107, 'Sensor Ultrasónico HC-SR04', 85.0, 60, 'sensores', 5);

-- ================================================
-- RESUMEN DE CONSULTAS EJECUTADAS:
-- - 5 Almacenes nuevos (IDs 6-10)
-- - 45 Productos nuevos (IDs 63-107)
-- Total: 50 consultas INSERT
-- ================================================