# Sistema de Inventario UNISON - AI Coding Instructions

Educational desktop app for Database 1 course at Universidad de Sonora. Python + Tkinter with strict MVC architecture and UNISON institutional branding.

## Architecture Overview

**Single-Window Pattern with Frame Switching**: App uses ONE root window with a persistent `main_container` Frame. Views are swapped by destroying container children and creating new views inside it—NEVER destroy the root or create Toplevel windows. This prevents flickering during transitions.

```python
# ✅ Correct: Smooth transitions
for widget in self.main_container.winfo_children():
    widget.destroy()
self.main_view = MainView(self.main_container)

# ❌ Wrong: Causes flicker
self.root.destroy()
new_root = Tk()
```

**MVC Boundaries (Strictly Enforced)**:
- `models/database.py`: SQLite operations only—NO tkinter imports
- `views/`: UI widgets only—NO sqlite3 imports, NO business logic
- `controllers/integrated_controller_simple.py`: Orchestrates everything—connects view events to model operations

Entry point: `src/main.py` → `IntegratedController` → shows login → shows main app.

## Theme System (`utils/theme_unison.py`)

All UI components MUST use UNISON institutional colors and custom widget creators:

```python
from theme_unison import (
    COLOR_AZUL_UNISON,      # #00529e (primary blue)
    COLOR_DORADO_UNISON,    # #f8bb00 (gold accent)
    BORDE_REDONDEADO,       # 8px (global border radius)
    crear_boton_redondeado_canvas,  # Buttons with real rounded corners
    crear_entry_redondeado          # Entry fields with rounded borders
)
```

**Critical**: Standard `tk.Button` and `tk.Entry` do NOT support rounded corners. Use `crear_boton_redondeado_canvas()` for buttons and `crear_entry_redondeado()` for inputs—these use Canvas to simulate 8px rounded borders.

**Button Pattern**:
```python
# Canvas-based button returns a Frame container
btn = crear_boton_redondeado_canvas(
    parent, 
    texto="Click Me",
    comando=self.my_method,
    width=220, height=50,
    corner_radius=BORDE_REDONDEADO,
    estilo="primario"  # or "dorado", "custom"
)
# To configure command later: btn.config(command=new_command)
```

**Entry Pattern**:
```python
# Returns Frame with .entry attribute
container = crear_entry_redondeado(parent, width=380, height=45, corner_radius=BORDE_REDONDEADO)
self.my_entry = container.entry  # Access actual Entry widget
# Then use: self.my_entry.get(), .delete(), .insert()
```

## Database Operations

**Connection**: SQLite at `database/InventarioBD_2.db`. Tables auto-created via `model.create_tables_if_not_exist()` on startup.

**Tables**:
- `productos`: id, nombre, precio, cantidad, departamento, almacen (FK to almacenes.id conceptually, but stored as TEXT—validate manually)
- `almacenes`: id, nombre
- `usuarios`: id, nombre (unique), password (SHA-256 hashed)

**Model Methods** (all in `DatabaseModel` class):
```python
get_all_productos()              # Returns list of tuples
agregar_producto(nombre, precio, cantidad, departamento, almacen_id)
eliminar_producto(producto_id)
validar_usuario(username, password)  # For login
```

Always wrap DB calls in try/except and return empty lists on error—views expect iterables.

## View Update Pattern

Controller loads data from model and pushes to view—views never pull data directly:

```python
# In controller:
def show_productos_frame(self):
    self.main_view.show_frame("productos")  # Switch UI
    self.load_productos_data()              # Fetch and populate

def load_productos_data(self):
    productos = self.model.get_all_productos()        # Model call
    self.main_view.update_productos_tree(productos)   # View update
```

Views provide `update_*_tree()` methods that clear and repopulate ttk.Treeview widgets.

## Navigation & Event Binding

**Frame Switching**: `main_view.show_frame("inicio"|"productos"|"almacenes")` uses `frame.tkraise()` to bring frames to front.

**Button Command Binding**: Canvas buttons store commands at creation. For dynamically assigned commands (e.g., from controller):
```python
# In view creation:
self.btn_cerrar_sesion = crear_boton_redondeado_canvas(parent, texto="CERRAR", comando=None, ...)

# In controller setup:
self.main_view.btn_cerrar_sesion.config(command=self.logout)
```

## Validation Rules

Product validation (`validar_producto()` in controller):
- All fields required except ID (auto-increment)
- Precio/Cantidad must be numeric ≥0
- Almacen must exist in `almacenes` table (check with `model.almacen_existe()`)
- Max lengths: nombre (100), departamento (50)

Almacen validation:
- Nombre required, max 50 chars
- Only alphanumeric, spaces, hyphens, underscores

Show validation errors via `messagebox.showerror()`.

## Development Commands

```bash
# Run app (from project root)
python src/main.py

# With venv (Windows)
venv\Scripts\activate && python src/main.py

# Populate test data
python database/populate_db.py
```

## Common Patterns to Avoid

❌ Creating `Toplevel` windows (breaks single-window design)  
❌ Importing tkinter in models or sqlite3 in views  
❌ Using `tk.Button`/`tk.Entry` for new UI (no rounded corners support)  
❌ Directly modifying `self.root` children (always work through `main_container`)  
❌ Forgetting to call `canvas.create_window()` after creating Entry in Canvas (Entry won't be visible)

## Key Files

- `src/controllers/integrated_controller_simple.py` (379 lines): Main orchestrator, login handling, CRUD logic
- `src/utils/theme_unison.py` (448 lines): Theme constants, rounded widget creators
- `src/views/login_view_split.py`: Split-screen login (form left, branding right)
- `src/views/main_view.py` (595 lines): Three frames (inicio, productos, almacenes) with Treeviews and forms
- `src/models/database.py`: All SQLite operations, user authentication

## Student Project Context

Built for DB1 course at UNISON by Manuel Munguia Rubio. Demonstrates MVC architecture and SQLite integration—functionality is complete (not just placeholders as originally scoped).
