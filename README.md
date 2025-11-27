# Sistema de Inventario - Universidad de Sonora

Sistema de gestión de inventario desarrollado con Python/Tkinter y SQLite para la Universidad de Sonora.

## 📋 Requisitos Previos

- Python 3.7 o superior (desarrollado con Python 3.13.7)
- Entorno virtual (venv) configurado
- VS Code (recomendado)

## 🚀 Instalación y Configuración

### 1. Configurar Entorno Virtual

El proyecto utiliza un entorno virtual ubicado en la raíz del workspace:
```
Proyecto bd1/.venv/
```

**En Windows:**
```powershell
# Activar el entorno virtual
.venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

**En Linux/Mac:**
```bash
# Activar el entorno virtual
source .venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

### 2. Dependencias Requeridas

El proyecto requiere las siguientes bibliotecas:
- `Pillow>=9.0.0` - Para manejo de imágenes (logo universitario)
- `tkcalendar>=1.6.0` - Para selectores de fecha en filtros

Bibliotecas estándar utilizadas (incluidas en Python):
- `tkinter` - Interfaz gráfica
- `sqlite3` - Base de datos
- `os`, `sys` - Operaciones del sistema

### 3. Estructura del Proyecto

```
databases-inventory-app/
├── src/
│   ├── main.py                 # Punto de entrada
│   ├── controllers/            # Lógica de control
│   ├── models/                 # Modelos de datos y BD
│   ├── views/                  # Interfaces de usuario
│   └── utils/                  # Utilidades y tema
├── database/                   # Base de datos SQLite
├── .vscode/                    # Configuración de VS Code
│   ├── settings.json          # Configuración del intérprete
│   └── launch.json            # Configuración de depuración
└── requirements.txt           # Dependencias del proyecto
```

## 🎮 Ejecución del Programa

### Opción 1: Desde la Terminal

**Windows (PowerShell):**
```powershell
cd databases-inventory-app
& "C:/Users/ManuelPC/Documents/Visual Studio Code/Python/Proyecto bd1/.venv/Scripts/python.exe" src/main.py
```

O usando el entorno activado:
```powershell
.venv\Scripts\activate
python src\main.py
```

**Linux/Mac:**
```bash
source .venv/bin/activate
python src/main.py
```

### Opción 2: Desde VS Code

#### Ejecutar con Code Runner (Botón ▶️):
1. Abre el archivo `src/main.py`
2. Presiona `Ctrl+Alt+N` o haz clic en el botón ▶️ (Run Code)
3. El programa se ejecutará usando la configuración del archivo `.vscode/settings.json`

#### Ejecutar con Debugger (F5):
1. Abre el archivo `src/main.py`
2. Presiona `F5` o ve a `Run > Start Debugging`
3. Selecciona la configuración "Python: Ejecutar Inventario"
4. El programa se ejecutará en modo depuración

## 🔧 Solución de Problemas

### ❌ Error: `ModuleNotFoundError: No module named 'tkcalendar'`

Este error ocurre cuando VS Code ejecuta el código con un intérprete de Python incorrecto (del sistema en lugar del entorno virtual).

**Causa:** La extensión Code Runner ejecuta el comando `python` del PATH del sistema, que no tiene las dependencias instaladas.

**✅ Solución (YA IMPLEMENTADA):**

El proyecto está configurado para usar automáticamente el entorno virtual. El archivo `.vscode/settings.json` contiene:

```json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/.venv/Scripts/python.exe",
    "code-runner.executorMap": {
        "python": "${workspaceFolder}/.venv/Scripts/python.exe -u"
    },
    "code-runner.runInTerminal": true
}
```

**Si aún tienes el error:**

1. **Recargar VS Code:**
   - Presiona `Ctrl+Shift+P`
   - Escribe "Developer: Reload Window"
   - Presiona Enter

2. **Verificar el intérprete:**
   - Presiona `Ctrl+Shift+P`
   - Escribe "Python: Select Interpreter"
   - Selecciona: `.venv\Scripts\python.exe` (debe tener una marca ✓)

3. **Reinstalar dependencias (si es necesario):**
   ```powershell
   .venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

4. **Verificar instalación:**
   ```powershell
   & ".venv\Scripts\python.exe" -c "import tkcalendar; print('OK:', tkcalendar.__version__)"
   # Debería mostrar: OK: 1.5.0 (o superior)
   ```

📖 Para más detalles, consulta el archivo `TROUBLESHOOTING.md`

### Error: Problemas con imports relativos

Si ves errores como `ImportError: attempted relative import with no known parent package`:

**Solución:**
- Asegúrate de ejecutar el programa desde la carpeta `databases-inventory-app`
- La variable `PYTHONPATH` debe apuntar a la carpeta `src`
- Usa los archivos de configuración `.vscode/settings.json` y `.vscode/launch.json` proporcionados

### La aplicación no muestra la interfaz gráfica

**Solución:**
1. Verifica que tkinter esté instalado (viene con Python estándar)
2. En Linux, puede requerir instalación manual: `sudo apt-get install python3-tk`
3. Verifica que no haya errores en la consola

## 📊 Base de Datos

La base de datos SQLite se crea automáticamente en:
```
databases-inventory-app/database/InventarioBD_2.db
```

### Usuarios por defecto:

| Usuario | Contraseña | Rol |
|---------|------------|-----|
| Admin | admin23 | ADMIN |
| almacen | almacen11 | ALMACEN |
| productos | producto19 | PRODUCTOS |

## 🎨 Características

- ✅ Sistema de autenticación con roles
- ✅ Gestión de productos con filtros avanzados
- ✅ Gestión de almacenes
- ✅ Filtros por fecha, usuario, precio, cantidad
- ✅ Tema personalizado UNISON (colores oficiales)
- ✅ Interfaz responsiva con diseño moderno
- ✅ Ordenamiento de columnas en tablas
- ✅ Panel de filtros colapsable

## 👤 Autor

**Manuel Munguia Rubio**  
Ingeniería en Sistemas de Información  
Universidad de Sonora

## 📝 Notas Adicionales

- El proyecto utiliza la arquitectura MVC (Modelo-Vista-Controlador)
- Los colores del tema siguen la identidad corporativa de la Universidad de Sonora
- La base de datos incluye triggers y auditoría automática de cambios
- Todos los campos de formulario tienen validación en tiempo real

## 🆘 Soporte

Si encuentras problemas:
1. Verifica que el entorno virtual esté activado
2. Confirma que todas las dependencias estén instaladas: `pip list`
3. Revisa la configuración de VS Code en `.vscode/settings.json`
4. Verifica la versión de Python: `python --version` (debe ser 3.7+)
