# Script de compilación a EXE para Linux/macOS
# Nota: Genera ejecutables específicos del sistema operativo

PROJECT_ROOT="$(cd "$(dirname "$0")" && pwd)"
VENV_PATH="$PROJECT_ROOT/.venv"
PYTHON_EXE="$VENV_PATH/bin/python"
SRC_DIR="$PROJECT_ROOT/src"
DIST_DIR="$PROJECT_ROOT/dist"
BUILD_DIR="$PROJECT_ROOT/build"

clear
echo "===================================================="
echo "  COMPILACIÓN A EJECUTABLE"
echo "  Sistema de Inventario - UNISON"
echo "===================================================="
echo ""

# Verificar entorno virtual
if [ ! -f "$PYTHON_EXE" ]; then
    echo "[ERROR] Entorno virtual no encontrado."
    echo ""
    echo "Ejecuta primero: ./setup.sh - Opción 1"
    echo ""
    read -p "Presiona Enter para continuar..."
    exit 1
fi

echo "[PASO 1/5] Instalando PyInstaller..."
echo ""
"$PYTHON_EXE" -m pip install pyinstaller --quiet
if [ $? -ne 0 ]; then
    echo "[ERROR] No se pudo instalar PyInstaller"
    read -p "Presiona Enter para continuar..."
    exit 1
fi
echo "[OK] PyInstaller instalado"
echo ""

echo "[PASO 2/5] Limpiando compilaciones anteriores..."
echo ""
rm -rf "$DIST_DIR" "$BUILD_DIR" "$PROJECT_ROOT"/*.spec
echo "[OK] Limpieza completada"
echo ""

echo "[PASO 3/5] Preparando recursos..."
echo ""
mkdir -p "$PROJECT_ROOT/temp_resources"
[ -f "$PROJECT_ROOT/unilogo.gif" ] && cp "$PROJECT_ROOT/unilogo.gif" "$PROJECT_ROOT/temp_resources/"
[ -d "$PROJECT_ROOT/database" ] && cp -r "$PROJECT_ROOT/database" "$PROJECT_ROOT/temp_resources/"
echo "[OK] Recursos preparados"
echo ""

echo "[PASO 4/5] Compilando aplicación..."
echo ""
echo "[INFO] Esto puede tomar varios minutos..."
echo ""

"$PYTHON_EXE" -m PyInstaller \
    --name="SistemaInventario_UNISON" \
    --onefile \
    --windowed \
    --add-data="$PROJECT_ROOT/unilogo.gif:." \
    --add-data="$PROJECT_ROOT/database:database" \
    --hidden-import=PIL \
    --hidden-import=PIL._tkinter_finder \
    --hidden-import=tkcalendar \
    --hidden-import=sqlite3 \
    --hidden-import=tkinter \
    --collect-all=tkcalendar \
    --collect-all=babel \
    --noconfirm \
    "$SRC_DIR/main.py"

if [ $? -ne 0 ]; then
    echo ""
    echo "[ERROR] La compilación falló"
    echo ""
    read -p "Presiona Enter para continuar..."
    exit 1
fi

echo ""
echo "[OK] Compilación exitosa"
echo ""

echo "[PASO 5/5] Organizando archivos finales..."
echo ""

mkdir -p "$PROJECT_ROOT/Release"

# Copiar ejecutable
if [ -f "$DIST_DIR/SistemaInventario_UNISON" ]; then
    cp "$DIST_DIR/SistemaInventario_UNISON" "$PROJECT_ROOT/Release/"
    chmod +x "$PROJECT_ROOT/Release/SistemaInventario_UNISON"
fi

# Copiar recursos
[ -d "$PROJECT_ROOT/database" ] && cp -r "$PROJECT_ROOT/database" "$PROJECT_ROOT/Release/"
[ -f "$PROJECT_ROOT/unilogo.gif" ] && cp "$PROJECT_ROOT/unilogo.gif" "$PROJECT_ROOT/Release/"

# Crear README
cat > "$PROJECT_ROOT/Release/LEEME.txt" << EOF
SISTEMA DE INVENTARIO - UNIVERSIDAD DE SONORA
===========================================

INSTRUCCIONES DE USO:

1. Ejecuta ./SistemaInventario_UNISON
2. Usa las credenciales de acceso:

   Usuario: Admin       Password: admin23
   Usuario: productos   Password: producto19
   Usuario: almacen     Password: almacen11

NOTAS IMPORTANTES:

- La base de datos se encuentra en la carpeta "database"
- El archivo unilogo.gif debe estar en la misma carpeta
- Compatible con el sistema operativo actual
- No requiere instalación de Python

Desarrollado por: Manuel Munguía Rubio
Universidad de Sonora - Base de Datos I - 2025
EOF

# Limpiar
rm -rf "$PROJECT_ROOT/temp_resources" "$BUILD_DIR" "$PROJECT_ROOT"/*.spec

echo "[OK] Organización completada"
echo ""

echo "===================================================="
echo "  COMPILACIÓN COMPLETADA EXITOSAMENTE"
echo "===================================================="
echo ""
echo "El ejecutable se encuentra en: Release/SistemaInventario_UNISON"
echo ""
echo "CONTENIDO DE LA CARPETA RELEASE:"
echo "  - SistemaInventario_UNISON     (Aplicación principal)"
echo "  - database/                    (Base de datos)"
echo "  - unilogo.gif                  (Logo UNISON)"
echo "  - LEEME.txt                    (Instrucciones)"
echo ""
echo "Puedes distribuir toda la carpeta 'Release' a otros usuarios."
echo ""
read -p "Presiona Enter para continuar..."

exit 0
