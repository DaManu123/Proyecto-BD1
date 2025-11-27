# 🔧 Guía de Solución de Problemas

## ❌ Problema: "ModuleNotFoundError: No module named 'tkcalendar'"

### 📋 Descripción
Al ejecutar el programa usando el botón "Run" (▶️) de VS Code, aparece el error:
```
ModuleNotFoundError: No module named 'tkcalendar'
```

### 🎯 Causa Raíz
Este problema ocurre porque la extensión **Code Runner** de VS Code ejecuta el código usando el comando `python` del PATH del sistema, en lugar de usar el intérprete Python configurado en el entorno virtual del proyecto.

**Situación detectada:**
- ✅ **Entorno Virtual (.venv)**: SÍ tiene `tkcalendar` instalado
- ❌ **Python del Sistema (miniconda)**: NO tiene `tkcalendar` instalado
- 🔴 **Code Runner**: Usa el Python del sistema (incorrecto)

### ✅ Solución Implementada

Se ha configurado el archivo `.vscode/settings.json` para forzar a Code Runner a usar el entorno virtual:

```json
{
    "code-runner.executorMap": {
        "python": "cd $dir ; & 'C:/Users/ManuelPC/Documents/Visual Studio Code/Python/Proyecto bd1/.venv/Scripts/python.exe' -u $fullFileName"
    },
    "code-runner.runInTerminal": true
}
```

**Notas importantes sobre la configuración:**
- Se usa **comillas simples** (`'`) alrededor de la ruta del Python ejecutable para manejar espacios en la ruta
- Se usa **forward slashes** (`/`) en lugar de backslashes (`\`) para mayor compatibilidad en PowerShell
- La variable `$fullFileName` NO lleva comillas (Code Runner ya la maneja correctamente)
- El comando `cd $dir` asegura que el directorio de trabajo sea el del archivo ejecutado

### 🚀 Formas de Ejecutar el Programa

#### **Opción 1: Botón "Run" de Code Runner** (▶️)
- Ahora funcionará correctamente con la configuración actualizada
- Usa automáticamente el entorno virtual

#### **Opción 2: Terminal Integrado** (Recomendado)
```powershell
# Desde la raíz del proyecto
cd databases-inventory-app
.\.venv\Scripts\Activate.ps1
python src\main.py
```

#### **Opción 3: Scripts de Ejecución Automática**
```powershell
# Usar el script que activa el entorno automáticamente
.\run_with_venv.bat
```

#### **Opción 4: Debugger de Python en VS Code** (🐛)
- Presiona `F5` para ejecutar con el debugger
- Usa automáticamente el intérprete configurado en `settings.json`

### 🔍 Verificación de la Solución

Para verificar que el entorno está configurado correctamente:

```powershell
# Verificar que el entorno virtual tiene las dependencias
& "C:/Users/ManuelPC/Documents/Visual Studio Code/Python/Proyecto bd1/.venv/Scripts/python.exe" -m pip list

# Debería mostrar:
# Package    Version
# ---------- -------
# pillow     12.0.0
# tkcalendar 1.6.1
```

### 📦 Paquetes Requeridos

El proyecto requiere estos paquetes instalados en el entorno virtual:
- `Pillow>=9.0.0` - Manejo de imágenes
- `tkcalendar>=1.6.0` - Selectores de fecha

### 🛠️ Reinstalar Dependencias (si es necesario)

Si necesitas reinstalar el entorno virtual desde cero:

```powershell
# 1. Eliminar entorno virtual existente
Remove-Item -Recurse -Force .venv

# 2. Crear nuevo entorno virtual
python -m venv .venv

# 3. Activar entorno virtual
.\.venv\Scripts\Activate.ps1

# 4. Instalar dependencias
pip install -r requirements.txt
```

### 📝 Notas Adicionales

**¿Por qué usar entorno virtual?**
- ✅ Aislamiento de dependencias del proyecto
- ✅ Evita conflictos con otros proyectos Python
- ✅ Garantiza reproducibilidad del entorno
- ✅ Facilita el despliegue en otros sistemas

**Intérpretes Python Disponibles en el Sistema:**
1. `C:\ProgramData\miniconda3\python.exe` - Instalación de Miniconda (sistema)
2. `C:\Users\ManuelPC\AppData\Local\Programs\Python\Python313\python.exe` - Python standalone
3. `C:\Users\ManuelPC\miniconda3\python.exe` - Miniconda usuario
4. **`.venv\Scripts\python.exe`** - ✅ **CORRECTO - Entorno virtual del proyecto**

---

**Universidad de Sonora - Ingeniería en Software**  
**Base de Datos I - Sistema de Inventario**  
*Última actualización: Noviembre 2025*
