# Sistema de Inventario UNISON - AI Coding Instructions

Educational desktop application for Database 1 course at Universidad de Sonora. Built with Python + Tkinter following strict MVC architecture, featuring role-based access control (RBAC), audit logging, and UNISON institutional branding.

---

## 🏗️ Architecture Overview

### Single-Window Pattern with Frame Switching

The app uses **ONE** root window with a persistent `main_container` Frame. Views are swapped by destroying container children and creating new views inside it—**NEVER** destroy the root or create `Toplevel` windows. This prevents flickering during transitions.

```python
# ✅ Correct: Smooth transitions
for widget in self.main_container.winfo_children():
    widget.destroy()
self.main_view = MainView(self.main_container)

# ❌ Wrong: Causes flicker and breaks single-window pattern
self.root.destroy()
new_root = Tk()
```

### MVC Boundaries (Strictly Enforced)

**Separation of concerns is critical:**

- **`models/database.py`**: SQLite operations ONLY—NO `tkinter` imports, pure data layer
- **`views/`**: UI widgets ONLY—NO `sqlite3` imports, NO business logic, pure presentation
- **`controllers/integrated_controller_simple.py`**: Orchestrates everything—connects view events to model operations, handles business logic

**Entry Point Flow:**
```
src/main.py → IntegratedController → LoginView → MainView (after authentication)
```

---

## 🎨 Theme System (`utils/theme_unison.py`)

All UI components **MUST** use UNISON institutional colors and custom widget creators to maintain brand consistency.

### Color Palette

```python
from theme_unison import (
    COLOR_AZUL_UNISON,      # #00529e (primary blue - official UNISON color)
    COLOR_DORADO_UNISON,    # #f8bb00 (gold accent - official UNISON color)
    COLOR_FONDO_BLANCO,     # #f5f5f5 (light background)
    BORDE_REDONDEADO,       # 8px (global border radius for consistency)
    crear_boton_redondeado_canvas,  # Buttons with real rounded corners
    crear_entry_redondeado          # Entry fields with rounded borders
)
```

### Widget Creation Patterns

**⚠️ Critical**: Standard `tk.Button` and `tk.Entry` do **NOT** support rounded corners. Always use custom creators.

#### Button Pattern

```python
# Canvas-based button returns a Frame container
btn = crear_boton_redondeado_canvas(
    parent, 
    texto="Click Me",
    comando=self.my_method,
    width=220, 
    height=50,
    corner_radius=BORDE_REDONDEADO,
    estilo="primario"  # Options: "primario" (blue), "dorado" (gold), "custom"
)

# To configure command later (useful for controller binding):
btn.config(command=new_command)
```

**Available Button Styles:**
- `"primario"`: Blue background (`COLOR_AZUL_UNISON`)
- `"dorado"`: Gold background (`COLOR_DORADO_UNISON`)
- `"custom"`: Use `bg_custom` and `hover_custom` parameters

#### Entry Pattern

```python
# Returns Frame with .entry attribute
container = crear_entry_redondeado(
    parent, 
    width=380, 
    height=45, 
    corner_radius=BORDE_REDONDEADO
)

# Access the actual Entry widget
self.my_entry = container.entry

# Standard Entry operations
value = self.my_entry.get()
self.my_entry.delete(0, 'end')
self.my_entry.insert(0, "New value")
```

---

## 🗄️ Database Operations

### Connection Details

- **Database**: SQLite at `database/InventarioBD_2.db`
- **Auto-creation**: Tables are auto-created via `model.create_tables_if_not_exist()` on startup
- **Connection Management**: Model handles connection lifecycle

### Database Schema

#### Table: `productos`
```sql
CREATE TABLE productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    precio REAL NOT NULL,
    cantidad INTEGER NOT NULL,
    departamento TEXT NOT NULL,
    almacen TEXT NOT NULL  -- FK to almacenes.id (stored as TEXT, validate manually)
);
```

#### Table: `almacenes`
```sql
CREATE TABLE almacenes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL UNIQUE
);
```

#### Table: `usuarios`
```sql
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,  -- SHA-256 hashed
    rol TEXT NOT NULL,       -- 'ADMIN', 'PRODUCTOS', or 'ALMACEN'
    ultimo_login TIMESTAMP
);
```

