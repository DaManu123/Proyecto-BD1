@echo off
REM ====================================================
REM Script NUEVO de Compilacion - Sistema Inventario
REM Universidad de Sonora
REM Metodo: auto-py-to-exe (GUI + PyInstaller mejorado)
REM ====================================================

setlocal enabledelayedexpansion

set "PROJECT_ROOT=%~dp0"
set "VENV_PATH=%PROJECT_ROOT%.venv"
set "PYTHON_EXE=%VENV_PATH%\Scripts\python.exe"

cls
echo.
echo ====================================================
echo   COMPILACION A EJECUTABLE - METODO MEJORADO
echo   Sistema de Inventario UNISON
echo ====================================================
echo.

REM Verificar entorno virtual
if not exist "%PYTHON_EXE%" (
    echo [ERROR] Entorno virtual no encontrado.
    echo.
    echo Por favor ejecuta primero: setup.bat - Opcion 1
    echo.
    pause
    exit /b 1
)

echo [PASO 1/3] Instalando auto-py-to-exe...
echo.
"%PYTHON_EXE%" -m pip install auto-py-to-exe --quiet
if errorlevel 1 (
    echo [ERROR] No se pudo instalar auto-py-to-exe
    pause
    exit /b 1
)
echo [OK] auto-py-to-exe instalado
echo.

echo [PASO 2/3] Abriendo interfaz grafica de configuracion...
echo.
echo INSTRUCCIONES:
echo.
echo 1. En "Script Location": Selecciona: %PROJECT_ROOT%src\main.py
echo 2. En "Onefile": Selecciona "One Directory" (carpeta)
echo 3. En "Console Window": Selecciona "Window Based" (sin consola)
echo 4. En "Icon": Selecciona: %PROJECT_ROOT%unilogo.gif (opcional)
echo.
echo 5. En "Additional Files": Agrega estos archivos/carpetas:
echo    - %PROJECT_ROOT%database (carpeta completa)
echo    - %PROJECT_ROOT%unilogo.gif
echo.
echo 6. En "Advanced" - "Hidden Imports": Agrega:
echo    - tkinter
echo    - sqlite3
echo    - PIL
echo    - tkcalendar
echo    - hashlib
echo.
echo 7. Click en "CONVERT .PY TO .EXE"
echo.
echo 8. Espera a que termine (puede tomar 5-10 minutos)
echo.
echo 9. El ejecutable estara en: output\SistemaInventario_UNISON
echo.
pause

REM Lanzar auto-py-to-exe
"%PYTHON_EXE%" -m auto_py_to_exe

echo.
echo [PASO 3/3] Creando carpeta de distribucion...
echo.

REM Crear carpeta Release si existe el ejecutable
if exist "%PROJECT_ROOT%output" (
    echo Copiando archivos a Release...
    
    if not exist "%PROJECT_ROOT%Release" mkdir "%PROJECT_ROOT%Release"
    
    REM Copiar todo el contenido de output a Release
    xcopy /E /I /Y "%PROJECT_ROOT%output\*" "%PROJECT_ROOT%Release\" >nul
    
    REM Asegurar que la base de datos este en la carpeta correcta
    if exist "%PROJECT_ROOT%database" (
        xcopy /E /I /Y "%PROJECT_ROOT%database" "%PROJECT_ROOT%Release\database" >nul
    )
    
    echo.
    echo [OK] Archivos copiados a Release\
    echo.
    
    REM Crear archivo LEEME
    (
    echo SISTEMA DE INVENTARIO - UNIVERSIDAD DE SONORA
    echo ===========================================
    echo.
    echo INSTRUCCIONES:
    echo.
    echo 1. Ejecuta el archivo .exe dentro de esta carpeta
    echo 2. NO muevas el .exe fuera de esta carpeta
    echo 3. La base de datos esta en la subcarpeta "database"
    echo.
    echo CREDENCIALES:
    echo   Usuario: Admin       Password: admin23
    echo   Usuario: productos   Password: producto19
    echo   Usuario: almacen     Password: almacen11
    echo.
    echo Desarrollado por: Manuel Munguia Rubio
    echo Universidad de Sonora - 2025
    ) > "%PROJECT_ROOT%Release\LEEME.txt"
    
    echo ====================================================
    echo   COMPILACION COMPLETADA
    echo ====================================================
    echo.
    echo El ejecutable esta en: Release\
    echo.
    echo IMPORTANTE: Distribuye TODA la carpeta Release
    echo.
    
    REM Abrir carpeta Release
    start explorer "%PROJECT_ROOT%Release"
) else (
    echo.
    echo [INFO] No se encontro la carpeta output
    echo Esto es normal si cerraste auto-py-to-exe sin compilar
    echo.
)

pause
exit /b 0
