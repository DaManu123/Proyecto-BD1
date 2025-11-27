@echo off
REM ====================================================
REM Script AUTOMATICO de Compilacion - Sistema Inventario
REM Universidad de Sonora
REM Metodo: PyInstaller con configuracion probada
REM ====================================================

setlocal enabledelayedexpansion

set "PROJECT_ROOT=%~dp0"
set "VENV_PATH=%PROJECT_ROOT%.venv"
set "PYTHON_EXE=%VENV_PATH%\Scripts\python.exe"
set "SRC_DIR=%PROJECT_ROOT%src"
set "DIST_DIR=%PROJECT_ROOT%dist"
set "BUILD_DIR=%PROJECT_ROOT%build"

cls
echo.
echo ====================================================
echo   COMPILACION AUTOMATICA A EJECUTABLE
echo   Sistema de Inventario UNISON
echo ====================================================
echo.

REM Verificar entorno virtual
if not exist "%PYTHON_EXE%" (
    echo [ERROR] Entorno virtual no encontrado.
    echo.
    echo Ejecuta primero: setup.bat - Opcion 1
    echo.
    pause
    exit /b 1
)

echo [PASO 1/5] Instalando PyInstaller...
echo.
"%PYTHON_EXE%" -m pip install pyinstaller --quiet --upgrade
if errorlevel 1 (
    echo [ERROR] No se pudo instalar PyInstaller
    pause
    exit /b 1
)
echo [OK] PyInstaller instalado/actualizado
echo.

echo [PASO 2/5] Limpiando compilaciones anteriores...
echo.
if exist "%DIST_DIR%" rmdir /s /q "%DIST_DIR%"
if exist "%BUILD_DIR%" rmdir /s /q "%BUILD_DIR%"
if exist "%PROJECT_ROOT%Release" rmdir /s /q "%PROJECT_ROOT%Release"
echo [OK] Limpieza completada
echo.

echo [PASO 3/5] Compilando aplicacion...
echo.
echo [INFO] Esto puede tomar 5-10 minutos, por favor espera...
echo.

REM Compilar con PyInstaller - Configuracion probada y funcional
"%PYTHON_EXE%" -m PyInstaller ^
    --name=SistemaInventario_UNISON ^
    --onedir ^
    --windowed ^
    --noupx ^
    --clean ^
    --noconfirm ^
    --add-data="%PROJECT_ROOT%database;database" ^
    --add-data="%PROJECT_ROOT%unilogo.gif;." ^
    --hidden-import=tkinter ^
    --hidden-import=tkinter.ttk ^
    --hidden-import=tkinter.messagebox ^
    --hidden-import=sqlite3 ^
    --hidden-import=PIL ^
    --hidden-import=PIL._tkinter_finder ^
    --hidden-import=tkcalendar ^
    --hidden-import=babel.numbers ^
    --collect-all=tkcalendar ^
    --collect-all=babel ^
    --copy-metadata=tkcalendar ^
    --copy-metadata=babel ^
    --recursive-copy-metadata=tkcalendar ^
    --recursive-copy-metadata=babel ^
    "%SRC_DIR%\main.py"

if errorlevel 1 (
    echo.
    echo [ERROR] La compilacion fallo
    echo.
    pause
    exit /b 1
)

echo.
echo [OK] Compilacion exitosa
echo.

echo [PASO 4/5] Organizando archivos para distribucion...
echo.

REM Crear carpeta Release
if not exist "%PROJECT_ROOT%Release" mkdir "%PROJECT_ROOT%Release"

REM Copiar ejecutable completo
if exist "%DIST_DIR%\SistemaInventario_UNISON" (
    xcopy /E /I /Y "%DIST_DIR%\SistemaInventario_UNISON" "%PROJECT_ROOT%Release\SistemaInventario_UNISON" >nul
)

REM Asegurar que la base de datos este presente
if exist "%PROJECT_ROOT%database" (
    xcopy /E /I /Y "%PROJECT_ROOT%database" "%PROJECT_ROOT%Release\SistemaInventario_UNISON\database" >nul
)

REM Copiar logo a la raiz del ejecutable
if exist "%PROJECT_ROOT%unilogo.gif" (
    copy "%PROJECT_ROOT%unilogo.gif" "%PROJECT_ROOT%Release\SistemaInventario_UNISON\" >nul
)

REM Crear README
(
echo ============================================
echo  SISTEMA DE INVENTARIO - UNISON
echo ============================================
echo.
echo COMO EJECUTAR:
echo.
echo 1. Abre la carpeta "SistemaInventario_UNISON"
echo 2. Ejecuta SistemaInventario_UNISON.exe
echo 3. NO muevas el .exe fuera de su carpeta
echo.
echo CREDENCIALES DE ACCESO:
echo.
echo   Usuario: Admin       Password: admin23   ^(Acceso total^)
echo   Usuario: productos   Password: producto19 ^(Solo productos^)
echo   Usuario: almacen     Password: almacen11  ^(Solo almacenes^)
echo.
echo IMPORTANTE:
echo - Todos los archivos en la carpeta son necesarios
echo - La base de datos esta en: database\InventarioBD_2.db
echo - Compatible con Windows 7/8/10/11
echo.
echo Desarrollado por: Manuel Munguia Rubio
echo Universidad de Sonora - Base de Datos I - 2025
echo ============================================
) > "%PROJECT_ROOT%Release\LEEME.txt"

echo [OK] Archivos organizados
echo.

echo [PASO 5/5] Limpiando archivos temporales...
echo.
if exist "%BUILD_DIR%" rmdir /s /q "%BUILD_DIR%"
if exist "%PROJECT_ROOT%*.spec" del /q "%PROJECT_ROOT%*.spec"
echo [OK] Limpieza completada
echo.

echo ====================================================
echo   COMPILACION COMPLETADA EXITOSAMENTE
echo ====================================================
echo.
echo UBICACION DEL EJECUTABLE:
echo   %PROJECT_ROOT%Release\SistemaInventario_UNISON\
echo.
echo COMO DISTRIBUIR:
echo   1. Comprime la carpeta "Release" en un ZIP
echo   2. Envia el ZIP completo a los usuarios
echo   3. Los usuarios descomprimen y ejecutan el .exe
echo.
echo IMPORTANTE:
echo   - NO muevas solo el .exe, distribuye toda la carpeta
echo   - Tamano aproximado: 100-150 MB
echo.

REM Abrir carpeta Release
start explorer "%PROJECT_ROOT%Release"

pause
exit /b 0