#### Table: `auditoria`
```sql
CREATE TABLE auditoria (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tabla TEXT NOT NULL,           -- 'productos' or 'almacenes'
    operacion TEXT NOT NULL,       -- 'INSERT', 'UPDATE', 'DELETE'
    registro_id INTEGER,           -- ID of affected record
    usuario TEXT,                  -- Username who performed action
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    detalles TEXT                  -- Additional context
);
```

### Model Methods (DatabaseModel class)

**Product Operations:**
```python
get_all_productos()                                      # Returns list of tuples
agregar_producto(nombre, precio, cantidad, 
                departamento, almacen_id, usuario=None)  # Logs to audit
actualizar_producto(producto_id, nombre, precio, 
                   cantidad, departamento, almacen_id, 
                   usuario=None)                         # Logs to audit
eliminar_producto(producto_id)                           # Logs to audit
producto_existe(producto_id)                             # Returns bool
```

**Warehouse Operations:**
```python
get_all_almacenes()                      # Returns list of tuples
agregar_almacen(nombre, usuario=None)    # Logs to audit
actualizar_almacen(almacen_id, nombre, 
                  usuario=None)          # Logs to audit
eliminar_almacen(almacen_id)             # Logs to audit
almacen_existe(almacen_id)               # Returns bool
almacen_existe_por_id(almacen_id)        # Returns bool
get_almacenes_nombres()                  # Returns list of names
get_almacenes_ids()                      # Returns list of IDs
```

**User Operations:**
```python
validar_usuario(nombre_usuario, password)  # Returns (bool, rol) tuple
actualizar_ultimo_login(usuario_id)        # Updates timestamp
obtener_usuarios()                         # Returns all users (no passwords)
```

**Error Handling:**
Always wrap DB calls in try/except and return empty lists on error—views expect iterables, never `None`.

---

## 🔐 Role-Based Access Control (RBAC)

### User Roles and Permissions

| Role | Productos Access | Almacenes Access | Description |
|------|-----------------|------------------|-------------|
| **ADMIN** | ✅ Full (Add/Edit/Delete) | ✅ Full (Add/Edit/Delete) | Complete system access |
| **PRODUCTOS** | ✅ Full (Add/Edit/Delete) | 👁️ Read-only | Manages products only |
| **ALMACEN** | 👁️ Read-only | ✅ Full (Add/Edit/Delete) | Manages warehouses only |

### Permission Verification Methods

```python
# In IntegratedController
def tiene_permiso_productos(self):
    """Verifica si el usuario tiene permiso para modificar productos"""
    return self.current_user_role in ['ADMIN', 'PRODUCTOS']

def tiene_permiso_almacenes(self):
    """Verifica si el usuario tiene permiso para modificar almacenes"""
    return self.current_user_role in ['ADMIN', 'ALMACEN']
```

### UI Permission Enforcement

The `aplicar_permisos_interfaz()` method dynamically adjusts the UI based on user role:

```python
def aplicar_permisos_interfaz(self):
    """Aplica los permisos de interfaz según el rol del usuario"""
    # For users WITHOUT permission:
    # - Entry fields are disabled (state='disabled')
    # - Add/Delete buttons are hidden (grid_remove())
    
    # For users WITH permission:
    # - Entry fields are enabled (state='normal')
    # - Add/Delete buttons are visible (grid())
```

**Behavior:**
- **No Permission**: Fields disabled (grayed out), buttons hidden
- **Has Permission**: Fields enabled, buttons visible and functional

### Backend Permission Validation

All CRUD methods verify permissions **before** executing:

```python
def agregar_producto(self):
    # Verify permissions BEFORE processing
    if not self.tiene_permiso_productos():
        messagebox.showerror(
            "Acceso Denegado", 
            f"Su rol ({self.current_user_role}) no tiene permiso para modificar productos."
        )
        return
    # ... rest of the code
```

**Protected Methods:**
- `agregar_producto()` - Requires ADMIN or PRODUCTOS role
- `eliminar_producto()` - Requires ADMIN or PRODUCTOS role
- `agregar_almacen()` - Requires ADMIN or ALMACEN role
- `eliminar_almacen()` - Requires ADMIN or ALMACEN role

### Permission Reapplication on Navigation

Permissions are reapplied every time the user changes views:

```python
def show_productos_frame(self):
    self.main_view.show_frame("productos")
    self.load_productos_data()
    self.aplicar_permisos_interfaz()  # ← Reapply permissions

def show_almacenes_frame(self):
    self.main_view.show_frame("almacenes")
    self.load_almacenes_data()
    self.aplicar_permisos_interfaz()  # ← Reapply permissions
```

