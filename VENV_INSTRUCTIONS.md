# Instrucciones para el Entorno Virtual

## 🐍 Entorno Virtual Creado

Se ha creado exitosamente un entorno virtual para este proyecto ubicado en la carpeta `venv/`.

### 📋 ¿Qué es un entorno virtual?

Un entorno virtual es un espacio aislado donde puedes instalar paquetes de Python específicos para este proyecto sin afectar otros proyectos o la instalación global de Python.

### 🚀 Cómo usar el entorno virtual

#### Opción 1: Script Automático (Recomendado)
```bash
# Ejecutar con entorno virtual automáticamente
run_with_venv.bat
```

#### Opción 2: PowerShell
```powershell
# Activar entorno virtual
.\activate_venv.ps1

# Ejecutar aplicación
python src\main.py

# Desactivar cuando termines
deactivate
```

#### Opción 3: Comandos Manuales
```bash
# 1. Activar entorno virtual
venv\Scripts\activate

# 2. Ejecutar aplicación
python src\main.py

# 3. Desactivar entorno virtual
deactivate
```

### 📦 Gestión de Paquetes

```bash
# Activar entorno virtual primero
venv\Scripts\activate

# Ver paquetes instalados
pip list

# Instalar nuevo paquete (si necesario)
pip install nombre_paquete

# Guardar dependencias
pip freeze > requirements.txt

# Instalar desde requirements.txt
pip install -r requirements.txt
```

### 🔧 Configuración en VS Code

Para que VS Code use automáticamente el entorno virtual:

1. Abre VS Code en el directorio del proyecto
2. Presiona `Ctrl+Shift+P`
3. Busca "Python: Select Interpreter"
4. Selecciona el intérprete del entorno virtual:
   ```
   .\venv\Scripts\python.exe
   ```

### ✅ Verificar que funciona

```bash
# Con entorno virtual activado, deberías ver (venv) al inicio del prompt
(venv) PS C:\...\databases-inventory-app>

# Verificar versión de Python
python --version

# Verificar ubicación de Python
Get-Command python
```

### 🗂️ Estructura del Entorno Virtual

```
venv/
├── Scripts/           # Ejecutables (activar, python, pip)
├── Lib/              # Librerías instaladas
├── Include/          # Headers de C
└── pyvenv.cfg        # Configuración del entorno
```

### ⚠️ Importante

- **NUNCA** subas la carpeta `venv/` al control de versiones (Git)
- Siempre activa el entorno virtual antes de trabajar en el proyecto
- Si compartes el proyecto, incluye `requirements.txt` para que otros puedan recrear el entorno

### 🎯 Beneficios

✅ **Aislamiento**: No conflictos con otros proyectos
✅ **Reproducibilidad**: Mismo entorno en diferentes máquinas  
✅ **Limpieza**: No contaminas la instalación global de Python
✅ **Flexibilidad**: Diferentes versiones de paquetes por proyecto