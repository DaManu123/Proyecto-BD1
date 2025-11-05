"""
Sistema de Inventario - Universidad de Sonora
Aplicación principal con login integrado en la misma ventana

Este punto de entrada muestra primero una pantalla de login y luego,
sin cerrar la ventana, cambia a la vista principal del sistema.

Autor: Manuel Munguia Rubio
Curso: Bases de Datos 1
"""

from tkinter import Tk
from controllers.integrated_controller import IntegratedController

def main():
    """Función principal que inicia la aplicación con login integrado"""
    # Crear la ventana principal
    root = Tk()
    
    # Crear el controlador integrado que maneja login y aplicación principal
    app = IntegratedController(root)
    
    # Iniciar el loop principal
    root.mainloop()

if __name__ == "__main__":
    main()