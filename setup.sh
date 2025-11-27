#!/bin/bash
# ====================================================
# Script Maestro de Configuracion - Sistema Inventario
# Universidad de Sonora - Base de Datos I
# Unifica: instalacion, ejecucion, verificacion, configuracion
# Compatible con Linux y macOS
# ====================================================

# Obtener ruta absoluta del directorio del proyecto
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_PATH="$PROJECT_ROOT/.venv"
PYTHON_EXE="$VENV_PATH/bin/python"
VSCODE_DIR="$PROJECT_ROOT/.vscode"
SETTINGS_FILE="$VSCODE_DIR/settings.json"

# Funciones auxiliares
verificar_python() {
    echo "[PASO 1/4] Verificando Python..."
    echo ""
    
    if ! command -v python3 &> /dev/null; then
        echo "[ERROR] Python 3 NO esta instalado"
        echo ""
        echo "Instala Python 3:"
        echo "  Ubuntu/Debian: sudo apt-get install python3 python3-venv python3-pip"
        echo "  Fedora: sudo dnf install python3 python3-pip"
        echo "  macOS: brew install python3"
        echo ""
        return 1
    fi
    
    echo "[OK] Python encontrado"
    python3 --version
    echo ""
    return 0
}

crear_entorno_virtual() {
    echo "[PASO 2/4] Configurando Entorno Virtual..."
    echo ""
    
    if [ -d "$VENV_PATH" ]; then
        echo "[INFO] Ya existe un entorno virtual"
        echo ""
        read -p "Deseas recrearlo? (s/N): " RECREATE
        if [ "$RECREATE" = "s" ] || [ "$RECREATE" = "S" ]; then
            echo ""
            echo "[INFO] Eliminando entorno virtual existente..."
            rm -rf "$VENV_PATH"
            echo "[OK] Entorno eliminado"
        else
            echo "[INFO] Usando entorno virtual existente"
            echo ""
            return 0
        fi
    fi
    
    echo "[INFO] Creando entorno virtual en .venv/..."
    python3 -m venv "$VENV_PATH"
    
    if [ $? -ne 0 ]; then
        echo "[ERROR] No se pudo crear el entorno virtual"
        echo ""
        echo "Verifica que tienes python3-venv instalado:"
        echo "  Ubuntu/Debian: sudo apt-get install python3-venv"
        return 1
    fi
    
    echo "[OK] Entorno virtual creado"
    echo ""
    return 0
}

instalar_dependencias() {
    echo "[PASO 3/4] Instalando Dependencias..."
    echo ""
    
    echo "[INFO] Actualizando pip..."
    "$PYTHON_EXE" -m pip install --upgrade pip --quiet
    
    echo "[INFO] Instalando paquetes desde requirements.txt..."
    "$PYTHON_EXE" -m pip install -r "$PROJECT_ROOT/requirements.txt"
    
    if [ $? -ne 0 ]; then
        echo "[ERROR] Hubo problemas al instalar dependencias"
        echo ""
        return 1
    fi
    
    echo "[OK] Dependencias instaladas"
    echo ""
    return 0
}

configurar_vscode() {
    echo "[PASO 4/4] Configurando VS Code..."
    echo ""
    
    if [ ! -d "$VSCODE_DIR" ]; then
        echo "[INFO] Creando directorio .vscode/..."
        mkdir -p "$VSCODE_DIR"
    fi
    
    echo "[INFO] Generando settings.json portable..."
    
    cat > "$SETTINGS_FILE" << 'EOF'
{
    "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
    "python.analysis.extraPaths": [
        "${workspaceFolder}/src",
        "${workspaceFolder}/src/utils"
    ],
    "python.terminal.activateEnvironment": true,
    "python.terminal.activateEnvInCurrentTerminal": true,
    
    // Configuracion de Code Runner - Portable usando variables de VS Code
    "code-runner.executorMap": {
        "python": "export PYTHONPATH='${workspaceFolder}/src' && '${workspaceFolder}/.venv/bin/python' -u $fullFileName"
    },
    "code-runner.runInTerminal": true,
    "code-runner.clearPreviousOutput": true,
    "code-runner.saveFileBeforeRun": true,
    "code-runner.fileDirectoryAsCwd": false
}
EOF
    
    echo "[OK] VS Code configurado con rutas portables"
    echo ""
    return 0
}

verificar_modulos() {
    echo ""
    echo "Verificando modulos requeridos:"
    echo ""
    
    "$PYTHON_EXE" -c "import tkcalendar; print('  [OK] tkcalendar version:', tkcalendar.__version__)" 2>/dev/null || echo "  [ERROR] tkcalendar NO instalado"
    
    "$PYTHON_EXE" -c "import PIL; print('  [OK] Pillow version:', PIL.__version__)" 2>/dev/null || echo "  [ERROR] Pillow NO instalado"
    
    "$PYTHON_EXE" -c "import tkinter; print('  [OK] tkinter disponible')" 2>/dev/null || echo "  [WARN] tkinter NO disponible - Instala: sudo apt-get install python3-tk"
    
    "$PYTHON_EXE" -c "import sqlite3; print('  [OK] sqlite3 version:', sqlite3.sqlite_version)" 2>/dev/null || echo "  [ERROR] sqlite3 NO disponible"
}

