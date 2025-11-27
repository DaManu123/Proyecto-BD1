# Guía de Configuración de VS Code para el Proyecto

## 🔍 Problema Común: Error `^&` en PowerShell

### ¿Por qué ocurre este error?

El error `^&` aparece cuando se mezcla sintaxis de diferentes shells (terminales):

| Shell | Sintaxis Correcta | Ejemplo |
|-------|-------------------|---------|
| **PowerShell** | `& "ruta"` | `& "C:\Python\python.exe" "script.py"` |
| **CMD** | `"ruta"` o `^&` | `"C:\Python\python.exe" "script.py"` |
| **Bash/Zsh** | `ruta` | `/usr/bin/python script.py` |

**El problema:** Usar `^&` (sintaxis de CMD) en PowerShell genera un error de parsing.

---

## ✅ Solución Automática

Este proyecto incluye configuración automática a través de `setup.bat`:

```cmd
setup.bat
# Selecciona: 1) Instalación Completa
# O: 4) Configurar VS Code
```

Esto genera automáticamente:
- `.vscode/settings.json` - Configuración de Code Runner con sintaxis PowerShell correcta
- `.vscode/launch.json` - Configuración de debugging

---

## 📋 Configuración Generada Automáticamente

### settings.json

El script `setup.bat` crea este archivo con la configuración correcta:

```json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/.venv/Scripts/python.exe",
    "python.analysis.extraPaths": [
        "${workspaceFolder}/src",
        "${workspaceFolder}/src/utils"
    ],
    "python.terminal.activateEnvironment": true,
    "python.terminal.activateEnvInCurrentTerminal": true,
    
    "code-runner.executorMap": {
        "python": "& \"$workspaceRoot/.venv/Scripts/python.exe\" \"$fullFileName\""
    },
    "code-runner.runInTerminal": true,
    "code-runner.clearPreviousOutput": true,
    "code-runner.saveFileBeforeRun": true,
    "code-runner.fileDirectoryAsCwd": false,
    
    "python.envFile": "${workspaceFolder}/.env",
    "terminal.integrated.env.windows": {
        "PYTHONPATH": "${workspaceFolder}/src"
    },
    "terminal.integrated.defaultProfile.windows": "PowerShell"
}
```

**Puntos clave:**
- ✅ `&` sin `^` → Sintaxis correcta de PowerShell
- ✅ Comillas dobles alrededor de rutas con espacios
- ✅ `${workspaceFolder}` → Variable de VS Code (python.defaultInterpreterPath, env, etc.)
- ✅ `$workspaceRoot` → Variable de Code Runner (SOLO en executorMap)
- ✅ Shell por defecto configurado a PowerShell
- ⚠️ **CRÍTICO:** Code Runner NO expande `${workspaceFolder}`, usa `$workspaceRoot`

### launch.json

