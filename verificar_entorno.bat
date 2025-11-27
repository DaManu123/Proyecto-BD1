@echo off
REM ====================================================
REM Script de Verificacion del Entorno - Sistema Inventario
REM Universidad de Sonora - Base de Datos I
REM ====================================================

echo.
echo ========================================
echo  VERIFICACION DEL ENTORNO PYTHON
echo ========================================
echo.

REM Obtener la ruta del workspace
set "WORKSPACE_ROOT=%~dp0.."
set "VENV_PATH=%WORKSPACE_ROOT%\.venv\Scripts\python.exe"

echo [1/5] Verificando ubicacion del workspace...
echo Workspace: %WORKSPACE_ROOT%
echo.

echo [2/5] Verificando entorno virtual...
if exist "%VENV_PATH%" (
    echo [OK] Entorno virtual encontrado
    echo Ruta: %VENV_PATH%
) else (
    echo [ERROR] Entorno virtual NO encontrado
    echo Ruta esperada: %VENV_PATH%
    echo.
    echo SOLUCION: Ejecuta setup.bat para crear el entorno virtual
    pause
    exit /b 1
)
echo.

echo [3/5] Verificando version de Python...
"%VENV_PATH%" --version
echo.

echo [4/5] Verificando dependencias instaladas...
"%VENV_PATH%" -m pip list --format=columns
echo.

echo [5/5] Verificando modulos requeridos...
echo.

echo Verificando tkcalendar...
"%VENV_PATH%" -c "import tkcalendar; print('  [OK] tkcalendar version:', tkcalendar.__version__)" 2>nul
if errorlevel 1 (
    echo   [ERROR] tkcalendar NO instalado
    echo   SOLUCION: pip install tkcalendar
) else (
    echo   Importacion exitosa
)
echo.

echo Verificando Pillow...
"%VENV_PATH%" -c "import PIL; print('  [OK] Pillow version:', PIL.__version__)" 2>nul
if errorlevel 1 (
    echo   [ERROR] Pillow NO instalado
    echo   SOLUCION: pip install Pillow
) else (
    echo   Importacion exitosa
)
echo.

echo Verificando tkinter...
"%VENV_PATH%" -c "import tkinter; print('  [OK] tkinter disponible')" 2>nul
if errorlevel 1 (
    echo   [ERROR] tkinter NO disponible
    echo   NOTA: tkinter debe venir con Python
) else (
    echo   Importacion exitosa
)
echo.

echo Verificando sqlite3...
"%VENV_PATH%" -c "import sqlite3; print('  [OK] sqlite3 version:', sqlite3.sqlite_version)" 2>nul
if errorlevel 1 (
    echo   [ERROR] sqlite3 NO disponible
) else (
    echo   Importacion exitosa
)
echo.

echo ========================================
echo  VERIFICACION COMPLETADA
echo ========================================
echo.
echo Si todos los modulos muestran [OK], el entorno esta configurado correctamente.
echo Puedes ejecutar la aplicacion con: run_with_venv.bat
echo.

pause
