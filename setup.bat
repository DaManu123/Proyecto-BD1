@echo off
REM ====================================================
REM Script de Instalacion - Sistema de Inventario
REM Universidad de Sonora - Base de Datos I
REM ====================================================

echo.
echo ================================================
echo   INSTALACION - Sistema de Inventario UNISON
echo ================================================
echo.
echo Este script configurara el entorno para ejecutar
echo la aplicacion en cualquier equipo.
echo.
echo Presiona cualquier tecla para continuar...
pause >nul

echo.
echo [PASO 1/4] Verificando Python...
echo.

REM Verificar que Python esta instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python NO esta instalado o no esta en el PATH
    echo.
    echo Por favor:
    echo   1. Descarga Python desde https://www.python.org/downloads/
    echo   2. Durante la instalacion, marca "Add Python to PATH"
    echo   3. Reinicia esta terminal y vuelve a ejecutar setup.bat
    echo.
    pause
    exit /b 1
)

echo [OK] Python encontrado
python --version
echo.

echo [PASO 2/4] Creando entorno virtual...
echo.

REM Verificar si ya existe el entorno virtual
if exist ".venv\" (
    echo [!] Ya existe un entorno virtual en .venv\
    echo.
    set /p "RECREATE=Deseas recrearlo? (S/N): "
    if /i "%RECREATE%"=="S" (
        echo.
        echo [INFO] Eliminando entorno virtual existente...
        rmdir /s /q .venv
        echo [OK] Entorno virtual eliminado
    ) else (
        echo.
        echo [INFO] Usando entorno virtual existente
        goto :install_deps
    )
)

echo [INFO] Creando nuevo entorno virtual en .venv\...
python -m venv .venv

if errorlevel 1 (
    echo [ERROR] No se pudo crear el entorno virtual
    echo.
    echo Verifica que tienes permisos de escritura en esta carpeta
    pause
    exit /b 1
)

echo [OK] Entorno virtual creado exitosamente
echo.

:install_deps
echo [PASO 3/4] Instalando dependencias...
echo.

REM Activar entorno virtual e instalar dependencias
call .venv\Scripts\activate.bat

echo [INFO] Actualizando pip...
python -m pip install --upgrade pip --quiet

echo [INFO] Instalando dependencias desde requirements.txt...
pip install -r requirements.txt

if errorlevel 1 (
    echo [ERROR] Hubo un problema al instalar las dependencias
    echo.
    echo Intenta manualmente:
    echo   1. .venv\Scripts\activate
    echo   2. pip install -r requirements.txt
    pause
    exit /b 1
)

echo [OK] Dependencias instaladas correctamente
echo.

echo [PASO 4/4] Verificando instalacion...
echo.

REM Verificar modulos criticos
echo Verificando modulos requeridos:
echo.

python -c "import tkcalendar; print('  [OK] tkcalendar version:', tkcalendar.__version__)" 2>nul
if errorlevel 1 (
    echo   [ERROR] tkcalendar NO instalado
)

python -c "import PIL; print('  [OK] Pillow version:', PIL.__version__)" 2>nul
if errorlevel 1 (
    echo   [ERROR] Pillow NO instalado
)

python -c "import tkinter; print('  [OK] tkinter disponible')" 2>nul
if errorlevel 1 (
    echo   [WARN] tkinter NO disponible (debe venir con Python)
)

python -c "import sqlite3; print('  [OK] sqlite3 version:', sqlite3.sqlite_version)" 2>nul
if errorlevel 1 (
    echo   [ERROR] sqlite3 NO disponible
)

echo.
echo ================================================
echo   INSTALACION COMPLETADA
echo ================================================
echo.
echo El entorno esta listo para usar!
echo.
echo PROXIMOS PASOS:
echo.
echo 1. Para verificar la instalacion:
echo    verificar_entorno.bat
echo.
echo 2. Para ejecutar la aplicacion:
echo.
echo    Opcion A - Terminal:
echo      .venv\Scripts\activate
echo      python src\main.py
echo.
echo    Opcion B - VS Code:
echo      1. Abre el proyecto en VS Code
echo      2. Selecciona el interprete: .venv\Scripts\python.exe
echo      3. Presiona F5 o el boton Run
echo.
echo    Opcion C - PyCharm/Otras IDEs:
echo      1. Configura el interprete de Python a: .venv\Scripts\python.exe
echo      2. Ejecuta: src\main.py
echo.
echo CREDENCIALES DE ACCESO:
echo   Usuario: Admin      Password: admin23      (Acceso completo)
echo   Usuario: productos  Password: producto19   (Solo productos)
echo   Usuario: almacen    Password: almacen11    (Solo almacenes)
echo.
echo ================================================
echo.

pause
