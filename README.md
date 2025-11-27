# ðŸŽ“ Sistema de Inventario - Universidad de Sonora

Sistema de gestiÃ³n de inventario desarrollado con **Python/Tkinter** y **SQLite** para la Universidad de Sonora. Incluye autenticaciÃ³n por roles, interfaz grÃ¡fica moderna con tema UNISON, y gestiÃ³n completa de productos y almacenes.

---

## ðŸ“‹ Requisitos del Sistema

- **Python 3.7 o superior** (desarrollado y probado con Python 3.13.7)
- **Sistema Operativo:** Windows, Linux o macOS
- **Espacio en disco:** ~50 MB (incluye dependencias)
- **Dependencias externas:**
  - `Pillow>=9.0.0` - Manejo de imÃ¡genes
  - `tkcalendar>=1.6.0` - Selectores de fecha

---

## âš¡ Inicio RÃ¡pido (Para Nuevos Usuarios)

### OpciÃ³n A: InstalaciÃ³n AutomÃ¡tica (Recomendado)

Si eres nuevo en el proyecto, sigue estos pasos:

#### **1. Clonar el Repositorio**
```bash
git clone https://github.com/DaManu123/Proyecto-BD1.git
cd Proyecto-BD1/databases-inventory-app
```

#### **2. Crear Entorno Virtual**
**Windows:**
```powershell
python -m venv .venv
```

**Linux/Mac:**
```bash
python3 -m venv .venv
```

#### **3. Activar Entorno Virtual**
**Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
.venv\Scripts\activate.bat
```

**Linux/Mac:**
```bash
source .venv/bin/activate
```

#### **4. Instalar Dependencias**
```bash
pip install -r requirements.txt
```

#### **5. Ejecutar la AplicaciÃ³n**
```bash
python src/main.py
```

### OpciÃ³n B: EjecuciÃ³n con VS Code

Si usas **Visual Studio Code**:

1. **Abrir el proyecto:**
   - Abre VS Code
   - `Archivo > Abrir Carpeta` â†’ Selecciona `databases-inventory-app`

2. **Seleccionar intÃ©rprete Python:**
   - Presiona `Ctrl+Shift+P`
   - Escribe: `Python: Select Interpreter`
   - Selecciona: `.venv/Scripts/python.exe` (Windows) o `.venv/bin/python` (Linux/Mac)

3. **Ejecutar:**
   - Abre `src/main.py`
   - Presiona `F5` o haz clic en el botÃ³n **â–¶ï¸ Run**

---

## ðŸ“ Estructura del Proyecto

```
databases-inventory-app/
â”‚
â”œâ”€â”€ src/                        # CÃ³digo fuente
â”‚   â”œâ”€â”€ main.py                # ðŸš€ Punto de entrada de la aplicaciÃ³n
â”‚   â”œâ”€â”€ controllers/           # LÃ³gica de negocio
â”‚   â”‚   â””â”€â”€ integrated_controller_simple.py
â”‚   â”œâ”€â”€ models/                # Modelos de datos y BD
â”‚   â”‚   â””â”€â”€ database.py
â”‚   â”œâ”€â”€ views/                 # Interfaces de usuario
â”‚   â”‚   â”œâ”€â”€ login_view_split.py
â”‚   â”‚   â””â”€â”€ main_view.py
â”‚   â””â”€â”€ utils/                 # Utilidades y configuraciÃ³n
â”‚       â”œâ”€â”€ config.py
â”‚       â””â”€â”€ theme_unison.py    # Tema personalizado UNISON
â”‚
â”œâ”€â”€ database/                  # Base de datos SQLite
â”‚   â””â”€â”€ InventarioBD_2.db     # Se crea automÃ¡ticamente
â”‚
â”œâ”€â”€ .vscode/                   # ConfiguraciÃ³n de VS Code
â”‚   â””â”€â”€ settings.json         # IntÃ©rprete y Code Runner configurados
â”‚
â”œâ”€â”€ requirements.txt          # ðŸ“¦ Dependencias del proyecto
â”œâ”€â”€ README.md                 # ðŸ“– Este archivo
â”œâ”€â”€ TROUBLESHOOTING.md        # ðŸ”§ GuÃ­a de soluciÃ³n de problemas
â”œâ”€â”€ verificar_entorno.bat     # ðŸ› ï¸ Script de diagnÃ³stico (Windows)
â””â”€â”€ unilogo.gif              # Logo de la Universidad de Sonora
```

---

## ðŸŽ® Formas de Ejecutar el Programa

### MÃ©todo 1: Terminal (Todas las plataformas)

**Con entorno virtual activado:**
```bash
# 1. Activar entorno virtual
# Windows PowerShell:
.venv\Scripts\Activate.ps1