Configuración para debugging (F5):

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Main Application",
            "type": "debugpy",
            "request": "launch",
            "program": "${workspaceFolder}/src/main.py",
            "console": "integratedTerminal",
            "cwd": "${workspaceFolder}",
            "env": {
                "PYTHONPATH": "${workspaceFolder}/src"
            },
            "justMyCode": true
        },
        {
            "name": "Python: Current File",
            "type": "debugpy",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "cwd": "${workspaceFolder}",
            "env": {
                "PYTHONPATH": "${workspaceFolder}/src"
            },
            "justMyCode": true
        }
    ]
}
```

---

## 🚀 Formas de Ejecutar el Proyecto en VS Code

### 1. Code Runner (▶️)
- Abre `src/main.py`
- Click en el botón **Run** (▶️) en la esquina superior derecha
- Usa el entorno virtual automáticamente

### 2. Run Python File
- Abre `src/main.py`
- Click derecho → **Run Python File in Terminal**
- Funcionalmente idéntico a Code Runner

### 3. Debugger (F5)
- Presiona **F5**
- Selecciona **"Python: Main Application"**
- Permite usar breakpoints y depuración paso a paso

### 4. Terminal Integrado
```powershell
# El entorno virtual se activa automáticamente
python src/main.py
```

---

## 🔧 Solución Manual (Si es Necesario)

### Si el error persiste después de ejecutar setup.bat:

1. **Verificar shell activo en VS Code:**
   - Presiona `Ctrl+Shift+P`
   - Escribe: `Terminal: Select Default Profile`
   - Selecciona: **PowerShell**

2. **Regenerar configuración:**
   ```cmd
   setup.bat
   # Opción 4: Configurar VS Code
   ```

3. **Reiniciar VS Code:**
   - Presiona `Ctrl+Shift+P`
   - Escribe: `Developer: Reload Window`
   - Presiona Enter

4. **Verificar archivos generados:**
   - Asegúrate de que `.vscode/settings.json` existe
   - Verifica que NO contenga `^&` (solo `&`)

---

## 🚨 Errores Comunes y Soluciones

### Error: "No se permite usar el carácter de Y comercial (&)"

**Causa:** El archivo settings.json tiene `^&` en lugar de `&`

**Solución:**
```cmd
# Ejecutar setup.bat opción 4
setup.bat
```

### Error: "No se puede cargar el archivo .ps1"

**Causa:** Política de ejecución de PowerShell restrictiva

**Solución (PowerShell como Administrador):**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Error: "ModuleNotFoundError"

**Causa:** Entorno virtual no activado o ruta incorrecta

**Solución:**
```cmd
# Verificar instalación
setup.bat
# Opción 3: Verificar Entorno
```

---

## 📊 Tabla de Referencia Rápida

| Situación | Comando/Configuración |
|-----------|----------------------|
| **PowerShell (Recomendado)** | `& "ruta\python.exe" "archivo.py"` |
| **CMD** | `"ruta\python.exe" "archivo.py"` |
| **VS Code settings.json** | `"python": "& \"${workspaceFolder}/.venv/...\"` |
| **Terminal manual** | `python src\main.py` |

---

## 🎯 Checklist Post-Instalación

- [ ] Ejecutado `setup.bat` opción 1 (Instalación Completa)
- [ ] Verificado que `.vscode/settings.json` existe
- [ ] Confirmado que settings.json NO contiene `^&`
- [ ] Shell de VS Code configurado a PowerShell
- [ ] Code Runner ejecuta sin errores
- [ ] Debugger (F5) funciona correctamente

---

## 💡 Consejos para Otros Proyectos

### Plantilla Minimalista para Nuevos Proyectos

Crea `.vscode/settings.json` con:

```json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/.venv/Scripts/python.exe",
    "code-runner.executorMap": {
        "python": "& \"$workspaceRoot/.venv/Scripts/python.exe\" \"$fullFileName\""
    },
    "code-runner.runInTerminal": true,
    "terminal.integrated.defaultProfile.windows": "PowerShell"
}
```

**⚠️ IMPORTANTE - Diferencia entre variables:**
- `${workspaceFolder}` = Variable de VS Code (para python.defaultInterpreterPath, launch.json)
- `$workspaceRoot` = Variable de Code Runner (para code-runner.executorMap)
- **NO mezclar:** Code Runner NO expande `${workspaceFolder}`

**Regla de Oro:** Si usas Windows con VS Code, usa PowerShell y el operador `&` (sin `^`)

---

## 📞 Comandos Útiles

### Verificar Entorno

```powershell
# Versión de Python
python --version

# Ruta de Python activo
Get-Command python

# Verificar entorno virtual activo
python -c "import sys; print(sys.prefix)"

# Listar paquetes instalados
pip list
```

### Activar Entorno Virtual Manualmente

```powershell
# PowerShell
.\.venv\Scripts\Activate.ps1

# CMD
.\.venv\Scripts\activate.bat

# Desactivar
deactivate
```

---

## 🔄 Portabilidad

Esta configuración es **completamente portable**:
- ✅ Funciona en cualquier PC con Windows
- ✅ No requiere rutas absolutas
- ✅ Se adapta automáticamente a la ubicación del proyecto
- ✅ Compatible con diferentes versiones de Python

Solo necesitas:
1. Copiar el proyecto completo
2. Ejecutar `setup.bat` opción 1
3. Abrir en VS Code

---

**Última actualización:** Noviembre 2025  
**Proyecto:** Sistema de Inventario UNISON  
**Autor:** Manuel Munguía Rubio
