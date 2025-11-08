import tkinter as tk
from tkinter import Frame, Label, Button, Entry, Canvas
import os
import sys

# Añadir el directorio utils al path para importar el tema - Ruta absoluta
current_dir = os.path.dirname(os.path.abspath(__file__))
utils_path = os.path.join(current_dir, '..', 'utils')
if utils_path not in sys.path:
    sys.path.insert(0, utils_path)
from theme_unison import *

class LoginViewUnisonDesign:
    def __init__(self, container):
        """
        Vista de login rediseñada con split-screen y tema UNISON
        """
        self.container = container
        self.frame = Frame(container, bg=COLOR_FONDO_NEUTRAL)
        
        # Callback para manejar el login exitoso
        self.on_login_success = None
        
        # Crear la interfaz de login con diseño dividido
        self.create_split_screen_interface()
    
    def create_split_screen_interface(self):
        """Crea la interfaz de login con diseño dividido (split-screen)"""
        # Configurar el frame principal
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)
        
        # === COLUMNA IZQUIERDA (Formulario) ===
        self.columna_izquierda = crear_frame_unison(self.frame, azul=True)
        self.columna_izquierda.grid(row=0, column=0, sticky="nsew")
        self.columna_izquierda.grid_rowconfigure(0, weight=1)
        self.columna_izquierda.grid_columnconfigure(0, weight=1)
        
        # Container para centrar el formulario verticalmente
        form_container = crear_frame_unison(self.columna_izquierda, azul=True)
        form_container.grid(row=0, column=0, sticky="")
        
        # Título principal
        titulo_label = crear_label_unison(
            form_container, 
            "Sistema de Inventario",
            sobre_azul=True,
            font=(FUENTE_PRINCIPAL, TAMAÑO_FUENTE_TITULO + 4, "bold")
        )
        titulo_label.pack(pady=(30, 10))
        
        # Subtítulo
        subtitulo_label = crear_label_unison(
            form_container,
            "Universidad de Sonora",
            sobre_azul=True,
            font=(FUENTE_PRINCIPAL, TAMAÑO_FUENTE_NORMAL, "italic")
        )
        subtitulo_label.pack(pady=(0, 40))
        
        # === FORMULARIO DE LOGIN ===
        
        # Label Usuario
        usuario_label = crear_label_unison(
            form_container,
            "Usuario:",
            sobre_azul=True,
            font=(FUENTE_PRINCIPAL, TAMAÑO_FUENTE_NORMAL, "bold")
        )
        usuario_label.pack(anchor="w", padx=(20, 0), pady=(0, 8))
        
        # Entry Usuario
        self.user_entry = crear_entry_unison(
            form_container,
            width=25,
            bg=COLOR_FONDO_NEUTRAL,
            fg=COLOR_TEXTO_SECUNDARIO
        )
        self.user_entry.pack(padx=20, pady=(0, ESPACIADO_ELEMENTOS))
        
        # Label Contraseña
        password_label = crear_label_unison(
            form_container,
            "Contraseña:",
            sobre_azul=True,
            font=(FUENTE_PRINCIPAL, TAMAÑO_FUENTE_NORMAL, "bold")
        )
        password_label.pack(anchor="w", padx=(20, 0), pady=(0, 8))
        
        # Entry Contraseña
        self.password_entry = crear_entry_unison(
            form_container,
            show="*",
            width=25,
            bg=COLOR_FONDO_NEUTRAL,
            fg=COLOR_TEXTO_SECUNDARIO
        )
        self.password_entry.pack(padx=20, pady=(0, 30))
        
        # Botón Iniciar Sesión
        self.login_button = crear_boton_unison(
            form_container,
            "Iniciar Sesión",
            comando=self.handle_login_click,
            estilo="dorado",
            width=20,
            height=2
        )
        self.login_button.pack(pady=(0, 40))
        
        # === COLUMNA DERECHA (Visual) ===
        self.columna_derecha = crear_frame_unison(self.frame, azul=False)
        self.columna_derecha.grid(row=0, column=1, sticky="nsew")
        self.columna_derecha.grid_rowconfigure(0, weight=1)
        self.columna_derecha.grid_columnconfigure(0, weight=1)
        
        # Container para centrar el contenido visual
        visual_container = crear_frame_unison(self.columna_derecha, azul=False)
        visual_container.grid(row=0, column=0, sticky="")
        
        # Crear el placeholder de usuario (círculo con texto "USER")
        self.create_user_placeholder(visual_container)
        
        # Texto informativo
        info_label = crear_label_unison(
            visual_container,
            "Bienvenido al Sistema\\nde Inventario UNISON",
            font=(FUENTE_PRINCIPAL, TAMAÑO_FUENTE_TITULO, "bold"),
            fg=COLOR_AZUL_PRINCIPAL,
            justify="center"
        )
        info_label.pack(pady=(30, 20))
        
        # Información adicional
        detalle_label = crear_label_unison(
            visual_container,
            "Ingrese sus credenciales\\npara acceder al sistema",
            font=(FUENTE_PRINCIPAL, TAMAÑO_FUENTE_NORMAL),
            fg=COLOR_GRIS_TEXTO,
            justify="center"
        )
        detalle_label.pack()
        
        # Focus inicial en el campo de usuario
        self.user_entry.focus()
    
    def create_user_placeholder(self, parent):
        """Crea un placeholder visual de usuario (círculo con texto USER)"""
        # Canvas para dibujar el círculo
        canvas = Canvas(
            parent,
            width=120,
            height=120,
            bg=COLOR_FONDO_NEUTRAL,
            highlightthickness=0
        )
        canvas.pack(pady=40)
        
        # Dibujar círculo de fondo
        canvas.create_oval(
            10, 10, 110, 110,
            fill=COLOR_GRIS_SUAVE,
            outline=COLOR_AZUL_PRINCIPAL,
            width=3
        )
        
        # Texto "USER" en el centro del círculo
        canvas.create_text(
            60, 60,
            text="USER",
            font=(FUENTE_PRINCIPAL, 16, "bold"),
            fill=COLOR_AZUL_PRINCIPAL
        )
    
    def set_login_callback(self, callback):
        """Establece la función callback que se ejecutará al hacer login exitoso"""
        self.on_login_success = callback
    
    def handle_login_click(self):
        """Maneja el clic del botón de login"""
        # Obtener credenciales
        credentials = self.get_credentials()
        
        # Validación básica
        if not credentials['usuario'] or not credentials['password']:
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