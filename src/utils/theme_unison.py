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
COLOR_TEXTO_SECUNDARIO = "#6c757d"    # Texto gris secundario

# Colores auxiliares
COLOR_FONDO_CLARO = "#f8f9fa"         # Fondos claros
COLOR_FONDO_BLANCO = "#ffffff"        # Fondo blanco
COLOR_FONDO_NEUTRAL = "#f8f9fa"       # Fondo neutral (igual a claro)
COLOR_GRIS_CLARO = "#e9ecef"          # Grises neutros
COLOR_GRIS_MEDIO = "#6c757d"          # Texto gris

# Configuración de fuente UNISON
FUENTE_UNISON = "Segoe UI"
FUENTE_PRINCIPAL = "Segoe UI"  # Alias para compatibilidad

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

import tkinter as tk

class EntryRedondeadoContainer(tk.Frame):
    """Contenedor personalizado para Entry redondeado con atributo entry definido"""
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.entry: tk.Entry = None  # Tipo explícito para Pylance

class BotonRedondeadoContainer(tk.Frame):
    """Contenedor personalizado para Botón redondeado con atributos definidos"""
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.canvas: tk.Canvas = None  # Canvas del botón
    
    def config(self, command=None, **kwargs):
        """Método config para cambiar el comando del botón"""
        pass  # Se sobrescribirá después

