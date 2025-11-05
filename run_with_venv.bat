@echo off
REM Script para activar el entorno virtual y ejecutar la aplicación
echo ================================================
echo     Sistema de Inventario - Base de Datos 1
echo     Universidad de Sonora
echo     Estudiante: Manuel Munguia Rubio
echo     Usando Entorno Virtual
echo ================================================

cd /d "C:\Users\ManuelPC\Documents\Visual Studio Code\Python\Proyecto bd1\databases-inventory-app"

echo Activando entorno virtual...
call venv\Scripts\activate.bat

echo Ejecutando aplicación desde entorno virtual...
echo.

python src\main.py

if %ERRORLEVEL% neq 0 (
    echo.
    echo Error al ejecutar la aplicación.
    pause
)

echo.
echo La aplicación se ha cerrado.
echo Desactivando entorno virtual...
call venv\Scripts\deactivate.bat
pause