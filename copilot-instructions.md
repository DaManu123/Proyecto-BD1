# Copilot Instructions - Sistema de Inventario

Este archivo sirve como fuente de verdad para GitHub Copilot sobre la arquitectura, stack tecnológico y reglas de este proyecto.

## 📋 Propósito del Proyecto

Una aplicación de escritorio educativa para la clase de **"Bases de Datos 1"** en la Universidad de Sonora.

### Objetivos:
- ✅ Visualizar datos de tablas de base de datos SQLite
- ✅ Implementar arquitectura MVC estricta
- ✅ Crear estructura de UI para operaciones CRUD (solo estructura por ahora)
- ❌ **NO implementar funcionalidad real de agregar/eliminar** (solo placeholders)

## 🛠️ Stack Tecnológico

| Componente | Tecnología | Versión |
|------------|------------|---------|
| **Lenguaje** | Python | 3.7+ |
| **GUI Framework** | Tkinter + ttk | Built-in |
| **Base de Datos** | SQLite | 3.x |
| **IDE** | VS Code | - |

### Librerías Principales:
```python
import tkinter as tk
from tkinter import ttk
import sqlite3
```

## 🏗️ Arquitectura MVC Estricta

### 📁 Estructura de Archivos
```
src/
├── models/
│   └── database.py         # Modelo (Datos)
├── views/
│   └── main_view.py        # Vista (UI)
├── controllers/
│   └── main_controller.py  # Controlador (Lógica)
└── main.py                 # Punto de entrada
```

### 🎯 Separación de Responsabilidades

#### 1. **MODELO** (`models/database.py`)
```python
class DatabaseModel:
    """ÚNICA responsabilidad: Interacción con base de datos"""
```

**✅ DEBE:**
- Manejar toda la conexión SQLite con `InventarioBD_2.db`
- Contener métodos: `get_all_productos()`, `get_all_almacenes()`
- Manejar errores de base de datos
- Retornar datos como listas/tuplas

**❌ NUNCA DEBE:**
- Importar `tkinter` o cualquier módulo de UI
- Contener lógica de presentación
- Manejar eventos de UI

#### 2. **VISTA** (`views/main_view.py`)
```python
class MainView:
    """ÚNICA responsabilidad: Crear y posicionar widgets"""
```

**✅ DEBE:**
- Crear todos los widgets de Tkinter/ttk
- Posicionar y configurar la UI
- Definir frames: `InicioFrame`, `ProductosFrame`, `AlmacenesFrame`
- Exponer métodos para actualizar datos: `update_productos_tree()`, `update_almacenes_tree()`

**❌ NUNCA DEBE:**
- Importar `sqlite3` o hacer consultas DB
- Contener lógica de aplicación
- Decidir qué hacer cuando se presiona un botón (solo informar al controlador)

#### 3. **CONTROLADOR** (`controllers/main_controller.py`)
```python
class MainController:
    """Punto de entrada y coordinador MVC"""
```

**✅ DEBE:**
- Instanciar `DatabaseModel` y `MainView`
- Conectar eventos de botones con métodos del controlador
- Manejar navegación: `show_frame(frame_name)`
- Pedir datos al modelo y pasarlos a la vista
- Contener toda la lógica de aplicación

## 🗄️ Esquema de Base de Datos

### Base de Datos: `InventarioBD_2.db`

#### Tabla: `productos`
```sql
CREATE TABLE productos (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    precio REAL NOT NULL,
    cantidad INTEGER NOT NULL,
    departamento TEXT NOT NULL,
    almacen TEXT NOT NULL
);
```

#### Tabla: `almacenes`
```sql
CREATE TABLE almacenes (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL
);
```

## 🎨 Especificaciones de UI

### Navegación por Frames
- **✅ USAR:** Una ventana raíz única con `frame.tkraise()`
- **❌ NUNCA:** Crear ventanas `Toplevel` adicionales

### Widgets Requeridos
- **✅ PREFERIR:** `ttk` widgets sobre `tk` simples
- **Ejemplos:** `ttk.Button`, `ttk.Entry`, `ttk.Treeview`, `ttk.Label`

