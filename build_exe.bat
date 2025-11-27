@echo off
REM ====================================================
REM Script de Compilacion a EXE - Sistema Inventario
REM Universidad de Sonora - Base de Datos I
REM Genera ejecutable standalone con PyInstaller
REM ====================================================

setlocal enabledelayedexpansion

REM Obtener ruta absoluta del directorio del proyecto
set "PROJECT_ROOT=%~dp0"
set "VENV_PATH=%PROJECT_ROOT%.venv"
set "PYTHON_EXE=%VENV_PATH%\Scripts\python.exe"
set "SRC_DIR=%PROJECT_ROOT%src"
set "DIST_DIR=%PROJECT_ROOT%dist"
set "BUILD_DIR=%PROJECT_ROOT%build"

cls
echo.
echo ====================================================
echo   COMPILACION A EJECUTABLE (.EXE)
echo   Sistema de Inventario - UNISON
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
"%PYTHON_EXE%" -m pip install pyinstaller --quiet
if errorlevel 1 (
    echo [ERROR] No se pudo instalar PyInstaller
    pause
    exit /b 1
)
echo [OK] PyInstaller instalado
echo.

echo [PASO 2/5] Limpiando compilaciones anteriores...
echo.
if exist "%DIST_DIR%" rmdir /s /q "%DIST_DIR%"
if exist "%BUILD_DIR%" rmdir /s /q "%BUILD_DIR%"
if exist "%PROJECT_ROOT%*.spec" del /q "%PROJECT_ROOT%*.spec"
echo [OK] Limpieza completada
echo.

echo [PASO 3/5] Copiando recursos necesarios...
echo.
REM Crear directorio temporal para recursos
if not exist "%PROJECT_ROOT%temp_resources" mkdir "%PROJECT_ROOT%temp_resources"
if exist "%PROJECT_ROOT%unilogo.gif" copy "%PROJECT_ROOT%unilogo.gif" "%PROJECT_ROOT%temp_resources\" >nul
if exist "%PROJECT_ROOT%database" xcopy /E /I /Y "%PROJECT_ROOT%database" "%PROJECT_ROOT%temp_resources\database" >nul
echo [OK] Recursos copiados
echo.

echo [PASO 4/5] Compilando aplicacion...
echo.
echo [INFO] Esto puede tomar varios minutos...
echo.

REM Compilar con PyInstaller
"%PYTHON_EXE%" -m PyInstaller ^
    --name="SistemaInventario_UNISON" ^
    --onefile ^
    --windowed ^
    --icon="%PROJECT_ROOT%unilogo.gif" ^
    --add-data="%PROJECT_ROOT%unilogo.gif;." ^
    --add-data="%PROJECT_ROOT%database;database" ^
    --hidden-import=PIL ^
    --hidden-import=PIL._tkinter_finder ^
    --hidden-import=tkcalendar ^
    --hidden-import=sqlite3 ^
    --hidden-import=tkinter ^
    --collect-all=tkcalendar ^
    --collect-all=babel ^
    --noconfirm ^
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

echo [PASO 5/5] Organizando archivos finales...
echo.

REM Crear directorio de distribucion
if not exist "%PROJECT_ROOT%Release" mkdir "%PROJECT_ROOT%Release"

REM Copiar ejecutable
if exist "%DIST_DIR%\SistemaInventario_UNISON.exe" (
    copy "%DIST_DIR%\SistemaInventario_UNISON.exe" "%PROJECT_ROOT%Release\" >nul
)

REM Copiar base de datos
if exist "%PROJECT_ROOT%database" (
    xcopy /E /I /Y "%PROJECT_ROOT%database" "%PROJECT_ROOT%Release\database" >nul
)

REM Copiar logo
if exist "%PROJECT_ROOT%unilogo.gif" (
    copy "%PROJECT_ROOT%unilogo.gif" "%PROJECT_ROOT%Release\" >nul
)

REM Crear README para el ejecutable
(
echo SISTEMA DE INVENTARIO - UNIVERSIDAD DE SONORA
echo ===========================================
echo.
echo INSTRUCCIONES DE USO:
echo.
echo 1. Ejecuta SistemaInventario_UNISON.exe
echo 2. Usa las credenciales de acceso:
echo.
echo    Usuario: Admin       Password: admin23
echo    Usuario: productos   Password: producto19
echo    Usuario: almacen     Password: almacen11
echo.
echo NOTAS IMPORTANTES:
echo.
echo - La base de datos se encuentra en la carpeta "database"
echo - El archivo unilogo.gif debe estar en la misma carpeta que el .exe
echo - No requiere instalacion de Python
echo - Compatible con Windows 7, 8, 10, 11
echo.
echo Desarrollado por: Manuel Munguia Rubio
echo Universidad de Sonora - Base de Datos I - 2025
) > "%PROJECT_ROOT%Release\LEEME.txt"

REM Limpiar archivos temporales
if exist "%PROJECT_ROOT%temp_resources" rmdir /s /q "%PROJECT_ROOT%temp_resources"
if exist "%BUILD_DIR%" rmdir /s /q "%BUILD_DIR%"
if exist "%PROJECT_ROOT%*.spec" del /q "%PROJECT_ROOT%*.spec"

echo [OK] Organizacion completada
echo.

echo ====================================================
echo   COMPILACION COMPLETADA EXITOSAMENTE
echo ====================================================
echo.
echo El ejecutable se encuentra en: Release\SistemaInventario_UNISON.exe
echo.
echo CONTENIDO DE LA CARPETA RELEASE:
echo   - SistemaInventario_UNISON.exe  (Aplicacion principal)
echo   - database\                     (Base de datos)
echo   - unilogo.gif                   (Logo UNISON)
echo   - LEEME.txt                     (Instrucciones)
echo.
echo Puedes distribuir toda la carpeta "Release" a otros usuarios.
echo.
echo TAMANO APROXIMADO: ~50-80 MB
echo.
pause

REM Abrir carpeta Release
start explorer "%PROJECT_ROOT%Release"

exit /b 0
