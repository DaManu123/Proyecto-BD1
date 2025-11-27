# Sistema de Inventario - Universidad de Sonora

Sistema de gestion de inventario desarrollado con **Python/Tkinter** y **SQLite** para la Universidad de Sonora. Incluye autenticacion por roles, interfaz grafica moderna con tema UNISON, y gestion completa de productos y almacenes.

---

## Requisitos del Sistema

- **Python 3.7 o superior** (desarrollado y probado con Python 3.13.7)
- **Sistema Operativo:** Windows, Linux o macOS
- **Espacio en disco:** ~50 MB (incluye dependencias)
- **Dependencias externas:**
  - `Pillow>=9.0.0` - Manejo de imagenes
  - `tkcalendar>=1.6.0` - Selectores de fecha

---

## Inicio Rapido (Para Nuevos Usuarios)

### Instalacion y Configuracion Automatica

El proyecto incluye un **script maestro unificado** que maneja instalacion, ejecucion, verificacion y configuracion automatica de VS Code.

#### **Windows:**
```cmd
# 1. Clonar el repositorio
git clone https://github.com/DaManu123/Proyecto-BD1.git
cd Proyecto-BD1

# 2. Ejecutar setup.bat DESDE LA TERMINAL
setup.bat

# 3. Seleccionar Opcion 1: Instalacion Completa
# 4. Seleccionar Opcion 4: Configurar VS Code
```

**IMPORTANTE:** Ejecuta `setup.bat` desde la terminal de Windows (PowerShell o CMD), NO hagas doble clic.

#### **Linux/macOS:**
```bash
# 1. Clonar el repositorio
git clone https://github.com/DaManu123/Proyecto-BD1.git
cd Proyecto-BD1

# 2. Dar permisos de ejecucion
chmod +x setup.sh

# 3. Ejecutar script maestro
./setup.sh

# 4. Seleccionar opciones 1 y 4
```

### Menu del Script Maestro

Al ejecutar `setup.bat` (Windows) o `./setup.sh` (Linux/macOS), obtendras un menu interactivo:

```
====================================================
  SISTEMA DE INVENTARIO - UNISON
  Configuracion y Administracion
====================================================

  MENU PRINCIPAL:

  1) Instalacion Completa (Primera Vez)
  2) Ejecutar Aplicacion
  3) Verificar Entorno
  4) Configurar VS Code
  5) Salir

====================================================
```

**PASOS REQUERIDOS PARA PRIMER USO:**

1. **Opcion 1 - Instalacion Completa:**
   - Crea el entorno virtual `.venv`
   - Instala todas las dependencias Python
   - Verifica la instalacion correcta

2. **Opcion 4 - Configurar VS Code:**
   - Genera `.vscode/settings.json` con configuracion optimizada
   - Genera `.vscode/launch.json` para debugging
   - Configura Code Runner para ejecutar correctamente
   - Configura PYTHONPATH automaticamente

3. **Reiniciar VS Code:**
   - Presiona `Ctrl+Shift+P`
   - Escribe: `Developer: Reload Window`
   - Presiona Enter

**Otras opciones:**

**Opcion 2 - Ejecutar Aplicacion:**
- Inicia el programa directamente desde el script

**Opcion 3 - Verificar Entorno:**
- Muestra version de Python
- Lista paquetes instalados
- Verifica modulos requeridos

**Importante:** La configuracion es completamente portable y funciona en **cualquier PC** sin modificaciones manuales.

---

## Compilar a Ejecutable (.EXE)

El proyecto incluye scripts para generar un **ejecutable standalone** que no requiere Python instalado.

### Windows:

```cmd
# 1. Asegúrate de haber ejecutado setup.bat opción 1 primero
setup.bat

# 2. Ejecuta el script de compilación
build_exe.bat
```

### Linux/macOS:

```bash
# 1. Asegúrate de haber ejecutado setup.sh primero
./setup.sh

# 2. Dar permisos y ejecutar compilación
chmod +x build_exe.sh
./build_exe.sh
```

### Resultado de la Compilación:

