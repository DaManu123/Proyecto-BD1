@echo off
REM ====================================================
REM Script Maestro de Configuracion - Sistema Inventario
REM Universidad de Sonora - Base de Datos I
REM Unifica: instalacion, ejecucion, verificacion, configuracion
REM ====================================================

setlocal enabledelayedexpansion

REM Obtener ruta absoluta del directorio del proyecto
set "PROJECT_ROOT=%~dp0"
set "VENV_PATH=%PROJECT_ROOT%.venv"
set "PYTHON_EXE=%VENV_PATH%\Scripts\python.exe"
set "VSCODE_DIR=%PROJECT_ROOT%.vscode"
set "SETTINGS_FILE=%VSCODE_DIR%\settings.json"

:MENU
cls
echo.
echo ====================================================
echo   SISTEMA DE INVENTARIO - UNISON
echo   Configuracion y Administracion
echo ====================================================
echo.
echo   MENU PRINCIPAL:
echo.
echo   1) Instalacion Completa (Primera Vez)
echo   2) Ejecutar Aplicacion
echo   3) Verificar Entorno
echo   4) Configurar VS Code
echo   5) Salir
echo.
echo ====================================================
echo.

set /p "OPCION=Selecciona una opcion (1-5): "

if "%OPCION%"=="1" goto INSTALACION_COMPLETA
if "%OPCION%"=="2" goto EJECUTAR_APP
if "%OPCION%"=="3" goto VERIFICAR_ENTORNO
if "%OPCION%"=="4" goto CONFIGURAR_VSCODE
if "%OPCION%"=="5" goto SALIR

echo.
echo [ERROR] Opcion invalida. Intenta de nuevo.
timeout /t 2 >nul
goto MENU

REM ====================================================
REM INSTALACION COMPLETA
REM ====================================================
:INSTALACION_COMPLETA
cls
echo.
echo ====================================================
echo   INSTALACION COMPLETA
echo ====================================================
echo.

call :VERIFICAR_PYTHON
if errorlevel 1 goto ERROR_PYTHON

call :CREAR_ENTORNO_VIRTUAL
if errorlevel 1 goto ERROR_VENV

call :INSTALAR_DEPENDENCIAS
if errorlevel 1 goto ERROR_DEPS

call :CONFIGURAR_VSCODE_FUNC
call :VERIFICAR_MODULOS

echo.
echo ====================================================
echo   INSTALACION COMPLETADA EXITOSAMENTE
echo ====================================================
echo.
echo El proyecto esta listo para usarse.
echo.
echo PROXIMOS PASOS:
echo   - Ejecutar aplicacion: Selecciona opcion 2 del menu
echo   - Desde VS Code: Abre el proyecto y presiona F5
echo   - Code Runner: Abre main.py y presiona el boton Run
echo.
echo CREDENCIALES DE ACCESO:
echo   Admin      / admin23      (Acceso completo)
echo   productos  / producto19   (Solo productos)
echo   almacen    / almacen11    (Solo almacenes)
echo.
pause
goto MENU

REM ====================================================
REM EJECUTAR APLICACION
REM ====================================================
:EJECUTAR_APP
cls
echo.
echo ====================================================
echo   EJECUTAR APLICACION
echo ====================================================
echo.

if not exist "%PYTHON_EXE%" (
    echo [ERROR] Entorno virtual no encontrado.
    echo.
    echo Ejecuta primero la opcion 1: Instalacion Completa
    echo.
    pause
    goto MENU
)

echo [INFO] Iniciando Sistema de Inventario...
echo.

"%PYTHON_EXE%" "%PROJECT_ROOT%src\main.py"

if errorlevel 1 (
    echo.
    echo [ERROR] La aplicacion termino con errores.
    echo.
    echo Intenta ejecutar la opcion 3: Verificar Entorno
    echo.
    pause
)

goto MENU

REM ====================================================
REM VERIFICAR ENTORNO
REM ====================================================
:VERIFICAR_ENTORNO
cls
echo.
echo ====================================================
echo   VERIFICACION DEL ENTORNO
echo ====================================================
echo.

