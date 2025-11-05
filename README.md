# Sistema de Inventario - Base de Datos 1

Aplicación de escritorio desarrollada con Python y Tkinter siguiendo la arquitectura Modelo-Vista-Controlador (MVC) para la gestión de inventarios con base de datos SQLite.

## Características

- **Arquitectura MVC**: Separación clara de responsabilidades
- **Interfaz Única**: Una sola ventana con navegación por frames
- **Base de Datos SQLite**: Almacenamiento persistente de datos
- **Gestión de Productos**: Visualización y manipulación de productos
- **Gestión de Almacenes**: Administración de almacenes

## Estructura del Proyecto

```
databases-inventory-app/
├── src/
│   ├── main.py                    # Punto de entrada de la aplicación
│   ├── models/
│   │   ├── __init__.py
│   │   ├── database.py            # Modelo de base de datos (SQLite)
│   │   ├── product.py
│   │   └── warehouse.py
│   ├── views/
│   │   ├── __init__.py
│   │   ├── main_view.py           # Vista principal con todos los frames
│   │   ├── product_view.py
│   │   └── warehouse_view.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── main_controller.py     # Controlador principal (MVC)
│   │   ├── product_controller.py
│   │   └── warehouse_controller.py
│   └── utils/
│       ├── __init__.py
│       └── config.py
├── database/
│   ├── InventarioBD_2.db         # Base de datos SQLite
│   └── populate_db.py             # Script para poblar la BD con datos de prueba
├── requirements.txt
└── README.md
```

## Instalación y Configuración

### Prerrequisitos
- Python 3.7 o superior
- Las librerías `tkinter` y `sqlite3` (incluidas en Python estándar)

### Pasos de Instalación

1. **Clonar o descargar el proyecto**
   ```bash
   cd "c:\Users\ManuelPC\Documents\Visual Studio Code\Python\Proyecto bd1\databases-inventory-app"
   ```

2. **Crear y activar entorno virtual** (Recomendado)
   ```bash
   # Crear entorno virtual
   python -m venv venv
   
   # Activar entorno virtual
   # En Windows:
   venv\Scripts\activate
   
   # En Linux/Mac:
   source venv/bin/activate
   ```

3. **Poblar la base de datos con datos de prueba** (opcional)
   ```bash
   python database/populate_db.py
   ```

4. **Ejecutar la aplicación**
   ```bash
   # Opción 1: Script automático con entorno virtual
   run_with_venv.bat
   
   # Opción 2: Manual (con venv activado)
   python src/main.py
   
   # Opción 3: PowerShell
   .\activate_venv.ps1
   python src\main.py
   ```

## Uso de la Aplicación

### Pantalla de Inicio
- Muestra "Universidad de Sonora"
- Muestra nombres de estudiantes
- Botones de navegación: "Productos" y "Almacenes"

### Gestión de Productos
- **Visualización**: Tabla con columnas: ID, Nombre, Precio, Cantidad, Departamento, Almacén
- **Formulario**: Campos de entrada para todos los atributos
- **Botones**: 
  - "Agregar Producto" (por implementar)
  - "Eliminar Producto" (por implementar)
  - "Volver al Inicio"

### Gestión de Almacenes
- **Visualización**: Tabla con columnas: ID, Nombre
- **Formulario**: Campos de entrada para ID y Nombre
- **Botones**: 
  - "Agregar Almacén" (por implementar)
  - "Eliminar Almacén" (por implementar)
  - "Volver al Inicio"

## Arquitectura MVC

### Modelo (`models/database.py`)
- **Responsabilidad**: Manejo de datos y lógica de base de datos
- **Funciones principales**:
  - Conexión a SQLite (`InventarioBD_2.db`)
  - `get_all_productos()`: Obtiene todos los productos
  - `get_all_almacenes()`: Obtiene todos los almacenes
  - Manejo de errores de conexión

### Vista (`views/main_view.py`)
- **Responsabilidad**: Interfaz de usuario y presentación
- **Componentes**:
  - Frame de Inicio
  - Frame de Productos (con Treeview y formulario)
  - Frame de Almacenes (con Treeview y formulario)
  - Navegación entre frames

### Controlador (`controllers/main_controller.py`)
- **Responsabilidad**: Lógica de aplicación y coordinación
- **Funciones principales**:
  - Inicialización del modelo y vista
  - Navegación entre frames (`show_frame()`)
  - Carga de datos (`load_productos_data()`, `load_almacenes_data()`)
  - Manejo de eventos de botones
  - Gestión del ciclo de vida de la aplicación

## Estructura de la Base de Datos

### Tabla: `productos`
```sql
CREATE TABLE productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    precio REAL NOT NULL,
    cantidad INTEGER NOT NULL,
    departamento TEXT NOT NULL,
    almacen TEXT NOT NULL
);
```

### Tabla: `almacenes`
```sql
CREATE TABLE almacenes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
);
```

## Notas de Desarrollo

- Los botones "Agregar" y "Eliminar" están conectados a funciones vacías que usan `pass`
- La aplicación carga automáticamente los datos al navegar a cada sección
- Se incluye manejo básico de errores para la conexión de base de datos
- El script `populate_db.py` crea datos de prueba para demostración

## Estudiante

**Manuel Munguia Rubio**  
Universidad de Sonora  
Carrera: Ingeniería en Sistemas Computacionales  
Materia: Bases de Datos 1

## Licencia

Este proyecto es para fines educativos - Universidad de Sonora