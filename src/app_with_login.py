"""
Sistema de Inventario - Universidad de Sonora
Aplicación principal con autenticación de usuarios

Este es el punto de entrada principal de la aplicación que incluye
un sistema de login antes de acceder al sistema de inventario.

Autor: Manuel Munguia Rubio
Curso: Bases de Datos 1
"""

import sys
import os

# Añadir el directorio actual al path para importar módulos
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Importar el controlador de login
from controllers.login_controller import LoginController

def main():
    """Función principal de la aplicación"""
    try:
        # Crear y ejecutar la aplicación con login
        app = LoginController()
        app.run()
    except KeyboardInterrupt:
        print("\nAplicación cerrada por el usuario")
    except Exception as e:
        print(f"Error fatal en la aplicación: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()