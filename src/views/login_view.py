import tkinter as tk
from tkinter import ttk, Frame, Label, Button, Entry, messagebox
import os

class LoginView:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de Inventario - Login")
        self.master.geometry("450x400")
        self.master.configure(bg="#2c3e50")
        self.master.resizable(False, False)
        
        # Forzar que la ventana aparezca al frente
        self.master.lift()
        self.master.attributes('-topmost', True)
        self.master.focus_force()
        
        # Centrar la ventana en la pantalla
        self.center_window()
        
        # Quitar el topmost después de centrar
        self.master.attributes('-topmost', False)
        
        # Intentar establecer el icono de la ventana con el logo
        try:
            logo_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'unilogo.gif')
            if os.path.exists(logo_path):
                icon = tk.PhotoImage(file=logo_path)
                self.master.iconphoto(True, icon)
        except Exception as e:
            print(f"No se pudo establecer el icono: {e}")
        
        # Variable para mantener la referencia del logo
        self.logo_image = None
        
        # Crear la interfaz de login
        self.create_login_interface()
    
    def center_window(self):
        """Centra la ventana en la pantalla"""
        self.master.update_idletasks()
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        x = (self.master.winfo_screenwidth() // 2) - (width // 2)
        y = (self.master.winfo_screenheight() // 2) - (height // 2)
        self.master.geometry(f"{width}x{height}+{x}+{y}")
    
    def create_login_interface(self):
        """Crea la interfaz de login"""
        # Frame principal
        main_frame = Frame(self.master, bg="#2c3e50")
        main_frame.pack(expand=True, fill="both", padx=30, pady=30)
        
        # Logo de la Universidad (por ahora solo placeholder)
        logo_placeholder = Label(main_frame, text="UNISON", 
                               font=("Arial", 20, "bold"), 
                               bg="#2c3e50", fg="white")
        logo_placeholder.pack(pady=(10, 15))
        
        # Título del sistema
        title_label = Label(main_frame, text="Sistema de Inventario", 
                           font=("Arial", 18, "bold"), 
                           bg="#2c3e50", fg="white")
        title_label.pack(pady=(0, 5))
        
        # Subtítulo
        subtitle_label = Label(main_frame, text="Universidad de Sonora", 
                              font=("Arial", 12, "italic"), 
                              bg="#2c3e50", fg="#bdc3c7")
        subtitle_label.pack(pady=(0, 30))
        
        # Frame para el formulario de login
        form_frame = Frame(main_frame, bg="#34495e", relief="raised", bd=2)
        form_frame.pack(pady=20, padx=20, fill="x")
        
        # Título del formulario
        form_title = Label(form_frame, text="Iniciar Sesión", 
                          font=("Arial", 14, "bold"), 
                          bg="#34495e", fg="white")
        form_title.pack(pady=(15, 20))
        
        # Campo de usuario
        user_label = Label(form_frame, text="Usuario:", 
                          font=("Arial", 11, "bold"), 
                          bg="#34495e", fg="white")
        user_label.pack(anchor="w", padx=20, pady=(0, 5))
        
        self.user_entry = Entry(form_frame, width=30, font=("Arial", 11), 
                               relief="solid", bd=1)
        self.user_entry.pack(padx=20, pady=(0, 15))
        
        # Campo de contraseña
        password_label = Label(form_frame, text="Contraseña:", 
                              font=("Arial", 11, "bold"), 
                              bg="#34495e", fg="white")
        password_label.pack(anchor="w", padx=20, pady=(0, 5))
        
        self.password_entry = Entry(form_frame, width=30, font=("Arial", 11), 
                                   show="*", relief="solid", bd=1)
        self.password_entry.pack(padx=20, pady=(0, 20))
        
        # Botón de login
        self.login_button = Button(form_frame, text="Iniciar Sesión", 
                                  font=("Arial", 12, "bold"), 
                                  bg="#27ae60", fg="white",
                                  width=20, height=2, 
                                  relief="raised", cursor="hand2", 
                                  borderwidth=2)
        self.login_button.pack(pady=(0, 20))
        
        # Efectos hover para el botón
        def on_enter(e):
            self.login_button.config(bg="#229954")
        def on_leave(e):
            self.login_button.config(bg="#27ae60")
            
        self.login_button.bind("<Enter>", on_enter)
        self.login_button.bind("<Leave>", on_leave)
        
        # Información adicional
        info_label = Label(main_frame, text="Ingrese sus credenciales para acceder al sistema", 
                          font=("Arial", 10), 
                          bg="#2c3e50", fg="#95a5a6")
        info_label.pack(pady=(10, 0))
        
        # Bind Enter key para hacer login
        self.master.bind('<Return>', lambda event: self.login_button.invoke())
        
        # Focus inicial en el campo de usuario
        self.user_entry.focus()
    
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
    
    def show_error(self, message):
        """Muestra un mensaje de error"""
        messagebox.showerror("Error de Autenticación", message)
    
    def show_success(self, message):
        """Muestra un mensaje de éxito"""
        messagebox.showinfo("Login Exitoso", message)