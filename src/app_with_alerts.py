import tkinter as tk
from tkinter import messagebox
import sys
import os
import winsound

# Añadir el directorio al path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from controllers.login_controller import LoginController

def main():
    """Función principal con alertas visuales y sonoras"""
    print("=== INICIANDO APLICACIÓN CON LOGIN ===")
    
    # Mensaje de alerta antes de abrir
    try:
        # Sonido de Windows
        winsound.MessageBeep()
    except:
        pass
    
    # Crear una ventana temporal para mostrar un mensaje
    temp_root = tk.Tk()
    temp_root.withdraw()  # Ocultar la ventana principal
    
    messagebox.showinfo("Sistema de Inventario", 
                       "Se va a abrir la pantalla de login.\n\n"
                       "Si no la ves, revisa:\n"
                       "• La barra de tareas\n"
                       "• Otros monitores\n"
                       "• Alt+Tab para cambiar ventanas")
    
    temp_root.destroy()
    
    try:
        # Crear y ejecutar el controlador de login
        print("Creando LoginController...")
        login_controller = LoginController()
        print("LoginController creado exitosamente")
        
        # Sonido adicional cuando se abre
        try:
            winsound.MessageBeep()
        except:
            pass
        
        print("Ejecutando aplicación...")
        login_controller.run()
        print("Aplicación finalizada")
    except KeyboardInterrupt:
        print("\nAplicación cerrada por el usuario")
    except Exception as e:
        print(f"Error al iniciar la aplicación: {e}")
        import traceback
        traceback.print_exc()
        messagebox.showerror("Error Fatal", f"No se pudo iniciar la aplicación: {str(e)}")

if __name__ == "__main__":
    main()