"""
Vista de login con diseño UNISON - Lado izquierdo formulario, lado derecho icono
"""

import tkinter as tk
from tkinter import messagebox
from utils.theme_unison import (
    COLOR_AZUL_UNISON, COLOR_AZUL_UNISON_OSCURO, COLOR_DORADO_UNISON,
    COLOR_TEXTO_BLANCO, COLOR_TEXTO_NEGRO, COLOR_FONDO_BLANCO,
    FUENTE_UNISON, TAMAÑO_FUENTE_TITULO, TAMAÑO_FUENTE_NORMAL, TAMAÑO_FUENTE_BOTON,
    crear_boton_unison, crear_entry_unison, crear_label_unison, crear_frame_unison
)

class LoginViewUnisonSplit:
    def __init__(self, root, login_callback=None):
        self.root = root
        self.login_callback = login_callback
        
        # Configurar ventana principal
        self.root.configure(bg=COLOR_FONDO_BLANCO)
        
        # Frame principal que ocupa toda la ventana
        self.main_frame = tk.Frame(root, bg=COLOR_FONDO_BLANCO)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=0, pady=0)
        
        self.create_login_interface()
    
    def create_login_interface(self):
        """Crea la interfaz de login con diseño split"""
        
        # LADO IZQUIERDO - Formulario de login
        left_frame = tk.Frame(self.main_frame, bg=COLOR_FONDO_BLANCO, width=400)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=40, pady=60)
        left_frame.pack_propagate(False)
        
        # Título del login
        titulo = tk.Label(
            left_frame,
            text="Iniciar Sesión",
            font=(FUENTE_UNISON, 24, "bold"),
            fg=COLOR_AZUL_UNISON,
            bg=COLOR_FONDO_BLANCO
        )
        titulo.pack(pady=(0, 40))
        
        # Subtítulo
        subtitulo = tk.Label(
            left_frame,
            text="Sistema de Inventario UNISON",
            font=(FUENTE_UNISON, 12),
            fg=COLOR_TEXTO_NEGRO,
            bg=COLOR_FONDO_BLANCO
        )
        subtitulo.pack(pady=(0, 60))
        
        # Campo Usuario
        usuario_label = tk.Label(
            left_frame,
            text="Usuario:",
            font=(FUENTE_UNISON, TAMAÑO_FUENTE_NORMAL, "bold"),
            fg=COLOR_TEXTO_NEGRO,
            bg=COLOR_FONDO_BLANCO
        )
        usuario_label.pack(anchor='w', pady=(0, 8))
        
        self.entry_usuario = tk.Entry(
            left_frame,
            font=(FUENTE_UNISON, TAMAÑO_FUENTE_NORMAL),
            relief='solid',
            bd=2,
            highlightcolor=COLOR_AZUL_UNISON,
            highlightbackground='#cccccc',
            insertbackground=COLOR_AZUL_UNISON,
            width=25
        )
        self.entry_usuario.pack(fill='x', pady=(0, 30), ipady=8)
        
        # Campo Contraseña
        password_label = tk.Label(
            left_frame,
            text="Contraseña:",
            font=(FUENTE_UNISON, TAMAÑO_FUENTE_NORMAL, "bold"),
            fg=COLOR_TEXTO_NEGRO,
            bg=COLOR_FONDO_BLANCO
        )
        password_label.pack(anchor='w', pady=(0, 8))
        
        self.entry_password = tk.Entry(
            left_frame,
            font=(FUENTE_UNISON, TAMAÑO_FUENTE_NORMAL),
            relief='solid',
            bd=2,
            highlightcolor=COLOR_AZUL_UNISON,
            highlightbackground='#cccccc',
            insertbackground=COLOR_AZUL_UNISON,
            show='*',
            width=25
        )
        self.entry_password.pack(fill='x', pady=(0, 40), ipady=8)
        
        # Botón de login con bordes redondeados (simulado)
        self.btn_login = tk.Button(
            left_frame,
            text="Iniciar Sesión",
            font=(FUENTE_UNISON, TAMAÑO_FUENTE_BOTON, "bold"),
            bg=COLOR_AZUL_UNISON,
            fg=COLOR_TEXTO_BLANCO,
            relief='flat',
            borderwidth=0,
            cursor='hand2',
            command=self.handle_login,
            pady=12,
            padx=30
        )
        self.btn_login.pack(fill='x', pady=(0, 20), ipady=4)
        
        # Efectos hover para el botón
        def on_enter(e):
            self.btn_login.config(bg=COLOR_AZUL_UNISON_OSCURO)
        
        def on_leave(e):
            self.btn_login.config(bg=COLOR_AZUL_UNISON)
        
        self.btn_login.bind('<Enter>', on_enter)
        self.btn_login.bind('<Leave>', on_leave)
        
        # LADO DERECHO - Icono/imagen de usuario
        right_frame = tk.Frame(self.main_frame, bg=COLOR_AZUL_UNISON, width=400)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        right_frame.pack_propagate(False)
        
        # Contenedor para centrar el icono
        icon_container = tk.Frame(right_frame, bg=COLOR_AZUL_UNISON)
        icon_container.pack(expand=True, fill=tk.BOTH)
        
        # Icono de usuario (usando texto como placeholder)
        user_icon = tk.Label(
            icon_container,
            text="👤",
            font=(FUENTE_UNISON, 120),
            fg=COLOR_TEXTO_BLANCO,
            bg=COLOR_AZUL_UNISON
        )
        user_icon.pack(expand=True)
        
        # Texto debajo del icono
        welcome_text = tk.Label(
            icon_container,
            text="Bienvenido al\\nSistema de Inventario\\nUNISON",
            font=(FUENTE_UNISON, 16, "bold"),
            fg=COLOR_TEXTO_BLANCO,
            bg=COLOR_AZUL_UNISON,
            justify='center'
        )
        welcome_text.pack(pady=(0, 100))
        
        # Hacer que los campos respondan a Enter
        self.entry_usuario.bind('<Return>', lambda e: self.entry_password.focus_set())
        self.entry_password.bind('<Return>', lambda e: self.handle_login())
        
        # Focus inicial en el campo usuario
        self.entry_usuario.focus_set()
    
    def handle_login(self):
        """Maneja el evento de login"""
        usuario = self.entry_usuario.get().strip()
        password = self.entry_password.get().strip()
        
        if not usuario or not password:
            messagebox.showerror("Error", "Por favor complete todos los campos")
            return
        
        if self.login_callback:
            # Validar credenciales (el callback se encarga de la validación)
            self.login_callback(usuario, password)
        else:
            messagebox.showinfo("Login", f"Bienvenido {usuario}")
    
    def clear_fields(self):
        """Limpia los campos de entrada"""
        self.entry_usuario.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)
        self.entry_usuario.focus_set()
    
    def destroy(self):
        """Destruye la vista de login"""
        if hasattr(self, 'main_frame'):
            self.main_frame.destroy()