### Estructura de Frames:

#### 🏠 **Frame de Inicio**
```python
# Contenido:
- Label: "Universidad de Sonora"
- Label: "[Nombre del estudiante]"
- Button: "Productos" → show_frame("productos")
- Button: "Almacenes" → show_frame("almacenes")
```

#### 📦 **Frame de Productos**
```python
# Contenido:
- Label: "Gestión de Productos"
- ttk.Treeview: columnas (id, nombre, precio, cantidad, departamento, almacen)
- Formulario: Entry fields para cada columna
- Button: "Agregar Producto" → agregar_producto() [placeholder]
- Button: "Eliminar Producto" → eliminar_producto() [placeholder]
- Button: "Volver al Inicio" → show_frame("inicio")
```

#### 🏪 **Frame de Almacenes**
```python
# Contenido:
- Label: "Gestión de Almacenes"
- ttk.Treeview: columnas (id, nombre)
- Formulario: Entry fields para id y nombre
- Button: "Agregar Almacén" → agregar_almacen() [placeholder]
- Button: "Eliminar Almacén" → eliminar_almacen() [placeholder]
- Button: "Volver al Inicio" → show_frame("inicio")
```

## ⚠️ Reglas y Restricciones Críticas

### 🚫 Prohibiciones Estrictas

1. **Arquitectura MVC:**
   - Modelo NO puede importar tkinter
   - Vista NO puede importar sqlite3
   - NO mezclar responsabilidades entre capas

2. **Navegación:**
   - NO crear ventanas `Toplevel`
   - Solo usar `frame.tkraise()` para cambiar vistas

3. **Funcionalidad:**
   - Botones "Agregar/Eliminar" SOLO deben tener `pass`
   - NO implementar funcionalidad CRUD real

### ✅ Buenas Prácticas Requeridas

1. **Widgets:**
   ```python
   # ✅ USAR
   import tkinter as tk
   from tkinter import ttk
   
   button = ttk.Button(parent, text="Click")
   tree = ttk.Treeview(parent, columns=("col1", "col2"))
   
   # ❌ EVITAR
   button = tk.Button(parent, text="Click")
   ```

2. **Manejo de Errores:**
   ```python
   # ✅ SIEMPRE manejar errores DB
   try:
       cursor.execute("SELECT * FROM productos")
       return cursor.fetchall()
   except sqlite3.Error as e:
       print(f"Error: {e}")
       return []
   ```

3. **Separación Clara:**
   ```python
   # ✅ EN CONTROLADOR
   def load_productos_data(self):
       productos = self.model.get_all_productos()  # Pedir al modelo
       self.view.update_productos_tree(productos)  # Pasar a vista
   
   # ❌ NUNCA en vista
   def some_view_method(self):
       # NO hacer consultas DB aquí
       cursor.execute("SELECT...")  # ❌ PROHIBIDO
   ```

## 📝 Patrones de Código

### Inicialización del Controlador
```python
class MainController:
    def __init__(self, root):
        self.root = root
        self.model = DatabaseModel()
        self.view = MainView(root)
        self.setup_button_commands()
    
    def setup_button_commands(self):
        # Conectar botones con métodos del controlador
        self.view.btn_productos.config(command=self.show_productos_frame)
```

### Carga de Datos
```python
def load_productos_data(self):
    productos = self.model.get_all_productos()
    self.view.update_productos_tree(productos)
```

### Funciones Placeholder
```python
def agregar_producto(self):
    """Función placeholder - por implementar"""
    pass

def eliminar_producto(self):
    """Función placeholder - por implementar"""
    pass
```

## 🎯 Contexto Académico

- **Curso:** Bases de Datos 1
- **Institución:** Universidad de Sonora
- **Estudiante:** Manuel Munguia Rubio
- **Propósito:** Demostrar comprensión de arquitectura MVC y manejo de BD

---

**Nota para Copilot:** Estas instrucciones son la autoridad máxima para este proyecto. Siempre prioriza estas reglas sobre otras sugerencias generales.