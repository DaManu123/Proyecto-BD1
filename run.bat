@echo off
REM ====================================================
REM Script de Ejecucion - Sistema de Inventario
REM Universidad de Sonora - Base de Datos I
REM ====================================================

echo.
echo ================================================
echo   Sistema de Inventario - Universidad de Sonora
echo ================================================
echo.

REM Verificar si existe el entorno virtual
if not exist ".venv\Scripts\python.exe" (
    echo [ERROR] Entorno virtual no encontrado
    echo.
    echo Primero debes ejecutar setup.bat para configurar el proyecto
    echo.
    pause
    exit /b 1
)

echo [INFO] Iniciando aplicacion...
echo.

REM Ejecutar la aplicacion con el entorno virtual
.venv\Scripts\python.exe src\main.py

if errorlevel 1 (
    echo.
    echo [ERROR] La aplicacion termino con errores
    echo.
    pause
    exit /b 1
)

echo.
echo [INFO] Aplicacion cerrada
