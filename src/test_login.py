import tkinter as tk
from tkinter import messagebox
import os
import sys

# Añadir el directorio src al path para importar los módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.database import DatabaseModel
from views.login_view_simple import LoginViewSimple

class LoginControllerTest:
    def __init__(self):
        print("=== INICIANDO LoginControllerTest ===")
        
        # Crear la ventana principal para el login
        self.login_root = tk.Tk()
        print("Ventana principal de login creada")
        
        # Inicializar el modelo de base de datos
        self.model = DatabaseModel()
        print("Modelo de base de datos inicializado")
        
        # Variable para almacenar información del usuario logueado
        self.current_user = None
        
        # Crear la vista de login simple
        print("Creando vista de login simple...")
        self.login_view = LoginViewSimple(self.login_root)
        print("Vista de login simple creada")
        
        # Configurar el comando del botón de login
        self.setup_login_commands()
        print("Comandos de login configurados")
    
    def setup_login_commands(self):
        """Configura los comandos para la interfaz de login"""
        self.login_view.login_button.config(command=self.handle_login)
        print("Comando del botón configurado")
    
    def handle_login(self):
        """Maneja el proceso de login"""
        print("=== PROCESANDO LOGIN ===")
        
        # Obtener credenciales del formulario
        credentials = self.login_view.get_credentials()
        username = credentials['usuario']
        password = credentials['password']
        
        print(f"Usuario ingresado: '{username}'")
        print(f"Contraseña ingresada: {'*' * len(password)}")
        
        # Validar que se hayan ingresado ambos campos
        if not username or not password:
            self.login_view.show_error("Por favor ingrese usuario y contraseña")
            return
        
        # Verificar credenciales en la base de datos
        user_data = self.model.verificar_usuario(username, password)
        
        if user_data:
            # Login exitoso
            self.current_user = user_data
            print(f"Login exitoso para: {user_data['nombre_completo']}")
            
            # Mostrar mensaje de bienvenida
            welcome_message = f"¡Bienvenido {user_data['nombre_completo']}!"
            self.login_view.show_success(welcome_message)
            
            # Por ahora solo cerraremos la ventana
            self.login_root.quit()
        else:
            # Login fallido
            print("Login fallido - credenciales incorrectas")
            self.login_view.show_error("Usuario o contraseña incorrectos")
            self.login_view.clear_form()
    
    def run(self):
        """Ejecuta la aplicación de login"""
        print("=== INICIANDO APLICACIÓN DE LOGIN TEST ===")
        
        # Configurar el cierre de la aplicación
        self.login_root.protocol("WM_DELETE_WINDOW", self.on_login_close)
        
        print("Mostrando ventana de login...")
        # Asegurar que la ventana esté visible
        self.login_root.deiconify()
        self.login_root.lift()
        self.login_root.focus_force()
        
        print("Iniciando loop principal...")
        # Iniciar el loop principal
        self.login_root.mainloop()
        print("Loop principal terminado")
    
    def on_login_close(self):
        """Maneja el cierre de la ventana de login"""
        print("Cerrando aplicación de login")
        self.login_root.quit()
        self.login_root.destroy()

def main():
    """Función principal para ejecutar la aplicación de prueba"""
    print("=== INICIANDO APLICACIÓN CON LOGIN TEST ===")
    try:
        # Crear y ejecutar el controlador de login
        print("Creando LoginControllerTest...")
        login_controller = LoginControllerTest()
        print("LoginControllerTest creado exitosamente")
        
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