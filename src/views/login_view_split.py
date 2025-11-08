"""
Vista de login con diseño UNISON - Lado izquierdo formulario, lado derecho icono
"""

import tkinter as tk
from tkinter import messagebox
from utils.theme_unison import (
    COLOR_AZUL_UNISON, COLOR_AZUL_UNISON_OSCURO, COLOR_DORADO_UNISON, COLOR_DORADO_UNISON_OSCURO,
    COLOR_TEXTO_BLANCO, COLOR_TEXTO_NEGRO, COLOR_FONDO_BLANCO, COLOR_GRIS_CLARO,
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
        """Crea la interfaz de login con diseño split y responsive usando Grid"""
        
        # Configurar grid del main_frame para responsividad
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)
        
        # ============ LADO IZQUIERDO - Formulario de login ============
        left_frame = tk.Frame(self.main_frame, bg=COLOR_FONDO_BLANCO)
        left_frame.grid(row=0, column=0, sticky="nsew", padx=40, pady=60)
        
        # Configurar grid del formulario para centrar contenido
        left_frame.grid_rowconfigure(0, weight=1)
        left_frame.grid_rowconfigure(7, weight=1)
        left_frame.grid_columnconfigure(0, weight=1)
        
        # Frame interno para el formulario centrado
        form_container = tk.Frame(left_frame, bg=COLOR_FONDO_BLANCO)
        form_container.grid(row=1, column=0, rowspan=6, sticky="n", pady=20)
        
        # Título del login
        titulo = tk.Label(
            form_container,
            text="Iniciar Sesión",
            font=(FUENTE_UNISON, 28, "bold"),
            fg=COLOR_AZUL_UNISON,
            bg=COLOR_FONDO_BLANCO
        )
        titulo.grid(row=0, column=0, pady=(0, 15), sticky="ew")
        
        # Subtítulo
        subtitulo = tk.Label(
            form_container,
            text="Sistema de Inventario UNISON",
            font=(FUENTE_UNISON, 13),
            fg=COLOR_TEXTO_NEGRO,
            bg=COLOR_FONDO_BLANCO
        )
        subtitulo.grid(row=1, column=0, pady=(0, 50), sticky="ew")
        
        # Campo Usuario
        usuario_label = tk.Label(
            form_container,
            text="Usuario:",
            font=(FUENTE_UNISON, TAMAÑO_FUENTE_NORMAL + 1, "bold"),
            fg=COLOR_TEXTO_NEGRO,
            bg=COLOR_FONDO_BLANCO,
            anchor='w'
        )
        usuario_label.grid(row=2, column=0, pady=(0, 8), sticky="w")
        
        # Entry de usuario con bordes redondeados mejorados
        self.entry_usuario = tk.Entry(
            form_container,
            font=(FUENTE_UNISON, TAMAÑO_FUENTE_NORMAL),
            relief='flat',
            bd=0,
            highlightthickness=2,
            highlightcolor=COLOR_AZUL_UNISON,
            highlightbackground=COLOR_GRIS_CLARO,
            insertbackground=COLOR_AZUL_UNISON,
            bg=COLOR_FONDO_BLANCO,
            fg=COLOR_TEXTO_NEGRO,
            width=30
        )
        self.entry_usuario.grid(row=3, column=0, pady=(0, 25), ipady=10, sticky="ew")
        
        # Campo Contraseña
        password_label = tk.Label(
            form_container,
            text="Contraseña:",
            font=(FUENTE_UNISON, TAMAÑO_FUENTE_NORMAL + 1, "bold"),
            fg=COLOR_TEXTO_NEGRO,
            bg=COLOR_FONDO_BLANCO,
            anchor='w'
        )
        password_label.grid(row=4, column=0, pady=(0, 8), sticky="w")
        
        # Entry de contraseña con bordes redondeados mejorados
        self.entry_password = tk.Entry(
            form_container,
            font=(FUENTE_UNISON, TAMAÑO_FUENTE_NORMAL),
            relief='flat',
            bd=0,
            highlightthickness=2,
            highlightcolor=COLOR_AZUL_UNISON,
            highlightbackground=COLOR_GRIS_CLARO,
            insertbackground=COLOR_AZUL_UNISON,
            bg=COLOR_FONDO_BLANCO,
            fg=COLOR_TEXTO_NEGRO,
            show='●',
            width=30
        )
        self.entry_password.grid(row=5, column=0, pady=(0, 35), ipady=10, sticky="ew")
        
        # Botón de login con efecto redondeado
        self.btn_login = tk.Button(
            form_container,
            text="INICIAR SESIÓN",
            font=(FUENTE_UNISON, TAMAÑO_FUENTE_BOTON, "bold"),
            bg=COLOR_AZUL_UNISON,
            fg=COLOR_TEXTO_BLANCO,
            activebackground=COLOR_AZUL_UNISON_OSCURO,
            activeforeground=COLOR_TEXTO_BLANCO,
            relief='flat',
            borderwidth=0,
            highlightthickness=0,
            cursor='hand2',
            command=self.handle_login,
            pady=14,
            padx=40
        )
        self.btn_login.grid(row=6, column=0, pady=(0, 15), ipady=2, sticky="ew")
        
        # Efectos hover para el botón
        def on_enter(e):
            self.btn_login.config(bg=COLOR_AZUL_UNISON_OSCURO)
        
        def on_leave(e):
            self.btn_login.config(bg=COLOR_AZUL_UNISON)
        
        self.btn_login.bind('<Enter>', on_enter)
        self.btn_login.bind('<Leave>', on_leave)
        
        # Efectos de focus en los entries
        def on_focus_in_user(e):
            self.entry_usuario.config(highlightbackground=COLOR_AZUL_UNISON)
        
        def on_focus_out_user(e):
            self.entry_usuario.config(highlightbackground=COLOR_GRIS_CLARO)
        
        def on_focus_in_pass(e):
            self.entry_password.config(highlightbackground=COLOR_AZUL_UNISON)
        
        def on_focus_out_pass(e):
            self.entry_password.config(highlightbackground=COLOR_GRIS_CLARO)
        
        self.entry_usuario.bind('<FocusIn>', on_focus_in_user)
        self.entry_usuario.bind('<FocusOut>', on_focus_out_user)
        self.entry_password.bind('<FocusIn>', on_focus_in_pass)
        self.entry_password.bind('<FocusOut>', on_focus_out_pass)
        
        # ============ LADO DERECHO - Icono/imagen de usuario ============
        right_frame = tk.Frame(self.main_frame, bg=COLOR_AZUL_UNISON)
        right_frame.grid(row=0, column=1, sticky="nsew")
        
        # Configurar grid para centrar contenido
        right_frame.grid_rowconfigure(0, weight=1)
        right_frame.grid_rowconfigure(1, weight=2)
        right_frame.grid_rowconfigure(2, weight=1)
        right_frame.grid_columnconfigure(0, weight=1)
        
        # Intentar cargar imagen de usuario, o usar ícono por defecto
        try:
            import os
            icon_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'user_icon.png')
            if os.path.exists(icon_path):
                from PIL import Image, ImageTk
                img = Image.open(icon_path)
                img = img.resize((200, 200), Image.Resampling.LANCZOS)
                self.user_image = ImageTk.PhotoImage(img)
                user_icon = tk.Label(
                    right_frame,
                    image=self.user_image,
                    bg=COLOR_AZUL_UNISON
                )
            else:
                raise FileNotFoundError
        except:
            # Crear círculo dorado con borde usando Canvas
            canvas_icon = tk.Canvas(
                right_frame,
                width=220,
                height=220,
                bg=COLOR_AZUL_UNISON,
                highlightthickness=0
            )
            # Círculo dorado de fondo
            canvas_icon.create_oval(10, 10, 210, 210, fill=COLOR_DORADO_UNISON, outline=COLOR_DORADO_UNISON_OSCURO, width=4)
            # Ícono de usuario (simulado con formas geométricas)
            canvas_icon.create_oval(80, 50, 140, 110, fill=COLOR_AZUL_UNISON_OSCURO, outline="")
            canvas_icon.create_arc(50, 100, 170, 220, start=0, extent=180, fill=COLOR_AZUL_UNISON_OSCURO, outline="")
            user_icon = canvas_icon
        
        user_icon.grid(row=1, column=0, pady=20)
        
        # Texto de bienvenida debajo del icono
        welcome_text = tk.Label(
            right_frame,
            text="Bienvenido al\nSistema de Inventario\nUNISON",
            font=(FUENTE_UNISON, 18, "bold"),
            fg=COLOR_TEXTO_BLANCO,
            bg=COLOR_AZUL_UNISON,
            justify='center'
        )
        welcome_text.grid(row=2, column=0, pady=(0, 40), sticky="n")
        
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