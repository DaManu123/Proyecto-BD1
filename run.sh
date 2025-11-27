#!/bin/bash
# ====================================================
# Script de Ejecucion - Sistema de Inventario
# Universidad de Sonora - Base de Datos I
# Compatible con Linux y macOS
# ====================================================

echo ""
echo "================================================"
echo "   Sistema de Inventario - Universidad de Sonora"
echo "================================================"
echo ""

# Verificar si existe el entorno virtual
if [ ! -f ".venv/bin/python" ]; then
    echo "[ERROR] Entorno virtual no encontrado"
    echo ""
    echo "Primero debes ejecutar ./setup.sh para configurar el proyecto"
    echo ""
    exit 1
fi

echo "[INFO] Iniciando aplicacion..."
echo ""

# Ejecutar la aplicacion con el entorno virtual
.venv/bin/python src/main.py

if [ $? -ne 0 ]; then
    echo ""
    echo "[ERROR] La aplicacion termino con errores"
    echo ""
    exit 1
fi

echo ""
echo "[INFO] Aplicacion cerrada"
