# Copilot Instructions - Sistema de Inventario UNISON

## Project Overview
Desktop inventory management system for Universidad de Sonora built with Python/Tkinter and SQLite. Features role-based access control, custom UNISON-branded UI theme, and split-screen login interface.

## Architecture

### MVC Pattern
- **Models** (`models/database.py`): SQLite operations via `DatabaseModel` class - handles products, warehouses (almacenes), and user authentication with SHA256 password hashing
- **Views** (`views/`): Tkinter UI components - `LoginViewUnisonSplit` (split login screen), `MainView` (tabbed interface with productos/almacenes/inicio frames)
- **Controllers** (`controllers/integrated_controller_simple.py`): Single `IntegratedController` manages entire app lifecycle, role permissions, and view transitions

### State Management
- `IntegratedController` maintains app state with `current_state` ("login"|"main"), `current_user`, and `current_user_role`
- View switching via `main_container` frame replacement pattern - destroys children and recreates views to prevent memory leaks
- Permission system checks `current_user_role` against ['ADMIN', 'PRODUCTOS', 'ALMACEN'] to show/hide UI elements using `.grid()/.grid_remove()` and `.pack()/.pack_forget()`

### Database Schema
- **productos**: id, nombre, precio, cantidad, departamento, almacen (TEXT storing ID), fecha_ultima_modificacion, ultimo_usuario_modificacion
- **almacenes**: id, nombre, fecha_ultima_modificacion, ultimo_usuario_modificacion  
- **usuarios**: id, nombre, contraseña (SHA256), rol, ultimo_inicio_sesion
- Default users: Admin/admin23, almacen/almacen11, productos/producto19

## Critical Conventions

### UNISON Theme System (`utils/theme_unison.py`)
All UI uses official Universidad de Sonora colors: `COLOR_AZUL_UNISON` (#00529e), `COLOR_DORADO_UNISON` (#f8bb00). Custom widgets:
- `crear_boton_redondeado_canvas()` - Canvas-based rounded buttons (8px radius) with hover effects
- `crear_entry_redondeado()` - Canvas-wrapped Entry widgets with focus animations
- Returns container Frame with `.entry` attribute for actual Entry widget access

**IMPORTANT**: Always use `.entry` attribute when accessing Entry values from rounded components:
```python
entry_container = crear_entry_redondeado(parent)
value = entry_container.entry.get()  # NOT entry_container.get()
```

### Permission Pattern
Controller methods check permissions before operations:
```python
def tiene_permiso_productos(self):
    return self.current_user_role in ['ADMIN', 'PRODUCTOS']

def agregar_producto(self):
    if not self.tiene_permiso_productos():
        messagebox.showerror("Acceso Denegado", ...)
        return
```

Apply UI permissions in `aplicar_permisos_interfaz()` after frame switches - uses both `grid_remove()` for Grid-managed widgets and `pack_forget()` for Pack-managed widgets.

### Controller Command Binding
Views create UI elements but don't bind commands. Controller binds in `setup_main_view_commands()`:
```python
self.main_view.btn_agregar_producto.config(command=self.agregar_producto)
```

For Canvas-based buttons, custom `.config()` method rebinds `<Button-1>` event.

### Almacén ID Handling
Products store warehouse ID as TEXT but accept name or ID. Controller's `convertir_almacen_a_id()` normalizes input before validation. Always validate with `almacen_existe()` before insert/update.

### Auto-ID Generation
`autocompletar_id_producto()` pre-fills next available ID by finding `max(existing_ids) + 1` when switching to products frame.

## Development Workflows

### Running Application
- **Quick**: `python src\main.py` (uses existing venv if activated)
- **With venv**: `setup.bat` then `run_with_venv.bat`
- **Manual**: `venv\Scripts\activate` → `python src\main.py`

Database initializes automatically at `database/InventarioBD_2.db` with default users/tables via `create_tables_if_not_exist()`.

### Adding New Features
1. **New view frame**: Add to `MainView.create_frames()`, ensure Grid responsiveness with `.grid_rowconfigure()`/`.grid_columnconfigure()` 
2. **Database operations**: Extend `DatabaseModel` with transaction-safe methods using `cursor.execute()` + `connection.commit()`
3. **Permissions**: Add role check method in controller, apply in `aplicar_permisos_interfaz()`, gate operations in action methods

### Debugging Database
Connection auto-establishes at `DatabaseModel.__init__()`. Check `database/InventarioBD_2.db` directly with SQLite tools. Print statements log operations (e.g., "Producto agregado exitosamente por {usuario}").

## Key Files Reference
- **Entry point**: `src/main.py` - Creates Tk root and IntegratedController
- **Theme constants**: `utils/theme_unison.py` - All colors, widget factories  
- **Login flow**: `views/login_view_split.py` → `controllers/integrated_controller_simple.py:handle_login()` → `show_main_application()`
- **Form validation**: Controller methods `validar_producto()`, `validar_almacen()` with regex/type checks

## Common Patterns
- **Treeview sorting**: Click headers trigger `ordenar_productos()`/`ordenar_almacenes()` - sorts cached data, toggles asc/desc indicators
- **Form population**: Treeview selection binds to `on_producto_select()`/`on_almacen_select()` which fills entry fields
- **Dual mode operations**: Check `producto_existe(id)` - if True, UPDATE; else INSERT
- **Window cleanup**: Override `WM_DELETE_WINDOW` protocol to call `model.disconnect()` before `destroy()`