# Menu principal
menu() {
    while true; do
        clear
        echo ""
        echo "===================================================="
        echo "   SISTEMA DE INVENTARIO - UNISON"
        echo "   Configuracion y Administracion"
        echo "===================================================="
        echo ""
        echo "   MENU PRINCIPAL:"
        echo ""
        echo "   1) Instalacion Completa (Primera Vez)"
        echo "   2) Ejecutar Aplicacion"
        echo "   3) Verificar Entorno"
        echo "   4) Reconfigurar VS Code"
        echo "   5) Reinstalar Dependencias"
        echo "   6) Salir"
        echo ""
        echo "===================================================="
        echo ""
        
        read -p "Selecciona una opcion (1-6): " OPCION
        
        case $OPCION in
            1) instalacion_completa ;;
            2) ejecutar_app ;;
            3) verificar_entorno ;;
            4) reconfigurar_vscode ;;
            5) reinstalar_deps ;;
            6) salir ;;
            *) 
                echo ""
                echo "[ERROR] Opcion invalida. Intenta de nuevo."
                sleep 2
                ;;
        esac
    done
}

instalacion_completa() {
    clear
    echo ""
    echo "===================================================="
    echo "   INSTALACION COMPLETA"
    echo "===================================================="
    echo ""
    
    verificar_python || {
        echo ""
        echo "[!] Instalacion cancelada: Python no encontrado"
        read -p "Presiona Enter para continuar..."
        return
    }
    
    crear_entorno_virtual || {
        echo ""
        echo "[!] Instalacion cancelada: Error creando entorno virtual"
        read -p "Presiona Enter para continuar..."
        return
    }
    
    instalar_dependencias || {
        echo ""
        echo "[!] Instalacion cancelada: Error instalando dependencias"
        read -p "Presiona Enter para continuar..."
        return
    }
    
    configurar_vscode
    verificar_modulos
    
    echo ""
    echo "===================================================="
    echo "   INSTALACION COMPLETADA EXITOSAMENTE"
    echo "===================================================="
    echo ""
    echo "El proyecto esta listo para usarse."
    echo ""
    echo "PROXIMOS PASOS:"
    echo "  - Ejecutar aplicacion: Selecciona opcion 2 del menu"
    echo "  - Desde VS Code: Abre el proyecto y presiona F5"
    echo "  - Code Runner: Abre main.py y presiona el boton Run"
    echo ""
    echo "CREDENCIALES DE ACCESO:"
    echo "  Admin      / admin23      (Acceso completo)"
    echo "  productos  / producto19   (Solo productos)"
    echo "  almacen    / almacen11    (Solo almacenes)"
    echo ""
    read -p "Presiona Enter para continuar..."
}

ejecutar_app() {
    clear
    echo ""
    echo "===================================================="
    echo "   EJECUTAR APLICACION"
    echo "===================================================="
    echo ""
    
    if [ ! -f "$PYTHON_EXE" ]; then
        echo "[ERROR] Entorno virtual no encontrado."
        echo ""
        echo "Ejecuta primero la opcion 1: Instalacion Completa"
        echo ""
        read -p "Presiona Enter para continuar..."
        return
    fi
    
    echo "[INFO] Iniciando Sistema de Inventario..."
    echo ""
    
    "$PYTHON_EXE" "$PROJECT_ROOT/src/main.py"
    
    if [ $? -ne 0 ]; then
        echo ""
        echo "[ERROR] La aplicacion termino con errores."
        echo ""
        echo "Intenta ejecutar la opcion 3: Verificar Entorno"
        echo ""
        read -p "Presiona Enter para continuar..."
    fi
}

verificar_entorno() {
    clear
    echo ""
    echo "===================================================="
    echo "   VERIFICACION DEL ENTORNO"
    echo "===================================================="
    echo ""
    
    if [ ! -f "$PYTHON_EXE" ]; then
        echo "[ERROR] Entorno virtual no encontrado."
        echo "Ruta esperada: $PYTHON_EXE"
        echo ""
        echo "Ejecuta la opcion 1: Instalacion Completa"
        echo ""
        read -p "Presiona Enter para continuar..."
        return
    fi
    
    echo "[1/4] Informacion del Proyecto"
    echo "  Directorio: $PROJECT_ROOT"
    echo "  Python: $PYTHON_EXE"
    echo ""
    
    echo "[2/4] Version de Python"
    "$PYTHON_EXE" --version
    echo ""
    
    echo "[3/4] Paquetes Instalados"
    "$PYTHON_EXE" -m pip list --format=columns
    echo ""
    
    echo "[4/4] Verificacion de Modulos Requeridos"
    verificar_modulos
    
    echo ""
    echo "===================================================="
    echo "   VERIFICACION COMPLETADA"
    echo "===================================================="
    echo ""
    read -p "Presiona Enter para continuar..."
}

reconfigurar_vscode() {
    clear
    echo ""
    echo "===================================================="
    echo "   RECONFIGURAR VS CODE"
    echo "===================================================="
    echo ""
    
    configurar_vscode
    
    echo ""
    echo "[OK] Configuracion de VS Code actualizada"
    echo ""
    echo "Reinicia VS Code para aplicar los cambios:"
    echo "  - Presiona Ctrl+Shift+P (Cmd+Shift+P en macOS)"
    echo "  - Escribe: Developer: Reload Window"
    echo "  - Presiona Enter"
    echo ""
    read -p "Presiona Enter para continuar..."
}

reinstalar_deps() {
    clear
    echo ""
    echo "===================================================="
    echo "   REINSTALAR DEPENDENCIAS"
    echo "===================================================="
    echo ""
    
    if [ ! -f "$PYTHON_EXE" ]; then
        echo "[ERROR] Entorno virtual no encontrado."
        echo ""
        echo "Ejecuta primero la opcion 1: Instalacion Completa"
        echo ""
        read -p "Presiona Enter para continuar..."
        return
    fi
    
    instalar_dependencias
    
    echo ""
    echo "[OK] Dependencias reinstaladas"
    echo ""
    read -p "Presiona Enter para continuar..."
}

salir() {
    clear
    echo ""
    echo "Gracias por usar el Sistema de Inventario UNISON"
    echo ""
    exit 0
}

# Punto de entrada
menu
