#!/bin/bash
# ====================================================
# Script de Verificacion del Entorno - Sistema Inventario
# Universidad de Sonora - Base de Datos I
# Compatible con Linux y macOS
# ====================================================

echo ""
echo "========================================"
echo "  VERIFICACION DEL ENTORNO PYTHON"
echo "========================================"
echo ""

# Obtener la ruta del directorio actual (donde esta el script)
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_PATH="$PROJECT_ROOT/.venv/bin/python"

echo "[1/5] Verificando ubicacion del proyecto..."
echo "Directorio del proyecto: $PROJECT_ROOT"
echo ""

echo "[2/5] Verificando entorno virtual..."
if [ -f "$VENV_PATH" ]; then
    echo "[OK] Entorno virtual encontrado"
    echo "Ruta: $VENV_PATH"
else
    echo "[ERROR] Entorno virtual NO encontrado"
    echo "Ruta esperada: $VENV_PATH"
    echo ""
    echo "SOLUCION: Ejecuta ./setup.sh para crear el entorno virtual"
    exit 1
fi
echo ""

echo "[3/5] Verificando version de Python..."
"$VENV_PATH" --version
echo ""

echo "[4/5] Verificando dependencias instaladas..."
"$VENV_PATH" -m pip list --format=columns
echo ""

echo "[5/5] Verificando modulos requeridos..."
echo ""

echo "Verificando tkcalendar..."
if "$VENV_PATH" -c "import tkcalendar; print('  [OK] tkcalendar version:', tkcalendar.__version__)" 2>/dev/null; then
    echo "  Importacion exitosa"
else
    echo "  [ERROR] tkcalendar NO instalado"
    echo "  SOLUCION: pip install tkcalendar"
    HAS_ERRORS=1
fi
echo ""

echo "Verificando Pillow..."
if "$VENV_PATH" -c "import PIL; print('  [OK] Pillow version:', PIL.__version__)" 2>/dev/null; then
    echo "  Importacion exitosa"
else
    echo "  [ERROR] Pillow NO instalado"
    echo "  SOLUCION: pip install Pillow"
    HAS_ERRORS=1
fi
echo ""

echo "Verificando tkinter..."
if "$VENV_PATH" -c "import tkinter; print('  [OK] tkinter disponible')" 2>/dev/null; then
    echo "  Importacion exitosa"
else
    echo "  [ERROR] tkinter NO disponible"
    echo "  NOTA: Instala con: sudo apt-get install python3-tk"
    HAS_ERRORS=1
fi
echo ""

echo "Verificando sqlite3..."
if "$VENV_PATH" -c "import sqlite3; print('  [OK] sqlite3 version:', sqlite3.sqlite_version)" 2>/dev/null; then
    echo "  Importacion exitosa"
else
    echo "  [ERROR] sqlite3 NO disponible"
    HAS_ERRORS=1
fi
echo ""

echo "========================================"
echo "  VERIFICACION COMPLETADA"
echo "========================================"
echo ""

if [ -n "$HAS_ERRORS" ]; then
    echo "[!] Algunos modulos tienen errores. Revisa los mensajes anteriores."
    echo ""
    echo "Para instalar dependencias faltantes:"
    echo "  1. Activa el entorno virtual: source .venv/bin/activate"
    echo "  2. Instala dependencias: pip install -r requirements.txt"
else
    echo "[OK] Todos los modulos estan correctamente instalados."
    echo ""
    echo "Para ejecutar la aplicacion:"
    echo "  - Desde terminal: python src/main.py"
    echo "  - Desde VS Code: Presiona F5 o el boton Run"
fi
echo ""