El script genera una carpeta `Release/` que contiene:
- **SistemaInventario_UNISON.exe** (Windows) - Ejecutable principal (~50-80 MB)
- **database/** - Base de datos SQLite
- **unilogo.gif** - Logo de la universidad
- **LEEME.txt** - Instrucciones de uso

### Distribución:

Para distribuir el programa:
1. Comprime la carpeta `Release/` en un archivo ZIP
2. Envía el ZIP a otros usuarios
3. Los usuarios solo necesitan descomprimir y ejecutar el .exe

**Ventajas del ejecutable:**
- ✅ No requiere Python instalado
- ✅ No requiere instalar dependencias
- ✅ Ejecutable de un solo archivo (onefile)
- ✅ Incluye todos los recursos necesarios
- ✅ Compatible con Windows 7, 8, 10, 11

---

## Compatibilidad con IDEs

Este proyecto esta **preconfigurado automaticamente** para funcionar en cualquier IDE. El script `setup.bat`/`setup.sh` configura VS Code automaticamente con rutas portables.

### Visual Studio Code (Recomendado - Configurado Automaticamente)

#### Pasos de Configuracion

**IMPORTANTE:** Debes ejecutar estas opciones del `setup.bat` desde la terminal:

1. Ejecuta `setup.bat` desde PowerShell o CMD
2. Selecciona **Opcion 1: Instalacion Completa**
3. Selecciona **Opcion 4: Configurar VS Code**
4. Abre la carpeta del proyecto en VS Code
5. Reinicia VS Code: `Ctrl+Shift+P` → `Developer: Reload Window`

#### Configuraciones Generadas Automaticamente

El script genera dos archivos en `.vscode/`:

**settings.json:**
- Interprete Python: `.venv/Scripts/python.exe`
- PYTHONPATH automatico: `src/`
- Code Runner configurado correctamente
- Activacion automatica del entorno virtual

**launch.json:**
- **"Python: Main Application"** - Ejecuta `src/main.py` (F5)
- **"Python: Current File"** - Ejecuta archivo actual
- Debugging con breakpoints habilitado

#### Formas de Ejecutar en VS Code

1. **Code Runner (▶️)** - Boton en esquina superior derecha
   - Abre `src/main.py`
   - Click en el boton Run
   - Ejecuta usando el entorno virtual

2. **Run Python File** - Boton nativo de VS Code
   - Abre `src/main.py`
   - Click derecho > Run Python File in Terminal
   - O usa el boton de "play" en la esquina superior

3. **Debugger (F5)** - Para debugging
   - Presiona F5
   - Selecciona "Python: Main Application"
   - Permite usar breakpoints y depurar

4. **Terminal Integrado**
   ```powershell
   # El entorno virtual se activa automaticamente
   python src/main.py
   ```

**Nota:** Code Runner y Run Python File ahora usan la **misma configuracion**, ambos funcionan correctamente.

### PyCharm
1. Abre el proyecto
2. PyCharm detectara automaticamente el entorno virtual `.venv`
3. Click derecho en `src/main.py` > Run

---

## Estructura del Proyecto

```
databases-inventory-app/
|
├── src/                        # Codigo fuente
│   ├── main.py                # Punto de entrada de la aplicacion
│   ├── controllers/           # Logica de negocio
│   │   └── integrated_controller_simple.py
│   ├── models/                # Modelos de datos y BD
│   │   └── database.py
│   ├── views/                 # Interfaces de usuario
│   │   ├── login_view_split.py
│   │   └── main_view.py
│   └── utils/                 # Utilidades y configuracion
│       ├── config.py
│       └── theme_unison.py    # Tema personalizado UNISON
│
├── database/                  # Base de datos SQLite
│   └── InventarioBD_2.db     # Se crea automaticamente
│
├── .vscode/                   # Configuracion de VS Code (generada por setup)
│   ├── settings.json         # Configuracion portable automatica
│   └── launch.json           # Debugging y ejecucion
│
├── setup.bat                 # Script maestro Windows
├── setup.sh                  # Script maestro Linux/macOS
├── requirements.txt          # Dependencias del proyecto
├── README.md                 # Este archivo
└── unilogo.gif              # Logo de la Universidad de Sonora
```

---

## Credenciales de Acceso

La aplicacion incluye **3 usuarios predeterminados** con diferentes niveles de acceso:

| Usuario | Contrasena | Rol | Permisos |
|---------|------------|-----|----------|
| **Admin** | admin23 | ADMIN | Acceso completo (productos + almacenes + usuarios) |
| **productos** | producto19 | PRODUCTOS | Gestion de productos unicamente |
| **almacen** | almacen11 | ALMACEN | Gestion de almacenes unicamente |

**Nota:** Las contrasenas se almacenan con hash SHA256 en la base de datos.

---

## Caracteristicas Principales

### Sistema de Autenticacion
- Login con pantalla dividida personalizada
- Validacion de credenciales con hash SHA256
- Control de acceso basado en roles (RBAC)
- Registro de ultimo inicio de sesion

### Gestion de Productos
- CRUD completo (Crear, Leer, Actualizar, Eliminar)
- Filtros avanzados por:
  - Nombre del producto
  - Rango de precios
  - Rango de cantidades
  - Fechas de modificacion
  - Usuario que realizo cambios
- Ordenamiento por columnas (clic en encabezados)
- Auto-generacion de IDs
- Validacion de datos en tiempo real

### Gestion de Almacenes
- Administracion de bodegas/almacenes
- Relacion con productos
- Filtros por nombre y fechas
- Auditoria de cambios

### Interfaz de Usuario
- Tema personalizado con **colores oficiales UNISON**:
  - Azul UNISON: `#00529e`
  - Dorado UNISON: `#f8bb00`
- Botones redondeados con efectos hover
- Campos de entrada con bordes suavizados
- Selector de fechas con calendario visual
- Panel de filtros colapsable/expandible
- Diseño responsivo

---

## Solucion de Problemas Comunes

### Error: `ModuleNotFoundError: No module named 'tkcalendar'`

**Causa:** El entorno virtual no esta configurado correctamente.

**Solucion:**

1. **Ejecutar setup.bat desde la terminal:**
   ```cmd
   setup.bat
   # Opcion 1: Instalacion Completa
   # Opcion 4: Configurar VS Code
   ```

2. **Reiniciar VS Code:**
   - `Ctrl+Shift+P` → `Developer: Reload Window`

3. **Verificar instalacion:**
   ```cmd
   setup.bat
   # Opcion 3: Verificar Entorno
   ```

4. **Si persiste, reinstalar manualmente:**
   ```powershell
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

### Error: `tkinter.TclError` o interfaz no se muestra

**Causa:** `tkinter` no esta instalado correctamente.

**Solucion:**

- **Windows/Mac:** `tkinter` viene incluido con Python
- **Linux (Ubuntu/Debian):**
  ```bash
  sudo apt-get install python3-tk
  ```
- **Linux (Fedora):**
  ```bash
  sudo dnf install python3-tkinter
  ```

### La base de datos no se crea

**Causa:** Permisos insuficientes en la carpeta `database/`.

**Solucion:**
```bash
# Crear carpeta manualmente
mkdir database

# En Linux/Mac, dar permisos
chmod 755 database
```

### Script de Diagnostico Automatico

Ejecuta `setup.bat` (Windows) o `./setup.sh` (Linux/macOS) y selecciona **Opcion 3: Verificar Entorno**.

**Resultado esperado:**
```
[OK] Entorno virtual encontrado
[OK] tkcalendar version: 1.5.0
[OK] Pillow version: 12.0.0
[OK] tkinter disponible
[OK] sqlite3 version: 3.x.x
```

### Problemas con Code Runner en VS Code

**Sintoma:** Code Runner no ejecuta o da errores.

**Solucion:**
```cmd
# Ejecutar setup.bat desde la terminal
setup.bat
# Opcion 4: Configurar VS Code
# Luego reiniciar VS Code: Ctrl+Shift+P > Developer: Reload Window
```

La opcion 4 regenera la configuracion correcta de Code Runner automaticamente.



---

## Base de Datos

### Informacion General
- **Motor:** SQLite 3
- **Ubicacion:** `database/InventarioBD_2.db`
- **Creacion:** Automatica al iniciar la aplicacion por primera vez
- **Tamano inicial:** ~20 KB

### Esquema de Tablas

**Tabla `productos`:**
- `id` (TEXT) - Identificador unico
- `nombre` (TEXT) - Nombre del producto
- `precio` (REAL) - Precio unitario
- `cantidad` (INTEGER) - Cantidad en stock
- `departamento` (TEXT) - Departamento/categoria
- `almacen` (TEXT) - ID del almacen asociado
- `fecha_ultima_modificacion` (TEXT) - Timestamp
- `ultimo_usuario_modificacion` (TEXT) - Usuario que modifico

**Tabla `almacenes`:**
- `id` (TEXT) - Identificador unico
- `nombre` (TEXT) - Nombre del almacen
- `fecha_ultima_modificacion` (TEXT)
- `ultimo_usuario_modificacion` (TEXT)

**Tabla `usuarios`:**
- `id` (INTEGER) - ID autoincremental
- `nombre` (TEXT) - Nombre de usuario
- `contrasena` (TEXT) - Hash SHA256
- `rol` (TEXT) - ADMIN, PRODUCTOS o ALMACEN
- `ultimo_inicio_sesion` (TEXT)

### Respaldo y Restauracion

**Crear respaldo:**
```bash
# La base de datos es un archivo unico
cp database/InventarioBD_2.db database/backup_$(date +%Y%m%d).db
```

**Restaurar respaldo:**
```bash
cp database/backup_YYYYMMDD.db database/InventarioBD_2.db
```

---

## Arquitectura del Proyecto

### Patron MVC (Modelo-Vista-Controlador)

```
┌─────────────┐
│   VIEWS     │ <- Interfaz grafica (Tkinter)
│  (Vista)    │
└──────┬──────┘
       │
┌──────▼──────┐
│ CONTROLLERS │ <- Logica de negocio y validacion
│ (Controlador│
└──────┬──────┘
       │
┌──────▼──────┐
│   MODELS    │ <- Acceso a datos (SQLite)
│  (Modelo)   │
└─────────────┘
```

**Ventajas:**
- Separacion de responsabilidades
- Codigo mantenible y escalable
- Facil testeo de componentes
- Reutilizacion de codigo

---

## Informacion del Proyecto

### Autor
**Manuel Munguia Rubio**  
Ingenieria en Sistemas de Informacion  
Universidad de Sonora

### Curso
Base de Datos I - 2025

### Tecnologias Utilizadas
- **Lenguaje:** Python 3.13.7
- **GUI Framework:** Tkinter
- **Base de Datos:** SQLite 3
- **Control de Versiones:** Git & GitHub
- **IDE:** Visual Studio Code

### Repositorio
[github.com/DaManu123/Proyecto-BD1](https://github.com/DaManu123/Proyecto-BD1)

---

## Notas Tecnicas

### Estandares de Codigo
- **Arquitectura:** MVC (Modelo-Vista-Controlador)
- **Estilo:** PEP 8
- **Encoding:** UTF-8
- **Seguridad:** Hash SHA256 para contrasenas

### Caracteristicas Tecnicas
- Triggers SQLite para auditoria automatica
- Validacion de datos en tiempo real
- Manejo de errores con try-except

---

## Soporte

### Recursos Disponibles
1. **README.md** - Guia de instalacion y uso
2. **setup.bat / setup.sh** - Script de instalacion y configuracion automatica

### Instrucciones Importantes

**Para evitar problemas:**
1. Siempre ejecuta `setup.bat` desde la **terminal** (PowerShell o CMD)
2. Ejecuta **Opcion 1** primero (Instalacion Completa)
3. Ejecuta **Opcion 4** despues (Configurar VS Code)
4. Reinicia VS Code despues de configurar

---

**Ultima actualizacion:** Noviembre 2025  
**Version:** 1.0.0