---

## 📊 View Update Pattern

**Controller-driven data flow**: Controller loads data from model and pushes to view—views **never** pull data directly.

```python
# In controller:
def show_productos_frame(self):
    self.main_view.show_frame("productos")  # Switch UI
    self.load_productos_data()              # Fetch and populate
    self.aplicar_permisos_interfaz()        # Apply role permissions

def load_productos_data(self):
    productos = self.model.get_all_productos()        # Model call
    self.main_view.update_productos_tree(productos)   # View update
```

Views provide `update_*_tree()` methods that clear and repopulate `ttk.Treeview` widgets.

---

## 🧭 Navigation & Event Binding

### Frame Switching

```python
# Uses tkraise() to bring frames to front
main_view.show_frame("inicio")      # Home screen
main_view.show_frame("productos")   # Products view
main_view.show_frame("almacenes")   # Warehouses view
```

### Button Command Binding

Canvas buttons store commands at creation. For dynamically assigned commands (e.g., from controller):

```python
# In view creation:
self.btn_cerrar_sesion = crear_boton_redondeado_canvas(
    parent, 
    texto="CERRAR SESIÓN", 
    comando=None,  # Initially None
    ...
)

# In controller setup:
self.main_view.btn_cerrar_sesion.config(command=self.logout)
```

---

## ✅ Validation Rules

### Product Validation (`validar_producto()` in controller)

- **Required Fields**: All fields except ID (auto-increment)
- **Numeric Validation**: 
  - `precio` must be numeric and ≥ 0
  - `cantidad` must be numeric integer and ≥ 0
- **Foreign Key**: `almacen` must exist in `almacenes` table (check with `model.almacen_existe()`)
- **Max Lengths**: 
  - `nombre`: 100 characters
  - `departamento`: 50 characters
- **Name Validation**: Only alphanumeric, spaces, hyphens allowed

### Warehouse Validation (`validar_almacen()` in controller)

- **Required**: `nombre` field is mandatory
- **Max Length**: 50 characters
- **Character Set**: Only alphanumeric, spaces, hyphens, underscores
- **Uniqueness**: Name must be unique (enforced by database)

### Error Display

Show validation errors via `messagebox.showerror()` with clear, user-friendly messages.

---

## 🛠️ Development Commands

```bash
# Run app (from project root)
python src/main.py

# With virtual environment (Windows)
venv\Scripts\activate && python src/main.py

# Alternative: Use batch scripts
run_with_venv.bat      # Activates venv and runs app
ejecutar_app.bat       # Direct execution

# Populate test data
python database/populate_db.py

# Setup environment
setup.bat              # Windows setup script
setup.sh               # Linux/Mac setup script
```

---

## ⚠️ Common Patterns to Avoid

| ❌ Anti-Pattern | ✅ Correct Approach | Reason |
|----------------|-------------------|---------|
| Creating `Toplevel` windows | Use frame switching with `tkraise()` | Breaks single-window design |
| Importing `tkinter` in models | Keep models pure data layer | Violates MVC separation |
| Importing `sqlite3` in views | Views only display data | Violates MVC separation |
| Using `tk.Button`/`tk.Entry` | Use `crear_boton_redondeado_canvas()` and `crear_entry_redondeado()` | No rounded corners support |
| Modifying `self.root` children directly | Always work through `main_container` | Breaks frame management |
| Forgetting `canvas.create_window()` | Always call after creating Entry in Canvas | Entry won't be visible |
| Hardcoding colors | Use theme constants from `theme_unison.py` | Breaks brand consistency |
| Skipping permission checks | Always verify with `tiene_permiso_*()` | Security vulnerability |

---

## 📁 Key Files Reference

### Controllers
- **`src/controllers/integrated_controller_simple.py`** (582 lines)
  - Main orchestrator for entire application
  - Login handling and session management
  - CRUD logic for products and warehouses
  - RBAC permission enforcement
  - Data validation and error handling

### Models
- **`src/models/database.py`** (408 lines)
  - All SQLite operations
  - User authentication with SHA-256 hashing
  - Audit logging for all modifications
  - Connection lifecycle management

### Views
- **`src/views/login_view_split.py`**
  - Split-screen login (form left, branding right)
  - UNISON institutional branding
  - Password masking and validation

- **`src/views/main_view.py`** (595 lines)
  - Three main frames: inicio, productos, almacenes
  - Treeview tables for data display
  - Forms with UNISON-themed widgets
  - Navigation buttons

