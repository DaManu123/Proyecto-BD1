#!/bin/bash
# Script de instalación y configuración del entorno virtual
# Para el Sistema de Inventario - Base de Datos 1

echo "=================================================="
echo "  Sistema de Inventario - Configuración Inicial"
echo "  Universidad de Sonora - Base de Datos 1"
echo "=================================================="

# Verificar que Python está instalado
echo "🔍 Verificando instalación de Python..."
python --version

if [ $? -ne 0 ]; then
    echo "❌ Error: Python no está instalado o no está en el PATH"
    echo "   Por favor instala Python 3.7+ desde https://python.org"
    exit 1
fi

echo "✅ Python encontrado"

# Crear entorno virtual
echo "📦 Creando entorno virtual..."
python -m venv venv

if [ $? -ne 0 ]; then
    echo "❌ Error al crear el entorno virtual"
    exit 1
fi

echo "✅ Entorno virtual creado en ./venv/"

# Activar entorno virtual (instrucciones)
echo "=================================================="
echo "🚀 Configuración completada!"
echo "=================================================="
echo ""
echo "Para usar la aplicación:"
echo ""
echo "1. Activar entorno virtual:"
echo "   Windows: venv\\Scripts\\activate"
echo "   Linux/Mac: source venv/bin/activate"
echo ""
echo "2. Ejecutar aplicación:"
echo "   python src/main.py"
echo ""
echo "3. Alternativamente, usar scripts automáticos:"
echo "   Windows: run_with_venv.bat"
echo "   PowerShell: .\\activate_venv.ps1"
echo ""
echo "=================================================="
echo "📚 Archivos de ayuda disponibles:"
echo "   - README.md (documentación completa)"
echo "   - VENV_INSTRUCTIONS.md (guía del entorno virtual)"
echo "   - copilot-instructions.md (para desarrolladores)"
echo "=================================================="