# Windows CMD:
.venv\Scripts\activate.bat

# Linux/Mac:
source .venv/bin/activate

# 2. Ejecutar
python src/main.py
```

### MÃ©todo 2: VS Code (Recomendado)

**Ejecutar con el botÃ³n Run (â–¶ï¸):**
- Abre `src/main.py`
- Presiona `Ctrl+Alt+N` o clic en **â–¶ï¸ Run Code**
- El programa usa automÃ¡ticamente el entorno virtual configurado

**Ejecutar con Debugger (F5):**
- Abre `src/main.py`
- Presiona `F5`
- Se ejecuta en modo depuraciÃ³n con puntos de interrupciÃ³n

### MÃ©todo 3: Script de DiagnÃ³stico (Solo Windows)

Para verificar que todo estÃ© configurado correctamente:
```cmd
verificar_entorno.bat
```

Este script comprueba:
- âœ… Existencia del entorno virtual
- âœ… VersiÃ³n de Python
- âœ… Paquetes instalados
- âœ… ImportaciÃ³n de mÃ³dulos requeridos

---

## ðŸ”‘ Credenciales de Acceso

La aplicaciÃ³n incluye **3 usuarios predeterminados** con diferentes niveles de acceso:

| Usuario | ContraseÃ±a | Rol | Permisos |
|---------|------------|-----|----------|
| **Admin** | admin23 | ADMIN | Acceso completo (productos + almacenes + usuarios) |
| **productos** | producto19 | PRODUCTOS | GestiÃ³n de productos Ãºnicamente |
| **almacen** | almacen11 | ALMACEN | GestiÃ³n de almacenes Ãºnicamente |

**Nota:** Las contraseÃ±as se almacenan con hash SHA256 en la base de datos.

---

## ðŸŽ¨ CaracterÃ­sticas Principales

### Sistema de AutenticaciÃ³n
- âœ… Login con pantalla dividida personalizada
- âœ… ValidaciÃ³n de credenciales con hash SHA256
- âœ… Control de acceso basado en roles (RBAC)
- âœ… Registro de Ãºltimo inicio de sesiÃ³n

### GestiÃ³n de Productos
- âœ… CRUD completo (Crear, Leer, Actualizar, Eliminar)
- âœ… Filtros avanzados por:
  - Nombre del producto
  - Rango de precios
  - Rango de cantidades
  - Fechas de modificaciÃ³n
  - Usuario que realizÃ³ cambios
- âœ… Ordenamiento por columnas (clic en encabezados)
- âœ… Auto-generaciÃ³n de IDs
- âœ… ValidaciÃ³n de datos en tiempo real

### GestiÃ³n de Almacenes
- âœ… AdministraciÃ³n de bodegas/almacenes
- âœ… RelaciÃ³n con productos
- âœ… Filtros por nombre y fechas
- âœ… AuditorÃ­a de cambios

### Interfaz de Usuario
- âœ… Tema personalizado con **colores oficiales UNISON**:
  - Azul UNISON: `#00529e`
  - Dorado UNISON: `#f8bb00`
- âœ… Botones redondeados con efectos hover
- âœ… Campos de entrada con bordes suavizados
- âœ… Selector de fechas con calendario visual
- âœ… Panel de filtros colapsable/expandible
- âœ… DiseÃ±o responsivo

---

## ðŸ”§ SoluciÃ³n de Problemas Comunes

### âŒ Error: `ModuleNotFoundError: No module named 'tkcalendar'`

**Causa:** El intÃ©rprete de Python no encuentra el mÃ³dulo porque no estÃ¡ usando el entorno virtual.

**SoluciÃ³n:**

1. **Verificar que el entorno virtual estÃ© activado:**
   ```bash
   # DeberÃ­as ver (.venv) al inicio del prompt
   (.venv) PS C:\...\databases-inventory-app>
   ```

2. **Reinstalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **En VS Code - Seleccionar intÃ©rprete correcto:**
   - Presiona `Ctrl+Shift+P`
   - Escribe: `Python: Select Interpreter`
   - Selecciona: `.venv\Scripts\python.exe` âœ“

4. **Verificar instalaciÃ³n:**
   ```bash
   python -c "import tkcalendar; print('OK:', tkcalendar.__version__)"
   # Debe mostrar: OK: 1.5.0 (o superior)
   ```

### âŒ Error: `tkinter.TclError` o interfaz no se muestra

**Causa:** `tkinter` no estÃ¡ instalado correctamente.

**SoluciÃ³n:**

- **Windows/Mac:** `tkinter` viene incluido con Python
- **Linux (Ubuntu/Debian):**
  ```bash
  sudo apt-get install python3-tk
  ```
- **Linux (Fedora):**
  ```bash
  sudo dnf install python3-tkinter
  ```

