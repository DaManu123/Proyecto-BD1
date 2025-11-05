@echo off
REM Script de instalación y configuración del entorno virtual
REM Para el Sistema de Inventario - Base de Datos 1

echo ==================================================
echo   Sistema de Inventario - Configuración Inicial
echo   Universidad de Sonora - Base de Datos 1
echo ==================================================

REM Verificar que Python está instalado
echo 🔍 Verificando instalación de Python...
python --version

if %ERRORLEVEL% neq 0 (
    echo ❌ Error: Python no está instalado o no está en el PATH
    echo    Por favor instala Python 3.7+ desde https://python.org
    pause
    exit /b 1
)

echo ✅ Python encontrado

REM Verificar si ya existe el entorno virtual
if exist "venv" (
    echo ⚠️  El entorno virtual ya existe
    echo    ¿Deseas recrearlo? [S/N]
    set /p "recreate="
    if /i "%recreate%"=="S" (
        echo 🗑️  Eliminando entorno virtual existente...
        rmdir /s /q venv
    ) else (
        echo ✅ Usando entorno virtual existente
        goto :activation_instructions
    )
)

REM Crear entorno virtual
echo 📦 Creando entorno virtual...
python -m venv venv

if %ERRORLEVEL% neq 0 (
    echo ❌ Error al crear el entorno virtual
    pause
    exit /b 1
)

echo ✅ Entorno virtual creado en .\venv\

:activation_instructions
echo ==================================================
echo 🚀 Configuración completada!
echo ==================================================
echo.
echo Para usar la aplicación:
echo.
echo 1. Activar entorno virtual:
echo    venv\Scripts\activate
echo.
echo 2. Ejecutar aplicación:
echo    python src\main.py
echo.
echo 3. Alternativamente, usar scripts automáticos:
echo    - run_with_venv.bat (ejecuta todo automáticamente)
echo    - activate_venv.ps1 (solo activa el entorno)
echo.
echo ==================================================
echo 📚 Archivos de ayuda disponibles:
echo    - README.md (documentación completa)
echo    - VENV_INSTRUCTIONS.md (guía del entorno virtual)
echo    - copilot-instructions.md (para desarrolladores)
echo ==================================================
echo.
echo ¿Deseas ejecutar la aplicación ahora? [S/N]
set /p "run_now="
if /i "%run_now%"=="S" (
    echo.
    echo 🚀 Ejecutando aplicación con entorno virtual...
    call run_with_venv.bat
)

pause