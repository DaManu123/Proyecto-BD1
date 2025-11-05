import tkinter as tk
from tkinter import messagebox
import os
import sys

# Añadir el directorio src al path para importar los módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.database import DatabaseModel
from views.login_view import LoginView
from views.main_view import MainView
from controllers.main_controller import MainController

class LoginController:
    def __init__(self):
        print("Iniciando LoginController...")
        
        # Crear la ventana principal para el login
        self.login_root = tk.Tk()
        print("Ventana principal de login creada")
        
        # Inicializar el modelo de base de datos
        self.model = DatabaseModel()
        print("Modelo de base de datos inicializado")
        
        # Variable para almacenar información del usuario logueado
        self.current_user = None
        
        # Crear la vista de login
        self.login_view = LoginView(self.login_root)
        print("Vista de login creada")
        
        # Configurar el comando del botón de login
        self.setup_login_commands()
        print("Comandos de login configurados")
    
    def setup_login_commands(self):
        """Configura los comandos para la interfaz de login"""
        self.login_view.login_button.config(command=self.handle_login)
    
    def handle_login(self):
        """Maneja el proceso de login"""
        # Obtener credenciales del formulario
        credentials = self.login_view.get_credentials()
        username = credentials['usuario']
        password = credentials['password']
        
        # Validar que se hayan ingresado ambos campos
        if not username or not password:
            self.login_view.show_error("Por favor ingrese usuario y contraseña")
            return
        
        # Verificar credenciales en la base de datos
        user_data = self.model.verificar_usuario(username, password)
        
        if user_data:
            # Login exitoso
            self.current_user = user_data
            
            # Actualizar último inicio de sesión
            self.model.actualizar_ultimo_inicio_sesion(user_data['id'])
            
            # Mostrar mensaje de bienvenida
            welcome_message = f"¡Bienvenido {user_data['nombre_completo']}!"
            self.login_view.show_success(welcome_message)
            
            # Abrir la aplicación principal
            self.open_main_application()
        else:
            # Login fallido
            self.login_view.show_error("Usuario o contraseña incorrectos")
            self.login_view.clear_form()
    
    def open_main_application(self):
        """Abre la aplicación principal y cierra la ventana de login"""
        try:
            # Ocultar la ventana de login
            self.login_root.withdraw()
            
            # Crear nueva ventana para la aplicación principal
            main_root = tk.Toplevel(self.login_root)
            main_root.title("Sistema de Inventario - Universidad de Sonora")
            main_root.geometry("1000x700")
            main_root.state('zoomed')  # Maximizar en Windows
            
            # Crear el controlador principal
            main_controller = MainController(main_root, user_context=self.current_user)
            
            # Configurar el cierre de la aplicación principal
            def on_main_close():
                main_root.destroy()
                self.login_root.destroy()
            
            main_root.protocol("WM_DELETE_WINDOW", on_main_close)
            
            # Configurar para que al cerrar la ventana principal también se cierre login
            def on_main_destroy(event):
                if event.widget == main_root:
                    self.login_root.quit()
            
            main_root.bind("<Destroy>", on_main_destroy)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al abrir la aplicación principal: {str(e)}")
            # Si hay error, mostrar la ventana de login nuevamente
            self.login_root.deiconify()
    
    def get_current_user(self):
        """Retorna la información del usuario actual"""
        return self.current_user
    
    def run(self):
        """Ejecuta la aplicación de login"""
        print("Iniciando aplicación de login...")
        
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
        self.login_root.quit()
        self.login_root.destroy()

def main():
    """Función principal para ejecutar la aplicación"""
    print("=== INICIANDO APLICACIÓN CON LOGIN ===")
    try:
        # Crear y ejecutar el controlador de login
        print("Creando LoginController...")
        login_controller = LoginController()
        print("LoginController creado exitosamente")
        
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