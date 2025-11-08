"""
Configuración global de tema y estilos para la aplicación UNISON
Define la paleta de colores oficial de la Universidad de Sonora
"""

# Paleta de colores oficial UNISON (Universidad de Sonora)
COLOR_AZUL_UNISON = "#00529e"         # Azul principal UNISON
COLOR_AZUL_UNISON_OSCURO = "#01509b"  # Azul UNISON oscuro para hover
COLOR_DORADO_UNISON = "#f8bb00"       # Dorado UNISON
COLOR_DORADO_UNISON_OSCURO = "#d99e30" # Dorado UNISON oscuro para hover
COLOR_TEXTO_BLANCO = "#FFFFFF"        # Texto blanco sobre fondos oscuros
COLOR_TEXTO_NEGRO = "#000000"         # Texto negro sobre fondos claros

# Colores auxiliares
COLOR_FONDO_CLARO = "#f8f9fa"         # Fondos claros
COLOR_FONDO_BLANCO = "#ffffff"        # Fondo blanco
COLOR_GRIS_CLARO = "#e9ecef"          # Grises neutros
COLOR_GRIS_MEDIO = "#6c757d"          # Texto gris

# Configuración de fuente UNISON
FUENTE_UNISON = "Segoe UI"

# Configuración de estilos
BORDE_REDONDEADO = 8
PADDING_ESTANDAR = 10
ESPACIADO_ELEMENTOS = 15

# Configuración de tamaños de fuente
TAMAÑO_FUENTE_TITULO = 16
TAMAÑO_FUENTE_NORMAL = 11
TAMAÑO_FUENTE_BOTON = 12
TAMAÑO_FUENTE_LABEL = 10

# Configuración de dimensiones
ANCHO_BOTON_ESTANDAR = 140
ALTO_BOTON_ESTANDAR = 35
ANCHO_ENTRY_ESTANDAR = 200

def aplicar_tema_ventana(ventana):
    """
    Aplica el tema UNISON a una ventana completa
    """
    ventana.configure(bg=COLOR_FONDO_BLANCO)
    return ventana

def crear_boton_unison(parent, texto, comando=None, estilo="primario", **kwargs):
    """
    Crea un botón con el estilo UNISON y bordes redondeados (simulado)
    """
    import tkinter as tk
    
    if estilo == "primario":
        bg_color = COLOR_AZUL_UNISON
        fg_color = COLOR_TEXTO_BLANCO
        hover_color = COLOR_AZUL_UNISON_OSCURO
    else:  # dorado/secundario
        bg_color = COLOR_DORADO_UNISON
        fg_color = COLOR_TEXTO_NEGRO
        hover_color = COLOR_DORADO_UNISON_OSCURO
    
    boton = tk.Button(
        parent,
        text=texto,
        font=(FUENTE_UNISON, TAMAÑO_FUENTE_BOTON, "bold"),
        bg=bg_color,
        fg=fg_color,
        relief="flat",
        borderwidth=0,
        cursor="hand2",
        command=comando,
        pady=8,
        padx=20,
        **kwargs
    )
    
    # Efectos hover
    def on_enter(e):
        boton.config(bg=hover_color)
    
    def on_leave(e):
        boton.config(bg=bg_color)
    
    boton.bind("<Enter>", on_enter)
    boton.bind("<Leave>", on_leave)
    
    return boton

def crear_entry_unison(parent, **kwargs):
    """
    Crea un Entry con el estilo UNISON
    """
    import tkinter as tk
    
    # Configuración por defecto
    config_default = {
        'font': (FUENTE_UNISON, TAMAÑO_FUENTE_NORMAL),
        'relief': 'solid',
        'borderwidth': 2,
        'bd': 1,
        'highlightcolor': COLOR_AZUL_UNISON,
        'highlightbackground': COLOR_GRIS_CLARO,
        'insertbackground': COLOR_AZUL_UNISON
    }
    
    # Actualizar con kwargs personalizados
    config_default.update(kwargs)
    
    entry = tk.Entry(parent, **config_default)
    
    return entry

def crear_label_unison(parent, texto, sobre_azul=False, **kwargs):
    """
    Crea un Label con el estilo UNISON aplicado
    """
    import tkinter as tk
    
    # Establecer colores por defecto
    if sobre_azul:
        fg_color = kwargs.get('fg', COLOR_TEXTO_BLANCO)
        bg_color = kwargs.get('bg', COLOR_AZUL_UNISON)
    else:
        fg_color = kwargs.get('fg', COLOR_TEXTO_NEGRO)
        bg_color = kwargs.get('bg', COLOR_FONDO_BLANCO)
    
    # Establecer fuente por defecto si no se especifica una
    font_default = kwargs.get('font', (FUENTE_UNISON, TAMAÑO_FUENTE_LABEL))
    
    # Remover parámetros que vamos a establecer explícitamente
    kwargs_clean = {k: v for k, v in kwargs.items() if k not in ['fg', 'bg', 'font']}
    
    label = tk.Label(
        parent,
        text=texto,
        fg=fg_color,
        bg=bg_color,
        font=font_default,
        **kwargs_clean
    )
    
    return label

def crear_frame_unison(parent, azul=False, **kwargs):
    """
    Crea un Frame con el estilo UNISON aplicado
    """
    import tkinter as tk
    
    if azul:
        bg_color = COLOR_AZUL_UNISON
    else:
        bg_color = COLOR_FONDO_BLANCO
    
    # Configuración por defecto
    config_default = {
        'bg': bg_color,
        'relief': 'flat'
    }
    
    # Actualizar con kwargs personalizados
    config_default.update(kwargs)
    
    frame = tk.Frame(parent, **config_default)
    
    return frame

def crear_titulo_unison(parent, texto, **kwargs):
    """
    Crea un título con el estilo UNISON
    """
    import tkinter as tk
    
    config_default = {
        'font': (FUENTE_UNISON, TAMAÑO_FUENTE_TITULO, "bold"),
        'fg': COLOR_AZUL_UNISON,
        'bg': COLOR_FONDO_BLANCO
    }
    
    config_default.update(kwargs)
    
    titulo = tk.Label(parent, text=texto, **config_default)
    return titulo