#!/bin/bash
# ====================================================
# Script de Instalacion - Sistema de Inventario
# Universidad de Sonora - Base de Datos I
# Compatible con Linux y macOS
# ====================================================

echo ""
echo "================================================"
echo "   INSTALACION - Sistema de Inventario UNISON"
echo "================================================"
echo ""
echo "Este script configurara el entorno para ejecutar"
echo "la aplicacion en cualquier equipo."
echo ""
read -p "Presiona Enter para continuar..."

echo ""
echo "[PASO 1/4] Verificando Python..."
echo ""

# Verificar que Python esta instalado
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python 3 NO esta instalado"
    echo ""
    echo "Por favor instala Python 3:"
    echo "  Ubuntu/Debian: sudo apt-get install python3 python3-venv python3-pip"
    echo "  Fedora: sudo dnf install python3 python3-pip"
    echo "  macOS: brew install python3"
    echo ""
    exit 1
fi

echo "[OK] Python encontrado"
python3 --version
echo ""

echo "[PASO 2/4] Creando entorno virtual..."
echo ""

# Verificar si ya existe el entorno virtual
if [ -d ".venv" ]; then
    echo "[!] Ya existe un entorno virtual en .venv/"
    echo ""
    read -p "Deseas recrearlo? (s/N): " RECREATE
    if [ "$RECREATE" = "s" ] || [ "$RECREATE" = "S" ]; then
        echo ""
        echo "[INFO] Eliminando entorno virtual existente..."
        rm -rf .venv
        echo "[OK] Entorno virtual eliminado"
    else
        echo ""
        echo "[INFO] Usando entorno virtual existente"
        # Saltar a instalacion de dependencias
        SKIP_VENV=1
    fi
fi

if [ -z "$SKIP_VENV" ]; then
    echo "[INFO] Creando nuevo entorno virtual en .venv/..."
    python3 -m venv .venv

    if [ $? -ne 0 ]; then
        echo "[ERROR] No se pudo crear el entorno virtual"
        echo ""
        echo "Verifica que tienes python3-venv instalado:"
        echo "  Ubuntu/Debian: sudo apt-get install python3-venv"
        exit 1
    fi

    echo "[OK] Entorno virtual creado exitosamente"
    echo ""
fi

echo "[PASO 3/4] Instalando dependencias..."
echo ""

# Activar entorno virtual e instalar dependencias
source .venv/bin/activate

echo "[INFO] Actualizando pip..."
python -m pip install --upgrade pip --quiet

echo "[INFO] Instalando dependencias desde requirements.txt..."
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "[ERROR] Hubo un problema al instalar las dependencias"
    echo ""
    echo "Intenta manualmente:"
    echo "  1. source .venv/bin/activate"
    echo "  2. pip install -r requirements.txt"
    exit 1
fi

echo "[OK] Dependencias instaladas correctamente"
echo ""

echo "[PASO 4/4] Verificando instalacion..."
echo ""

# Verificar modulos criticos
echo "Verificando modulos requeridos:"
echo ""

python -c "import tkcalendar; print('  [OK] tkcalendar version:', tkcalendar.__version__)" 2>/dev/null || echo "  [ERROR] tkcalendar NO instalado"
python -c "import PIL; print('  [OK] Pillow version:', PIL.__version__)" 2>/dev/null || echo "  [ERROR] Pillow NO instalado"
python -c "import tkinter; print('  [OK] tkinter disponible')" 2>/dev/null || echo "  [WARN] tkinter NO disponible - Instala: sudo apt-get install python3-tk"
python -c "import sqlite3; print('  [OK] sqlite3 version:', sqlite3.sqlite_version)" 2>/dev/null || echo "  [ERROR] sqlite3 NO disponible"

echo ""
echo "================================================"
echo "   INSTALACION COMPLETADA"
echo "================================================"
echo ""
echo "El entorno esta listo para usar!"
echo ""
echo "PROXIMOS PASOS:"
echo ""
echo "1. Para verificar la instalacion:"
echo "   ./verificar_entorno.sh"
echo ""
echo "2. Para ejecutar la aplicacion:"
echo ""
echo "   Opcion A - Terminal:"
echo "     source .venv/bin/activate"
echo "     python src/main.py"
echo ""
echo "   Opcion B - VS Code:"
echo "     1. Abre el proyecto en VS Code"
echo "     2. Selecciona el interprete: .venv/bin/python"
echo "     3. Presiona F5 o el boton Run"
echo ""
echo "   Opcion C - PyCharm/Otras IDEs:"
echo "     1. Configura el interprete de Python a: .venv/bin/python"
echo "     2. Ejecuta: src/main.py"
echo ""
echo "CREDENCIALES DE ACCESO:"
echo "  Usuario: Admin      Password: admin23      (Acceso completo)"
echo "  Usuario: productos  Password: producto19   (Solo productos)"
echo "  Usuario: almacen    Password: almacen11    (Solo almacenes)"
echo ""
echo "================================================"
echo ""
