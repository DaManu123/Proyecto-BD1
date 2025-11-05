@echo off
echo Iniciando Sistema de Inventario con Login Integrado...
echo.

cd /d "%~dp0src"

if not exist main.py (
    echo Error: No se encuentra el archivo main.py
    pause
    exit /b 1
)

echo Ejecutando aplicacion...
python main.py

if errorlevel 1 (
    echo.
    echo Error al ejecutar la aplicacion.
    pause
)