### Utils
- **`src/utils/theme_unison.py`** (448 lines)
  - Theme constants and color palette
  - Rounded widget creators (buttons, entries)
  - Treeview styling
  - Hover effects and focus states

### Database
- **`database/InventarioBD_2.db`**
  - SQLite database file
  - Auto-created with schema on first run

- **`database/populate_db.py`**
  - Test data population script
  - Creates sample users, products, warehouses

---

## 🎓 Student Project Context

**Author**: Manuel Munguia Rubio  
**Institution**: Universidad de Sonora  
**Program**: Ingeniería en Sistemas de Información  
**Course**: Bases de Datos 1

**Project Scope**: Demonstrates professional MVC architecture, SQLite integration, role-based access control, and audit logging. This is a **complete, production-ready application**, not a prototype or placeholder.

**Key Learning Objectives**:
- MVC architectural pattern implementation
- Database design and normalization
- CRUD operations with SQLite
- User authentication and authorization
- Audit trail implementation
- Desktop GUI development with Tkinter
- Professional code organization and documentation

---

## 🔒 Security Considerations

1. **Password Hashing**: All passwords stored as SHA-256 hashes
2. **Two-Layer Security**: 
   - UI layer (disabled fields, hidden buttons)
   - Backend layer (permission verification in methods)
3. **Audit Trail**: All modifications logged with user, timestamp, and details
4. **Session Management**: Current user role tracked throughout session
5. **Input Validation**: All user inputs validated before database operations

---

## 📝 Code Style Guidelines

### Naming Conventions
- **Classes**: PascalCase (e.g., `DatabaseModel`, `IntegratedController`)
- **Functions/Methods**: snake_case (e.g., `agregar_producto`, `tiene_permiso_almacenes`)
- **Constants**: UPPER_SNAKE_CASE (e.g., `COLOR_AZUL_UNISON`, `BORDE_REDONDEADO`)
- **Variables**: snake_case (e.g., `current_user_role`, `producto_id`)

### Documentation
- Use Spanish for user-facing strings and comments (project language)
- Include docstrings for all public methods
- Comment complex business logic

### Error Handling
```python
try:
    # Database operation
    result = self.model.some_operation()
except Exception as e:
    print(f"Error: {e}")
    messagebox.showerror("Error", "Descripción del error para el usuario")
    return []  # Return empty list, never None
```

---

## 🧪 Testing Recommendations

### Manual Testing Scenarios

**Test 1: Role-Based Access**
```
1. Login as 'Admin' (ADMIN role) → Should have full access
2. Login as 'productos' (PRODUCTOS role) → Can edit products, view-only almacenes
3. Login as 'almacen' (ALMACEN role) → Can edit almacenes, view-only products
```

**Test 2: Permission Enforcement**
```
1. Login with restricted role
2. Navigate to restricted section
3. Verify fields are disabled and buttons hidden
4. Attempt to bypass UI (should show error message)
```

**Test 3: Data Validation**
```
1. Try adding product with negative price → Should reject
2. Try adding product with non-existent warehouse → Should reject
3. Try adding warehouse with special characters → Should reject
```

**Test 4: Audit Trail**
```
1. Perform CRUD operations
2. Check auditoria table for logged entries
3. Verify username and timestamp are recorded
```

---

## 🔄 Future Enhancement Guidelines

### Adding New Permissions
1. Create method `tiene_permiso_XXX()` in controller
2. Add validation in `aplicar_permisos_interfaz()`
3. Add verification in corresponding CRUD methods
4. Update this documentation

### Adding New Tables
1. Add CREATE TABLE statement in `create_tables_if_not_exist()`
2. Create getter/setter methods in `DatabaseModel`
3. Create corresponding view in `main_view.py`
4. Add controller methods for CRUD operations
5. Add validation method in controller
6. Update audit logging if needed

### Adding New Roles
1. Add role to `usuarios` table
2. Update permission methods in controller
3. Update `aplicar_permisos_interfaz()` logic
4. Document role permissions in this file

---

## 📚 Additional Resources

- **SQLite Documentation**: https://www.sqlite.org/docs.html
- **Tkinter Documentation**: https://docs.python.org/3/library/tkinter.html
- **MVC Pattern**: https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller
- **RBAC Concepts**: https://en.wikipedia.org/wiki/Role-based_access_control

---

**Last Updated**: 2025-11-22  
**Version**: 2.0 (with RBAC and Audit Logging)
