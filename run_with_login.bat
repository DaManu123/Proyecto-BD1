@echo off
echo ================================================
echo   Sistema de Inventario con Login
echo   Universidad de Sonora - Base de Datos 1
echo   Autor: Manuel Munguia Rubio
echo ================================================
echo.

echo Activando entorno virtual...
cd /d "%~dp0"
call venv\Scripts\activate.bat

echo.
echo Ejecutando aplicacion con sistema de login...
echo.
echo Credenciales de prueba:
echo - Usuario: Admin, Contrasena: admin23
echo - Usuario: almacen, Contrasena: almacen11  
echo - Usuario: productos, Contrasena: producto19
echo.

python src\app_with_login.py

echo.
echo Aplicacion cerrada.
pause