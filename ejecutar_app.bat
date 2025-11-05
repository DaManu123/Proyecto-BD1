@echo off
echo ================================================
echo     Sistema de Inventario - Base de Datos 1
echo     Universidad de Sonora
echo ================================================
echo.

cd /d "C:\Users\ManuelPC\Documents\Visual Studio Code\Python\Proyecto bd1\databases-inventory-app"

echo Iniciando la aplicación...
echo.

python src\main.py

if %ERRORLEVEL% neq 0 (
    echo.
    echo Error al ejecutar la aplicación.
    echo Verifica que Python esté instalado y en el PATH.
    pause
)

echo.
echo La aplicación se ha cerrado.
pause