if not exist "%PYTHON_EXE%" (
    echo [ERROR] Entorno virtual no encontrado.
    echo Ruta esperada: %PYTHON_EXE%
    echo.
    echo Ejecuta la opcion 1: Instalacion Completa
    echo.
    pause
    goto MENU
)

echo [1/4] Informacion del Proyecto
echo   Directorio: %PROJECT_ROOT%
echo   Python: %PYTHON_EXE%
echo.

echo [2/4] Version de Python
"%PYTHON_EXE%" --version
echo.

echo [3/4] Paquetes Instalados
"%PYTHON_EXE%" -m pip list --format=columns
echo.

echo [4/4] Verificacion de Modulos Requeridos
call :VERIFICAR_MODULOS

echo.
echo ====================================================
echo   VERIFICACION COMPLETADA
echo ====================================================
echo.
pause
goto MENU

REM ====================================================
REM CONFIGURAR VS CODE
REM ====================================================
:CONFIGURAR_VSCODE
cls
echo.
echo ====================================================
echo   CONFIGURAR VS CODE
echo ====================================================
echo.

if not exist "%PYTHON_EXE%" (
    echo [ERROR] Entorno virtual no encontrado.
    echo.
    echo Ejecuta primero la opcion 1: Instalacion Completa
    echo.
    pause
    goto MENU
)

call :CONFIGURAR_VSCODE_FUNC

echo.
echo [OK] Configuracion de VS Code actualizada
echo.
echo CONFIGURACIONES APLICADAS:
echo   - Entorno virtual: .venv
echo   - Code Runner configurado
echo   - Debugger configurado
echo   - PYTHONPATH automatico
echo.
echo Reinicia VS Code para aplicar los cambios:
echo   - Presiona Ctrl+Shift+P
echo   - Escribe: Developer: Reload Window
echo   - Presiona Enter
echo.
pause
goto MENU

REM ====================================================
REM FUNCIONES AUXILIARES
REM ====================================================

:VERIFICAR_PYTHON
echo [PASO 1/4] Verificando Python...
echo.

python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python NO esta instalado o no esta en el PATH.
    echo.
    echo Descarga Python desde: https://www.python.org/downloads/
    echo Durante la instalacion, marca "Add Python to PATH"
    echo.
    exit /b 1
)

echo [OK] Python encontrado
python --version
echo.
exit /b 0

:CREAR_ENTORNO_VIRTUAL
echo [PASO 2/4] Configurando Entorno Virtual...
echo.

if exist "%VENV_PATH%\" (
    echo [INFO] Ya existe un entorno virtual
    echo.
    set /p "RECREATE=Deseas recrearlo? (S/N): "
    if /i "!RECREATE!"=="S" (
        echo.
        echo [INFO] Eliminando entorno virtual existente...
        rmdir /s /q "%VENV_PATH%"
        echo [OK] Entorno eliminado
    ) else (
        echo [INFO] Usando entorno virtual existente
        echo.
        exit /b 0
    )
)

echo [INFO] Creando entorno virtual en .venv\...
python -m venv "%VENV_PATH%"

if errorlevel 1 (
    echo [ERROR] No se pudo crear el entorno virtual
    echo.
    exit /b 1
)

echo [OK] Entorno virtual creado
echo.
exit /b 0

:INSTALAR_DEPENDENCIAS
echo [PASO 3/4] Instalando Dependencias...
echo.

echo [INFO] Actualizando pip...
"%PYTHON_EXE%" -m pip install --upgrade pip --quiet

echo [INFO] Instalando paquetes desde requirements.txt...
"%PYTHON_EXE%" -m pip install -r "%PROJECT_ROOT%requirements.txt"

if errorlevel 1 (
    echo [ERROR] Hubo problemas al instalar dependencias
    echo.
    exit /b 1
)

echo [OK] Dependencias instaladas
echo.
exit /b 0

:CONFIGURAR_VSCODE_FUNC
echo [PASO 4/4] Configurando VS Code...
echo.

