"""
Configuración global de tema y estilos para la aplicación UNISON
Define la paleta de colores oficial y configuraciones de estilo
"""

# Paleta de colores oficial UNISON
COLOR_AZUL_PRINCIPAL = "#00529e"      # Fondo principal, cabeceras, botones primarios
COLOR_AZUL_OSCURO = "#01509b"         # Hover/active para botones azules
COLOR_DORADO_ACENTO = "#f8bb00"       # Botones secundarios, acentos
COLOR_DORADO_OSCURO = "#d99e30"       # Hover/active para botones dorados
COLOR_TEXTO_PRINCIPAL = "#FFFFFF"     # Texto sobre fondos azules
COLOR_TEXTO_SECUNDARIO = "#000000"    # Texto sobre fondos claros/dorados

# Colores adicionales permitidos
COLOR_FONDO_CLARO = "#f8f9fa"         # Fondos claros
COLOR_FONDO_NEUTRAL = "#ffffff"       # Fondo blanco
COLOR_GRIS_SUAVE = "#e9ecef"          # Grises neutros
COLOR_GRIS_TEXTO = "#6c757d"          # Texto gris

# Configuración de fuente
FUENTE_PRINCIPAL = "Segoe UI"

# Configuración de estilos
BORDE_REDONDEADO = 8
PADDING_STANDAR = 10
ESPACIADO_ELEMENTOS = 15

# Configuración de tamaños
TAMAÑO_FUENTE_TITULO = 16
TAMAÑO_FUENTE_NORMAL = 11
TAMAÑO_FUENTE_BOTON = 12
TAMAÑO_FUENTE_LABEL = 10

# Configuración de dimensiones
ANCHO_BOTON_STANDAR = 140
ALTO_BOTON_STANDAR = 35
ANCHO_ENTRY_STANDAR = 200

def aplicar_estilo_global_tkinter():
    """
    Aplica los estilos globales para componentes Tkinter usando ttk.Style
    """
    import tkinter as tk
    from tkinter import ttk
    
    # Crear un estilo personalizado
    style = ttk.Style()
    
    # Configurar estilo para botones
    style.configure(
        "Unison.TButton",
        font=(FUENTE_PRINCIPAL, TAMAÑO_FUENTE_BOTON, "bold"),
        background=COLOR_AZUL_PRINCIPAL,
        foreground=COLOR_TEXTO_PRINCIPAL,
        borderwidth=1,
        relief="flat",
        padding=(PADDING_STANDAR, 8)
    )
    
    style.map(
        "Unison.TButton",
        background=[('active', COLOR_AZUL_OSCURO), ('pressed', COLOR_AZUL_OSCURO)]
    )
    
    # Configurar estilo para botones dorados
    style.configure(
        "UnisonGold.TButton",
        font=(FUENTE_PRINCIPAL, TAMAÑO_FUENTE_BOTON, "bold"),
        background=COLOR_DORADO_ACENTO,
        foreground=COLOR_TEXTO_SECUNDARIO,
        borderwidth=1,
        relief="flat",
        padding=(PADDING_STANDAR, 8)
    )
    
    style.map(
        "UnisonGold.TButton",
        background=[('active', COLOR_DORADO_OSCURO), ('pressed', COLOR_DORADO_OSCURO)]
    )
    
    # Configurar estilo para Entry
    style.configure(
        "Unison.TEntry",
        font=(FUENTE_PRINCIPAL, TAMAÑO_FUENTE_NORMAL),
        borderwidth=2,
        relief="solid",
        insertcolor=COLOR_AZUL_PRINCIPAL
    )
    
    # Configurar estilo para Labels
    style.configure(
        "Unison.TLabel",
        font=(FUENTE_PRINCIPAL, TAMAÑO_FUENTE_LABEL),
        background=COLOR_FONDO_NEUTRAL,
        foreground=COLOR_TEXTO_SECUNDARIO
    )
    
    # Configurar estilo para Labels sobre fondo azul
    style.configure(
        "UnisonBlue.TLabel",
        font=(FUENTE_PRINCIPAL, TAMAÑO_FUENTE_LABEL),
        background=COLOR_AZUL_PRINCIPAL,
        foreground=COLOR_TEXTO_PRINCIPAL
    )
    
    # Configurar estilo para Frame principal
    style.configure(
        "Unison.TFrame",
        background=COLOR_FONDO_NEUTRAL,
        relief="flat"
    )
    
    # Configurar estilo para Frame azul
    style.configure(
        "UnisonBlue.TFrame",
        background=COLOR_AZUL_PRINCIPAL,
        relief="flat"
    )
    
    return style

def crear_boton_unison(parent, texto, comando=None, estilo="primario", **kwargs):
    """
    Crea un botón con el estilo UNISON aplicado
    """
    import tkinter as tk
    
    if estilo == "primario":
        bg_color = COLOR_AZUL_PRINCIPAL
        fg_color = COLOR_TEXTO_PRINCIPAL
        hover_color = COLOR_AZUL_OSCURO
    else:  # dorado/secundario
        bg_color = COLOR_DORADO_ACENTO
        fg_color = COLOR_TEXTO_SECUNDARIO
        hover_color = COLOR_DORADO_OSCURO
    
    boton = tk.Button(
        parent,
        text=texto,
        font=(FUENTE_PRINCIPAL, TAMAÑO_FUENTE_BOTON, "bold"),
        bg=bg_color,
        fg=fg_color,
        relief="flat",
        borderwidth=0,
        cursor="hand2",
        command=comando,
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
    Crea un Entry con el estilo UNISON aplicado
    """
    import tkinter as tk
    
    entry = tk.Entry(
        parent,
        font=(FUENTE_PRINCIPAL, TAMAÑO_FUENTE_NORMAL),
        relief="solid",
        borderwidth=2,
        **kwargs
    )
    
    return entry

def crear_label_unison(parent, texto, sobre_azul=False, **kwargs):
    """
    Crea un Label con el estilo UNISON aplicado
    """
    import tkinter as tk
    
    # Establecer colores por defecto pero permitir override
    if sobre_azul:
        fg_color = kwargs.get('fg', COLOR_TEXTO_PRINCIPAL)
        bg_color = kwargs.get('bg', COLOR_AZUL_PRINCIPAL)
    else:
        fg_color = kwargs.get('fg', COLOR_TEXTO_SECUNDARIO)
        bg_color = kwargs.get('bg', COLOR_FONDO_NEUTRAL)
    
    # Establecer fuente por defecto si no se especifica una
    font_default = kwargs.get('font', (FUENTE_PRINCIPAL, TAMAÑO_FUENTE_LABEL))
    
    # Remover parámetros que vamos a establecer explícitamente para evitar duplicados
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
        bg_color = COLOR_AZUL_PRINCIPAL
    else:
        bg_color = COLOR_FONDO_NEUTRAL
    
    frame = tk.Frame(
        parent,
        bg=bg_color,
        **kwargs
    )
    
    return frame