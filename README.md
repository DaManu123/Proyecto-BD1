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
cd Proyecto-BD1\databases-inventory-app

# 2. Ejecutar script maestro
setup.bat
```

#### **Linux/macOS:**
```bash
# 1. Clonar el repositorio
git clone https://github.com/DaManu123/Proyecto-BD1.git
cd Proyecto-BD1/databases-inventory-app

# 2. Dar permisos de ejecucion
chmod +x setup.sh

# 3. Ejecutar script maestro
./setup.sh
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

**Opcion 1 - Instalacion Completa:**
- Crea el entorno virtual `.venv`
- Instala todas las dependencias
- Configura VS Code automaticamente
- Verifica la instalacion

**Opcion 2 - Ejecutar Aplicacion:**
- Inicia el programa directamente
- Usa el entorno virtual configurado

**Opcion 3 - Verificar Entorno:**
- Muestra version de Python
- Lista paquetes instalados
- Verifica modulos requeridos

**Opcion 4 - Configurar VS Code:**
- Genera `settings.json` con configuracion portable
- Genera `launch.json` para debugging
- Configura Code Runner para funcionar como "Run Python File"
- Configura PYTHONPATH automaticamente

**Importante:** La configuracion funciona en **cualquier equipo y carpeta** sin modificaciones manuales.

### Metodo Manual (Opcional)

Si prefieres configurar manualmente:

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

#### **5. Ejecutar la Aplicacion**
```bash
python src/main.py
```

---

## Compatibilidad con IDEs

Este proyecto esta **preconfigurado automaticamente** para funcionar en cualquier IDE. El script `setup.bat`/`setup.sh` configura VS Code automaticamente con rutas portables.

### Visual Studio Code (Recomendado - Configurado Automaticamente)

#### Configuracion Inicial
1. Ejecuta `setup.bat` (Windows) o `./setup.sh` (Linux/macOS)
2. Selecciona **Opcion 1: Instalacion Completa**
3. (Opcional) Selecciona **Opcion 4: Configurar VS Code** para regenerar configuracion
4. Abre la carpeta del proyecto en VS Code
5. Reinicia VS Code si es necesario (Ctrl+Shift+P > Developer: Reload Window)

#### Configuraciones Automaticas Aplicadas

**settings.json:**
- Interprete Python configurado: `.venv/Scripts/python.exe`
- PYTHONPATH automatico apuntando a `src/`
- Code Runner configurado para funcionar igual que "Run Python File"
- Activacion automatica del entorno virtual en terminales

**launch.json:**
- **"Python: Main Application"** - Ejecuta `src/main.py` siempre (F5)
- **"Python: Current File"** - Ejecuta el archivo actual
- Debugging completo con breakpoints
- Variables de entorno configuradas

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
1. Abre el proyecto `databases-inventory-app`
2. PyCharm detectara automaticamente el entorno virtual `.venv`
3. Click derecho en `src/main.py` > Run

### Otros IDEs
El entorno virtual `.venv` funciona con cualquier IDE:
- **Ruta Windows:** `.venv\Scripts\python.exe`
- **Ruta Linux/Mac:** `.venv/bin/python`

---

## Formas de Ejecutar el Programa

### Metodo 1: Script Maestro (Recomendado)

**Windows:**
```cmd
setup.bat
# Selecciona opcion 2: Ejecutar Aplicacion
```

**Linux/macOS:**
```bash
./setup.sh
# Selecciona opcion 2: Ejecutar Aplicacion
```

### Metodo 2: Desde VS Code
1. Abre `src/main.py`
2. Presiona el boton **Run** (▶️) de Code Runner
3. O presiona **F5** para debugging

### Metodo 3: Terminal Manual
```bash
# Activar entorno virtual primero
# Windows:
.venv\Scripts\Activate.ps1

# Linux/Mac:
source .venv/bin/activate

# Ejecutar
python src/main.py
```

---

## Verificar Instalacion

Ejecuta el script maestro y selecciona **Opcion 3: Verificar Entorno**:

**Windows:**
```cmd
setup.bat
```

**Linux/macOS:**
```bash
./setup.sh
```

El menu de verificacion muestra:
- Directorio del proyecto y ruta del Python virtual
- Version de Python instalada
- Lista completa de paquetes
- Estado de modulos requeridos (tkcalendar, Pillow, tkinter, sqlite3)

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

**Causa:** El interprete de Python no encuentra el modulo porque no esta usando el entorno virtual.

**Solucion:**

1. **Ejecutar desde VS Code correctamente:**
   - Usa el boton **Run Python File** (▶️ en la esquina superior derecha)
   - O usa **Code Runner** (debe estar configurado con `setup.bat` opcion 4)
   - O presiona **F5** para debugging

2. **Si el error persiste, verificar entorno virtual:**
   ```bash
   # Ejecutar setup.bat y seleccionar opcion 3: Verificar Entorno
   setup.bat
   ```

3. **Reconfigurar VS Code:**
   ```bash
   # Ejecutar setup.bat y seleccionar opcion 4: Configurar VS Code
   setup.bat
   # Luego reiniciar VS Code (Ctrl+Shift+P > Developer: Reload Window)
   ```

4. **Reinstalar dependencias manualmente:**
   ```bash
   .venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

5. **Verificar instalacion:**
   ```bash
   python -c "import tkcalendar; print('OK:', tkcalendar.__version__)"
   # Debe mostrar: OK: 1.5.0 (o superior)
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

**Sintoma:** Code Runner no ejecuta o da errores de sintaxis PowerShell.

**Solucion:**
```bash
# Ejecutar setup.bat y seleccionar opcion 4
setup.bat
# Selecciona: 4) Configurar VS Code
# Luego reinicia VS Code
```

Esto regenerara `settings.json` y `launch.json` con la configuracion correcta para que Code Runner funcione igual que "Run Python File".



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
2. **verificar_entorno.bat** - Diagnostico automatico (Windows)

---

**Ultima actualizacion:** Noviembre 2025  
**Version:** 1.0.0