if not exist "%VSCODE_DIR%" (
    echo [INFO] Creando directorio .vscode\...
    mkdir "%VSCODE_DIR%"
)

echo [INFO] Generando settings.json...
REM Crear settings.json con configuracion funcional
(
echo {
echo     "python.defaultInterpreterPath": "${workspaceFolder}/.venv/Scripts/python.exe",
echo     "python.analysis.extraPaths": [
echo         "${workspaceFolder}/src",
echo         "${workspaceFolder}/src/utils"
echo     ],
echo     "python.terminal.activateEnvironment": true,
echo     "python.terminal.activateEnvInCurrentTerminal": true,
echo.    
echo     // Configuracion de Code Runner - Compatible con Run Python File
echo     "code-runner.executorMap": {
echo         "python": "^& \"${workspaceFolder}/.venv/Scripts/python.exe\" \"$fullFileName\""
echo     },
echo     "code-runner.runInTerminal": true,
echo     "code-runner.clearPreviousOutput": true,
echo     "code-runner.saveFileBeforeRun": true,
echo     "code-runner.fileDirectoryAsCwd": false,
echo.    
echo     // Configuracion adicional para ejecucion de Python
echo     "python.envFile": "${workspaceFolder}/.env",
echo     "terminal.integrated.env.windows": {
echo         "PYTHONPATH": "${workspaceFolder}/src"
echo     },
echo     "terminal.integrated.defaultProfile.windows": "PowerShell"
echo }
) > "%SETTINGS_FILE%"

echo [INFO] Generando launch.json...
REM Crear launch.json para debugging
(
echo {
echo     "version": "0.2.0",
echo     "configurations": [
echo         {
echo             "name": "Python: Main Application",
echo             "type": "debugpy",
echo             "request": "launch",
echo             "program": "${workspaceFolder}/src/main.py",
echo             "console": "integratedTerminal",
echo             "cwd": "${workspaceFolder}",
echo             "env": {
echo                 "PYTHONPATH": "${workspaceFolder}/src"
echo             },
echo             "justMyCode": true
echo         },
echo         {
echo             "name": "Python: Current File",
echo             "type": "debugpy",
echo             "request": "launch",
echo             "program": "${file}",
echo             "console": "integratedTerminal",
echo             "cwd": "${workspaceFolder}",
echo             "env": {
echo                 "PYTHONPATH": "${workspaceFolder}/src"
echo             },
echo             "justMyCode": true
echo         }
echo     ]
echo }
) > "%VSCODE_DIR%\launch.json"

echo [OK] VS Code configurado correctamente
echo.
exit /b 0

:VERIFICAR_MODULOS
echo.
echo Verificando modulos requeridos:
echo.

"%PYTHON_EXE%" -c "import tkcalendar; print('  [OK] tkcalendar version:', tkcalendar.__version__)" 2>nul || echo   [ERROR] tkcalendar NO instalado

"%PYTHON_EXE%" -c "import PIL; print('  [OK] Pillow version:', PIL.__version__)" 2>nul || echo   [ERROR] Pillow NO instalado

"%PYTHON_EXE%" -c "import tkinter; print('  [OK] tkinter disponible')" 2>nul || echo   [WARN] tkinter NO disponible

"%PYTHON_EXE%" -c "import sqlite3; print('  [OK] sqlite3 version:', sqlite3.sqlite_version)" 2>nul || echo   [ERROR] sqlite3 NO disponible

exit /b 0

REM ====================================================
REM MANEJO DE ERRORES
REM ====================================================

:ERROR_PYTHON
echo.
echo [!] Instalacion cancelada: Python no encontrado
pause
goto MENU

:ERROR_VENV
echo.
echo [!] Instalacion cancelada: Error creando entorno virtual
pause
goto MENU

:ERROR_DEPS
echo.
echo [!] Instalacion cancelada: Error instalando dependencias
pause
goto MENU

:SALIR
cls
echo.
echo Gracias por usar el Sistema de Inventario UNISON
echo.
exit /b 0