### âŒ La base de datos no se crea

**Causa:** Permisos insuficientes en la carpeta `database/`.

**SoluciÃ³n:**
```bash
# Crear carpeta manualmente
mkdir database

# En Linux/Mac, dar permisos
chmod 755 database
```

### ðŸ› ï¸ Script de DiagnÃ³stico AutomÃ¡tico

**Windows:** Ejecuta `verificar_entorno.bat` para un diagnÃ³stico completo del entorno.

**Resultado esperado:**
```
[OK] Entorno virtual encontrado
[OK] tkcalendar version: 1.5.0
[OK] Pillow version: 12.0.0
[OK] tkinter disponible
[OK] sqlite3 version: 3.x.x
```

ðŸ“– **MÃ¡s ayuda:** Consulta `TROUBLESHOOTING.md` para soluciones detalladas.

---

## ðŸ“Š Base de Datos

### InformaciÃ³n General
- **Motor:** SQLite 3
- **UbicaciÃ³n:** `database/InventarioBD_2.db`
- **CreaciÃ³n:** AutomÃ¡tica al iniciar la aplicaciÃ³n por primera vez
- **TamaÃ±o inicial:** ~20 KB

### Esquema de Tablas

**Tabla `productos`:**
- `id` (TEXT) - Identificador Ãºnico
- `nombre` (TEXT) - Nombre del producto
- `precio` (REAL) - Precio unitario
- `cantidad` (INTEGER) - Cantidad en stock
- `departamento` (TEXT) - Departamento/categorÃ­a
- `almacen` (TEXT) - ID del almacÃ©n asociado
- `fecha_ultima_modificacion` (TEXT) - Timestamp
- `ultimo_usuario_modificacion` (TEXT) - Usuario que modificÃ³

**Tabla `almacenes`:**
- `id` (TEXT) - Identificador Ãºnico
- `nombre` (TEXT) - Nombre del almacÃ©n
- `fecha_ultima_modificacion` (TEXT)
- `ultimo_usuario_modificacion` (TEXT)

**Tabla `usuarios`:**
- `id` (INTEGER) - ID autoincremental
- `nombre` (TEXT) - Nombre de usuario
- `contraseÃ±a` (TEXT) - Hash SHA256
- `rol` (TEXT) - ADMIN, PRODUCTOS o ALMACEN
- `ultimo_inicio_sesion` (TEXT)

### Respaldo y RestauraciÃ³n

**Crear respaldo:**
```bash
# La base de datos es un archivo Ãºnico
cp database/InventarioBD_2.db database/backup_$(date +%Y%m%d).db
```

**Restaurar respaldo:**
```bash
cp database/backup_YYYYMMDD.db database/InventarioBD_2.db
```

---

## ðŸ—ï¸ Arquitectura del Proyecto

### PatrÃ³n MVC (Modelo-Vista-Controlador)

```
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚   VIEWS     â”‚ â† Interfaz grÃ¡fica (Tkinter)
â”‚  (Vista)    â”‚
â””â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”˜
       â”‚
â”Œâ”€â”€â”€â”€â”€â”€â–¼â”€â”€â”€â”€â”€â”€â”
â”‚ CONTROLLERS â”‚ â† LÃ³gica de negocio y validaciÃ³n
â”‚ (Controladorâ”‚
â””â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”˜
       â”‚
â”Œâ”€â”€â”€â”€â”€â”€â–¼â”€â”€â”€â”€â”€â”€â”
â”‚   MODELS    â”‚ â† Acceso a datos (SQLite)
â”‚  (Modelo)   â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

**Ventajas:**
- âœ… SeparaciÃ³n de responsabilidades
- âœ… CÃ³digo mantenible y escalable
- âœ… FÃ¡cil testeo de componentes
- âœ… ReutilizaciÃ³n de cÃ³digo

---

## ðŸ‘¤ Autor

**Manuel Munguia Rubio**  
IngenierÃ­a en Sistemas de InformaciÃ³n  
Universidad de Sonora

## ðŸ“ Notas Adicionales

- El proyecto utiliza la arquitectura MVC (Modelo-Vista-Controlador)
- Los colores del tema siguen la identidad corporativa de la Universidad de Sonora
- La base de datos incluye triggers y auditorÃ­a automÃ¡tica de cambios
- Todos los campos de formulario tienen validaciÃ³n en tiempo real

## ðŸ†˜ Soporte

Si encuentras problemas:
1. Verifica que el entorno virtual estÃ© activado
2. Confirma que todas las dependencias estÃ©n instaladas: `pip list`
3. Revisa la configuraciÃ³n de VS Code en `.vscode/settings.json`
4. Verifica la versiÃ³n de Python: `python --version` (debe ser 3.7+)