def crear_entry_redondeado(parent, width=300, height=40, corner_radius=8, **kwargs):
    """
    Crea un Entry con bordes redondeados usando Canvas (8px)
    """
    import tkinter as tk
    
    # Extraer parámetros específicos
    show = kwargs.pop('show', None)
    
    # Frame contenedor con tipo explícito
    container = EntryRedondeadoContainer(parent, bg=parent['bg'] if isinstance(parent, tk.Frame) else COLOR_FONDO_BLANCO)
    
    # Canvas para el borde redondeado
    canvas = tk.Canvas(
        container,
        width=width,
        height=height,
        bg=parent['bg'] if isinstance(parent, tk.Frame) else COLOR_FONDO_BLANCO,
        highlightthickness=0,
        bd=0
    )
    canvas.pack()
    
    # Dibujar rectángulo redondeado (borde)
    border_color = COLOR_GRIS_CLARO
    
    def create_rounded_rect(x1, y1, x2, y2, r, **opts):
        return canvas.create_polygon(
            x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, 
            x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, 
            x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1, smooth=True, **opts
        )
    
    # Fondo del entry
    create_rounded_rect(
        2, 2, width-2, height-2, corner_radius,
        fill=COLOR_FONDO_BLANCO, outline=border_color, width=2
    )
    
    # Entry real
    entry = tk.Entry(
        canvas,
        font=(FUENTE_UNISON, TAMAÑO_FUENTE_NORMAL),
        relief='flat',
        bd=0,
        highlightthickness=0,
        insertbackground=COLOR_AZUL_UNISON,
        bg=COLOR_FONDO_BLANCO,
        fg=COLOR_TEXTO_NEGRO,
        show=show if show else '',
        **kwargs
    )
    
    # Posicionar el entry en el canvas INICIALMENTE
    canvas.create_window(width//2, height//2, window=entry, width=width-20, height=height-10)
    
    # Efectos de focus
    def on_focus_in(e):
        canvas.delete('all')
        create_rounded_rect(
            2, 2, width-2, height-2, corner_radius,
            fill=COLOR_FONDO_BLANCO, outline=COLOR_AZUL_UNISON, width=2
        )
        canvas.create_window(width//2, height//2, window=entry, width=width-20, height=height-10)
    
    def on_focus_out(e):
        canvas.delete('all')
        create_rounded_rect(
            2, 2, width-2, height-2, corner_radius,
            fill=COLOR_FONDO_BLANCO, outline=border_color, width=2
        )
        canvas.create_window(width//2, height//2, window=entry, width=width-20, height=height-10)
    
    entry.bind('<FocusIn>', on_focus_in)
    entry.bind('<FocusOut>', on_focus_out)
    
    # Guardar referencia al entry en el container
    container.entry = entry
    
    return container

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

    frame = tk.Frame(parent, config_default)

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

def configurar_estilo_treeview():
    """
    Configura el estilo global para Treeview con colores UNISON
    """
    from tkinter import ttk
    
    style = ttk.Style()
    
    # Configurar tema base
    style.theme_use('clam')
    
    # Estilo para los encabezados
    style.configure(
        "Treeview.Heading",
        background=COLOR_AZUL_UNISON,
        foreground=COLOR_TEXTO_BLANCO,
        font=(FUENTE_UNISON, TAMAÑO_FUENTE_NORMAL, "bold"),
        relief="flat",
        borderwidth=0
    )
    
    style.map(
        "Treeview.Heading",
        background=[('active', COLOR_AZUL_UNISON_OSCURO)],
        foreground=[('active', COLOR_TEXTO_BLANCO)]
    )
    
    # Estilo para las filas
    style.configure(
        "Treeview",
        background=COLOR_FONDO_BLANCO,
        foreground=COLOR_TEXTO_NEGRO,
        fieldbackground=COLOR_FONDO_BLANCO,
        font=(FUENTE_UNISON, TAMAÑO_FUENTE_LABEL),
        rowheight=28,
        borderwidth=0
    )
    
    # Colores alternados para filas
    style.map(
        "Treeview",
        background=[('selected', COLOR_AZUL_UNISON)],
        foreground=[('selected', COLOR_TEXTO_BLANCO)]
    )
    
    return style

def crear_boton_redondeado_canvas(parent, texto, comando=None, width=200, height=45, 
                                  corner_radius=8, estilo="primario", bg_custom=None, hover_custom=None):
    """
    Crea un botón con bordes redondeados reales usando Canvas (8px)
    Parámetros adicionales:
    - bg_custom: Color de fondo personalizado (opcional)
    - hover_custom: Color hover personalizado (opcional)
    """
    import tkinter as tk
    
    if estilo == "primario":
        bg_color = COLOR_AZUL_UNISON
        hover_color = COLOR_AZUL_UNISON_OSCURO
        text_color = COLOR_TEXTO_BLANCO
    elif estilo == "dorado":
        bg_color = COLOR_DORADO_UNISON
        hover_color = COLOR_DORADO_UNISON_OSCURO
        text_color = COLOR_TEXTO_NEGRO
    elif estilo == "custom":
        bg_color = bg_custom if bg_custom else "#c0392b"
        hover_color = hover_custom if hover_custom else "#a93226"
        text_color = COLOR_TEXTO_BLANCO
    else:
        bg_color = COLOR_AZUL_UNISON
        hover_color = COLOR_AZUL_UNISON_OSCURO
        text_color = COLOR_TEXTO_BLANCO
    
    # Frame contenedor con tipo explícito
    container = BotonRedondeadoContainer(parent, bg=parent['bg'] if isinstance(parent, tk.Frame) else COLOR_FONDO_BLANCO)
    
    # Canvas para el botón
    canvas = tk.Canvas(
        container,
        width=width,
        height=height,
        bg=parent['bg'] if isinstance(parent, tk.Frame) else COLOR_FONDO_BLANCO,
        highlightthickness=0,
        bd=0,
        cursor="hand2"
    )
    canvas.pack()
    
    # Función para crear rectángulo redondeado con arcos reales
    def create_round_rectangle(x1, y1, x2, y2, radius, **kwargs):
        """Dibuja un rectángulo con esquinas redondeadas usando arcos reales"""
        # Extraer fill y outline de kwargs
        fill = kwargs.get('fill', '')
        outline = kwargs.get('outline', '')
        width_param = kwargs.get('width', 1)
        
        # Crear las 4 esquinas con arcos
        canvas.create_arc(x1, y1, x1 + radius*2, y1 + radius*2, 
                         start=90, extent=90, fill=fill, outline=outline, width=width_param)
        canvas.create_arc(x2 - radius*2, y1, x2, y1 + radius*2, 
                         start=0, extent=90, fill=fill, outline=outline, width=width_param)
        canvas.create_arc(x2 - radius*2, y2 - radius*2, x2, y2, 
                         start=270, extent=90, fill=fill, outline=outline, width=width_param)
        canvas.create_arc(x1, y2 - radius*2, x1 + radius*2, y2, 
                         start=180, extent=90, fill=fill, outline=outline, width=width_param)
        
        # Crear los 4 rectángulos que conectan los arcos
        # Top
        canvas.create_rectangle(x1 + radius, y1, x2 - radius, y1 + radius, 
                               fill=fill, outline=fill, width=0)
        # Bottom
        canvas.create_rectangle(x1 + radius, y2 - radius, x2 - radius, y2, 
                               fill=fill, outline=fill, width=0)
        # Left
        canvas.create_rectangle(x1, y1 + radius, x1 + radius, y2 - radius, 
                               fill=fill, outline=fill, width=0)
        # Right
        canvas.create_rectangle(x2 - radius, y1 + radius, x2, y2 - radius, 
                               fill=fill, outline=fill, width=0)
        
        # Centro
        canvas.create_rectangle(x1 + radius, y1 + radius, x2 - radius, y2 - radius, 
                               fill=fill, outline=fill, width=0)
        
        # Retornar un identificador (usaremos un tag para agrupar)
        return "rounded_rect"
    
    # Dibujar el botón
    btn_rect = create_round_rectangle(
        0, 0, width, height, corner_radius,
        fill=bg_color, outline=bg_color, width=2
    )
    
    # Texto del botón
    btn_text = canvas.create_text(
        width//2, height//2,
        text=texto,
        fill=text_color,
        font=(FUENTE_UNISON, TAMAÑO_FUENTE_BOTON, "bold")
    )
    
    # Efectos hover
    def on_enter(e):
        canvas.itemconfig(btn_rect, fill=hover_color, outline=hover_color)
    
    def on_leave(e):
        canvas.itemconfig(btn_rect, fill=bg_color, outline=bg_color)
    
    def on_click(e):
        if comando:
            comando()
    
    canvas.bind('<Enter>', on_enter)
    canvas.bind('<Leave>', on_leave)
    canvas.bind('<Button-1>', on_click)
    
    # Agregar método config para compatibilidad con el controlador
    def config_method(command=None, **kwargs):
        if command:
            # Desvincular el evento anterior y vincular el nuevo
            canvas.unbind('<Button-1>')
            canvas.bind('<Button-1>', lambda e: command())
    
    # Agregar atributos al container
    container.canvas = canvas
    container.config = config_method
    
    return container