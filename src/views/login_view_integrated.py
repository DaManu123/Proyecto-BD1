import tkinter as tk
from tkinter import ttk, Frame, Label, Button, Entry
import os

class LoginViewIntegrated:
    def __init__(self, container):
        """
        Vista de login integrada que funciona como un frame dentro de un contenedor
        """
        self.container = container
        self.frame = Frame(container, bg="#2c3e50")
        
        # Variable para mantener la referencia del logo
        self.logo_image = None
        
        # Callback para manejar el login exitoso
        self.on_login_success = None
        
        # Crear la interfaz de login
        self.create_login_interface()
    
    def create_login_interface(self):
        """Crea la interfaz de login dentro del frame"""
        # Configurar el frame principal
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        
        # Frame central para centrar el contenido
        center_frame = Frame(self.frame, bg="#2c3e50")
        center_frame.grid(row=0, column=0, sticky="")
        
        # Logo simplificado (solo texto)
        logo_placeholder = Label(center_frame, text="UNISON", 
                               font=("Arial", 24, "bold"), 
                               bg="#2c3e50", fg="white")
        logo_placeholder.pack(pady=(30, 20))
        
        # Título del sistema
        title_label = Label(center_frame, text="Sistema de Inventario", 
                           font=("Arial", 20, "bold"), 
                           bg="#2c3e50", fg="white")
        title_label.pack(pady=(0, 8))
        
        # Subtítulo
        subtitle_label = Label(center_frame, text="Universidad de Sonora", 
                              font=("Arial", 14, "italic"), 
                              bg="#2c3e50", fg="#bdc3c7")
        subtitle_label.pack(pady=(0, 40))
        
        # Frame para el formulario de login
        form_frame = Frame(center_frame, bg="#34495e", relief="raised", bd=2)
        form_frame.pack(pady=20, padx=40)
        
        # Título del formulario
        form_title = Label(form_frame, text="Iniciar Sesión", 
                          font=("Arial", 16, "bold"), 
                          bg="#34495e", fg="white")
        form_title.pack(pady=(20, 25))
        
        # Campo de usuario/nombre
        user_label = Label(form_frame, text="Nombre:", 
                          font=("Arial", 12, "bold"), 
                          bg="#34495e", fg="white")
        user_label.pack(anchor="w", padx=25, pady=(0, 8))
        
        self.user_entry = Entry(form_frame, width=35, font=("Arial", 12), 
                               relief="solid", bd=1)
        self.user_entry.pack(padx=25, pady=(0, 20))
        
        # Campo de contraseña
        password_label = Label(form_frame, text="Contraseña:", 
                              font=("Arial", 12, "bold"), 
                              bg="#34495e", fg="white")
        password_label.pack(anchor="w", padx=25, pady=(0, 8))
        
        self.password_entry = Entry(form_frame, width=35, font=("Arial", 12), 
                                   show="*", relief="solid", bd=1)
        self.password_entry.pack(padx=25, pady=(0, 25))
        
        # Botón de login
        self.login_button = Button(form_frame, text="Iniciar Sesión", 
                                  font=("Arial", 14, "bold"), 
                                  bg="#27ae60", fg="white",
                                  width=25, height=2, 
                                  relief="raised", cursor="hand2", 
                                  borderwidth=2,
                                  command=self.handle_login_click)
        self.login_button.pack(pady=(0, 25))
        
        # Efectos hover para el botón
        def on_enter(e):
            self.login_button.config(bg="#229954")
        def on_leave(e):
            self.login_button.config(bg="#27ae60")
            
        self.login_button.bind("<Enter>", on_enter)
        self.login_button.bind("<Leave>", on_leave)
        
        # Información adicional
        info_label = Label(center_frame, 
                          text="Ingrese sus credenciales para acceder al sistema", 
                          font=("Arial", 11), 
                          bg="#2c3e50", fg="#95a5a6")
        info_label.pack(pady=(15, 30))
        
        # Focus inicial en el campo de usuario
        self.user_entry.focus()
    
    def set_login_callback(self, callback):
        """Establece la función callback que se ejecutará al hacer login exitoso"""
        self.on_login_success = callback
    
    def handle_login_click(self):
        """Maneja el clic del botón de login"""
        # Obtener credenciales
        credentials = self.get_credentials()
        
        # Validación básica (por ahora solo verifica que no estén vacíos)
        if not credentials['usuario'] or not credentials['password']:
            # En una implementación real, aquí mostraríamos un mensaje de error
            # Por ahora, simplemente no hacemos nada si están vacíos
            return
        
        # Llamar al callback si está configurado
        if self.on_login_success:
            self.on_login_success(credentials)
    
    def get_credentials(self):
        """Obtiene las credenciales ingresadas"""
        return {
            'usuario': self.user_entry.get().strip(),
            'password': self.password_entry.get()
        }
    
    def clear_form(self):
        """Limpia el formulario de login"""
        self.user_entry.delete(0, 'end')
        self.password_entry.delete(0, 'end')
        self.user_entry.focus()
    
    def show(self):
        """Muestra el frame de login"""
        self.frame.grid(row=0, column=0, sticky="nsew")
    
    def hide(self):
        """Oculta el frame de login"""
        self.frame.grid_remove()
    
    def bind_enter_key(self, root_window):
        """Vincula la tecla Enter para hacer login"""
        root_window.bind('<Return>', lambda event: self.handle_login_click())