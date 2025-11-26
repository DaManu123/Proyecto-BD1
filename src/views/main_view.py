import tkinter as tk
from tkinter import ttk, Frame, Label, Button, Entry, Canvas, BooleanVar, Checkbutton
from tkcalendar import DateEntry
from datetime import datetime
import os
import sys

# Importar el sistema de temas UNISON - Agregar ruta absoluta
current_dir = os.path.dirname(os.path.abspath(__file__))
utils_path = os.path.join(current_dir, '..', 'utils')
if utils_path not in sys.path:
    sys.path.insert(0, utils_path)
from theme_unison import (
    COLOR_AZUL_UNISON, COLOR_AZUL_UNISON_OSCURO, COLOR_DORADO_UNISON,
    COLOR_TEXTO_BLANCO, COLOR_TEXTO_NEGRO, COLOR_FONDO_BLANCO, COLOR_FONDO_CLARO,
    COLOR_GRIS_CLARO,
    FUENTE_UNISON, TAMAÑO_FUENTE_NORMAL, TAMAÑO_FUENTE_BOTON, TAMAÑO_FUENTE_LABEL,
    BORDE_REDONDEADO,
    crear_boton_redondeado_canvas, crear_entry_redondeado, crear_label_unison, crear_frame_unison,
    crear_titulo_unison, configurar_estilo_treeview
)

class MainView:
    def __init__(self, master):
        self.master = master
        
        # Configurar estilos globales de Treeview
        configurar_estilo_treeview()
        
        # Variables para control de ordenamiento
        self.productos_orden = {}  # {'columna': 'asc'/'desc'}
        self.almacenes_orden = {}  # {'columna': 'asc'/'desc'}
        self.productos_data_cache = []  # Cache de datos para ordenamiento
        self.almacenes_data_cache = []  # Cache de datos para ordenamiento
        
        # Variables para filtros
        self.productos_data_original = []  # Datos originales sin filtrar
        self.almacenes_data_original = []  # Datos originales sin filtrar
        self.filtros_productos_visible = True
        self.filtros_almacenes_visible = True
        
        # Solo configurar propiedades de ventana si master es una ventana Tk, no un Frame
        if hasattr(master, 'title'):
            self.master.title("Sistema de Inventario - Universidad de Sonora - Manuel Munguia Rubio")
            self.master.geometry("950x700")
            self.master.resizable(True, True)
            self.master.minsize(800, 600)
            
            # Intentar establecer el icono de la ventana con el logo
            try:
                logo_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'unilogo.gif')
                if os.path.exists(logo_path):
                    icon = tk.PhotoImage(file=logo_path)
                    self.master.iconphoto(True, icon)
            except Exception as e:
                print(f"No se pudo establecer el icono: {e}")
        
        self.master.configure(bg=COLOR_FONDO_CLARO)
        
        # Configurar el grid principal para que sea responsivo
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        
        # Contenedor principal para todos los frames
        self.container = crear_frame_unison(self.master, azul=False)
        self.container.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        
        # Configurar el contenedor para que sea responsivo
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        
        # Dictionary para almacenar los frames
        self.frames = {}
        
        # Variable para mantener la referencia del logo
        self.logo_image = None
        
        # Crear todos los frames
        self.create_frames()
    
    def create_frames(self):
        """Crea todos los frames de la aplicación"""
        # Frame de Inicio
        self.frames["inicio"] = self.create_inicio_frame()
        
        # Frame de Productos
        self.frames["productos"] = self.create_productos_frame()
        
        # Frame de Almacenes
        self.frames["almacenes"] = self.create_almacenes_frame()
        
        # Mostrar el frame de inicio por defecto
        self.show_frame("inicio")
    
    def create_inicio_frame(self):
        """Crea el frame de inicio con scroll y diseño responsivo"""
        frame = Frame(self.container, bg=COLOR_FONDO_CLARO)
        # No hacer grid aquí - se hará en show_frame()
        
        # Configurar el grid principal
        frame.grid_rowconfigure(1, weight=1)  # Contenido scrollable
        frame.grid_columnconfigure(0, weight=1)
        
        # Barra de navegación discreta solo para inicio
        nav_bar = Frame(frame, bg=COLOR_AZUL_UNISON, height=50)
        nav_bar.grid(row=0, column=0, sticky="ew", padx=10, pady=(10, 0))
        nav_bar.grid_propagate(False)
        nav_bar.grid_columnconfigure(0, weight=1)
        
        # Container centrado para botones
        nav_buttons = Frame(nav_bar, bg=COLOR_AZUL_UNISON)
        nav_buttons.place(relx=0.5, rely=0.5, anchor="center")
        
        # Botones discretos de navegación
        self.btn_productos = crear_boton_redondeado_canvas(
            nav_buttons,
            texto="📦 Productos",
            comando=lambda: self.show_frame("productos"),
            width=150,
            height=35,
            corner_radius=BORDE_REDONDEADO,
            estilo="primario"
        )
        self.btn_productos.pack(side="left", padx=8)
        
        self.btn_almacenes = crear_boton_redondeado_canvas(
            nav_buttons,
            texto="🏪 Almacenes",
            comando=lambda: self.show_frame("almacenes"),
            width=150,
            height=35,
            corner_radius=BORDE_REDONDEADO,
            estilo="primario"
        )
        self.btn_almacenes.pack(side="left", padx=8)
        
        self.btn_cerrar_sesion = crear_boton_redondeado_canvas(
            nav_buttons,
            texto="🚪 Cerrar Sesión",
            comando=None,
            width=150,
            height=35,
            corner_radius=BORDE_REDONDEADO,
            estilo="dorado"
        )
        self.btn_cerrar_sesion.pack(side="left", padx=8)
        
        # Crear Canvas y Scrollbar para scroll vertical
        canvas = tk.Canvas(frame, bg=COLOR_FONDO_CLARO, highlightthickness=0)
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollable_frame = Frame(canvas, bg=COLOR_FONDO_CLARO)
        
        # Configurar el scroll
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Grid del canvas y scrollbar (ahora en row=1 por la barra de navegación)
        canvas.grid(row=1, column=0, sticky="nsew")
        scrollbar.grid(row=1, column=1, sticky="ns")
        
        # Configurar el frame scrollable para que sea responsivo
        scrollable_frame.grid_columnconfigure(0, weight=1)
        
        # Contenido principal dentro del frame scrollable
        main_content = Frame(scrollable_frame, bg=COLOR_FONDO_CLARO)
        main_content.grid(row=0, column=0, sticky="ew", padx=20, pady=20)
        main_content.grid_columnconfigure(0, weight=1)
        
        # Logo de la Universidad de Sonora (tamaño reducido para mejor responsividad)
        try:
            logo_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'unilogo.gif')
            if os.path.exists(logo_path):
                self.logo_image = tk.PhotoImage(file=logo_path)
                logo_label = Label(main_content, image=self.logo_image, bg="#f0f0f0")
                logo_label.grid(row=0, column=0, pady=(10, 8), sticky="n")
            else:
                logo_placeholder = Label(main_content, text="UNISON", font=(FUENTE_UNISON, 28, "bold"), 
                                        bg=COLOR_FONDO_CLARO, fg=COLOR_AZUL_UNISON)
                logo_placeholder.grid(row=0, column=0, pady=(10, 8), sticky="n")
        except Exception as e:
            print(f"Error cargando logo: {e}")
            logo_placeholder = Label(main_content, text="UNISON", font=(FUENTE_UNISON, 28, "bold"), 
                                    bg=COLOR_FONDO_CLARO, fg=COLOR_AZUL_UNISON)
            logo_placeholder.grid(row=0, column=0, pady=(10, 8), sticky="n")
        
        # Título Universidad con colores UNISON
        titulo = Label(main_content, text="Universidad de Sonora", 
                      font=(FUENTE_UNISON, 22, "bold"), bg=COLOR_FONDO_CLARO, fg=COLOR_AZUL_UNISON)
        titulo.grid(row=1, column=0, pady=(0, 5), sticky="ew")
        
        # Subtítulo del sistema
        subtitulo = Label(main_content, text="Sistema de Inventario - Base de Datos 1", 
                         font=(FUENTE_UNISON, 13, "italic"), bg=COLOR_FONDO_CLARO, fg=COLOR_AZUL_UNISON_OSCURO)
        subtitulo.grid(row=2, column=0, pady=(0, 15), sticky="ew")
        
        # Separador visual con color UNISON dorado
        separator = Frame(main_content, height=3, bg=COLOR_DORADO_UNISON)
        separator.grid(row=3, column=0, sticky="ew", padx=30, pady=10)
        
        # Nombres de estudiantes
        nombres = Label(main_content, text="Manuel Munguia Rubio", 
                       font=(FUENTE_UNISON, 17, "bold"), bg=COLOR_FONDO_CLARO, fg=COLOR_AZUL_UNISON)
        nombres.grid(row=4, column=0, pady=(10, 5), sticky="ew")
        
        # Información adicional
        info = Label(main_content, text="Carrera: Ingeniería en Sistemas de Información", 
                    font=(FUENTE_UNISON, 12), bg=COLOR_FONDO_CLARO, fg=COLOR_AZUL_UNISON_OSCURO)
        info.grid(row=5, column=0, pady=(0, 25), sticky="ew")
        
        # Espacio adicional al final para asegurar que todo sea visible
        spacer = Frame(main_content, bg=COLOR_FONDO_CLARO, height=50)
        spacer.grid(row=7, column=0, sticky="ew")
        
        # Bind scroll con mouse wheel
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        canvas.bind_all("<MouseWheel>", _on_mousewheel)
        
        # Función para ajustar el scroll cuando cambie el tamaño
        def configure_scroll_region(event=None):
            canvas.configure(scrollregion=canvas.bbox("all"))
            # Ajustar el ancho del frame scrollable al ancho del canvas
            canvas_width = canvas.winfo_width()
            canvas.itemconfig(canvas.find_all()[0], width=canvas_width)
        
        canvas.bind('<Configure>', configure_scroll_region)
        
        return frame
    
    def create_productos_frame(self):
        """Crea el frame de gestión de productos"""
        frame = Frame(self.container, bg=COLOR_FONDO_CLARO)
        # No hacer grid aquí - se hará en show_frame()
        
        # Configurar grid responsivo
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=0)  # Panel de filtros
        frame.grid_columnconfigure(1, weight=1)  # Contenido principal
        
        # ===== PANEL LATERAL DE FILTROS =====
        self.panel_filtros_productos = Frame(frame, bg="white", relief="raised", bd=1, width=240)
        self.panel_filtros_productos.grid(row=0, column=0, sticky="nsew", padx=(10, 0), pady=10)
        self.panel_filtros_productos.grid_propagate(False)
        
        # Header del panel de filtros
        filtros_header = Frame(self.panel_filtros_productos, bg=COLOR_AZUL_UNISON, height=40)
        filtros_header.pack(fill="x")
        
        Label(filtros_header, text="🔍 Filtros", font=(FUENTE_UNISON, 11, "bold"),
              bg=COLOR_AZUL_UNISON, fg=COLOR_TEXTO_BLANCO).pack(side="left", padx=10, pady=8)
        
        self.btn_toggle_filtros_prod = crear_boton_redondeado_canvas(
            filtros_header, texto="◀", comando=self.toggle_filtros_productos,
            width=35, height=25, corner_radius=5, estilo="dorado"
        )
        self.btn_toggle_filtros_prod.pack(side="right", padx=8, pady=8)
        
        # Contenedor directo para filtros sin scrollbar
        filtros_scroll_frame = Frame(self.panel_filtros_productos, bg="white")
        filtros_scroll_frame.pack(fill="both", expand=True, padx=8, pady=5)
        
        # ===== FILTROS INDIVIDUALES =====
        # Búsqueda general
        Label(filtros_scroll_frame, text="Buscar:", font=("Arial", 8, "bold"),
              bg="white", fg="#2c3e50", anchor="w").pack(fill="x", padx=5, pady=(8, 1))
        buscar_container = crear_entry_redondeado(filtros_scroll_frame, width=210, height=28, corner_radius=5)
        buscar_container.pack(padx=5, pady=(0, 6))
        self.filtro_buscar_producto = buscar_container.entry
        self.filtro_buscar_producto.bind('<KeyRelease>', lambda e: self.aplicar_filtros_productos())
        
        ttk.Separator(filtros_scroll_frame, orient='horizontal').pack(fill='x', padx=8, pady=3)
        
        # Departamento
        Label(filtros_scroll_frame, text="Departamento:", font=("Arial", 8, "bold"),
              bg="white", fg="#2c3e50", anchor="w").pack(fill="x", padx=5, pady=(3, 1))
        depto_container = crear_entry_redondeado(filtros_scroll_frame, width=210, height=28, corner_radius=5)
        depto_container.pack(padx=5, pady=(0, 6))
        self.filtro_departamento = depto_container.entry
        self.filtro_departamento.bind('<KeyRelease>', lambda e: self.aplicar_filtros_productos())
        
        # Almacén
        Label(filtros_scroll_frame, text="Almacén:", font=("Arial", 8, "bold"),
              bg="white", fg="#2c3e50", anchor="w").pack(fill="x", padx=5, pady=(3, 1))
        almacen_container = crear_entry_redondeado(filtros_scroll_frame, width=210, height=28, corner_radius=5)
        almacen_container.pack(padx=5, pady=(0, 6))
        self.filtro_almacen_producto = almacen_container.entry
        self.filtro_almacen_producto.bind('<KeyRelease>', lambda e: self.aplicar_filtros_productos())
        
        ttk.Separator(filtros_scroll_frame, orient='horizontal').pack(fill='x', padx=8, pady=3)
        
        # Rango de precio
        Label(filtros_scroll_frame, text="Precio:", font=("Arial", 8, "bold"),
              bg="white", fg="#2c3e50", anchor="w").pack(fill="x", padx=5, pady=(3, 1))
        
        precio_frame = Frame(filtros_scroll_frame, bg="white")
        precio_frame.pack(fill="x", padx=5, pady=(0, 6))
        
        Label(precio_frame, text="Min:", font=("Arial", 7), bg="white", fg="#7f8c8d").grid(row=0, column=0, sticky="w")
        precio_min_container = crear_entry_redondeado(precio_frame, width=85, height=26, corner_radius=5)
        precio_min_container.grid(row=0, column=1, padx=(3, 5))
        self.filtro_precio_min = precio_min_container.entry
        self.filtro_precio_min.bind('<KeyRelease>', lambda e: self.aplicar_filtros_productos())
        
        Label(precio_frame, text="Max:", font=("Arial", 7), bg="white", fg="#7f8c8d").grid(row=1, column=0, sticky="w", pady=(3, 0))
        precio_max_container = crear_entry_redondeado(precio_frame, width=85, height=26, corner_radius=5)
        precio_max_container.grid(row=1, column=1, padx=(3, 5), pady=(3, 0))
        self.filtro_precio_max = precio_max_container.entry
        self.filtro_precio_max.bind('<KeyRelease>', lambda e: self.aplicar_filtros_productos())
        
        # Rango de cantidad
        Label(filtros_scroll_frame, text="Cantidad:", font=("Arial", 8, "bold"),
              bg="white", fg="#2c3e50", anchor="w").pack(fill="x", padx=5, pady=(3, 1))
        
        cantidad_frame = Frame(filtros_scroll_frame, bg="white")
        cantidad_frame.pack(fill="x", padx=5, pady=(0, 6))
        
        Label(cantidad_frame, text="Min:", font=("Arial", 7), bg="white", fg="#7f8c8d").grid(row=0, column=0, sticky="w")
        cantidad_min_container = crear_entry_redondeado(cantidad_frame, width=85, height=26, corner_radius=5)
        cantidad_min_container.grid(row=0, column=1, padx=(3, 5))
        self.filtro_cantidad_min = cantidad_min_container.entry
        self.filtro_cantidad_min.bind('<KeyRelease>', lambda e: self.aplicar_filtros_productos())
        
        Label(cantidad_frame, text="Max:", font=("Arial", 7), bg="white", fg="#7f8c8d").grid(row=1, column=0, sticky="w", pady=(3, 0))
        cantidad_max_container = crear_entry_redondeado(cantidad_frame, width=85, height=26, corner_radius=5)
        cantidad_max_container.grid(row=1, column=1, padx=(3, 5), pady=(3, 0))
        self.filtro_cantidad_max = cantidad_max_container.entry
        self.filtro_cantidad_max.bind('<KeyRelease>', lambda e: self.aplicar_filtros_productos())
        
        # Usuario que modificó
        Label(filtros_scroll_frame, text="Usuario:", font=("Arial", 8, "bold"),
              bg="white", fg="#2c3e50", anchor="w").pack(fill="x", padx=5, pady=(3, 1))
        
        usuario_frame = Frame(filtros_scroll_frame, bg="white")
        usuario_frame.pack(fill="x", padx=5, pady=(0, 6))
        
        self.filtro_usuario_prod = ttk.Combobox(usuario_frame, state="readonly", width=27, font=("Arial", 8))
        self.filtro_usuario_prod.pack(fill="x")
        self.filtro_usuario_prod.set("Todos")
        self.filtro_usuario_prod.bind('<<ComboboxSelected>>', lambda e: self.aplicar_filtros_productos())
        
        # Rango de fechas
        Label(filtros_scroll_frame, text="Fecha modificación:", font=("Arial", 8, "bold"),
              bg="white", fg="#2c3e50", anchor="w").pack(fill="x", padx=5, pady=(3, 1))
        
        fecha_frame = Frame(filtros_scroll_frame, bg="white")
        fecha_frame.pack(fill="x", padx=5, pady=(0, 6))
        
        Label(fecha_frame, text="Desde:", font=("Arial", 7), bg="white", fg="#7f8c8d").grid(row=0, column=0, sticky="w")
        self.filtro_fecha_desde_prod = DateEntry(fecha_frame, width=16, background=COLOR_AZUL_UNISON,
                                                  foreground='white', borderwidth=2, font=("Arial", 7),
                                                  date_pattern='yyyy-mm-dd')
        self.filtro_fecha_desde_prod.grid(row=0, column=1, padx=(3, 0), pady=(0, 3))
        self.filtro_fecha_desde_prod.bind('<<DateEntrySelected>>', lambda e: self.aplicar_filtros_productos())
        
        Label(fecha_frame, text="Hasta:", font=("Arial", 7), bg="white", fg="#7f8c8d").grid(row=1, column=0, sticky="w")
        self.filtro_fecha_hasta_prod = DateEntry(fecha_frame, width=16, background=COLOR_AZUL_UNISON,
                                                  foreground='white', borderwidth=2, font=("Arial", 7),
                                                  date_pattern='yyyy-mm-dd')
        self.filtro_fecha_hasta_prod.grid(row=1, column=1, padx=(3, 0))
        self.filtro_fecha_hasta_prod.bind('<<DateEntrySelected>>', lambda e: self.aplicar_filtros_productos())
        
        # Checkbox para habilitar/deshabilitar filtro de fecha
        self.fecha_habilitada_prod = BooleanVar(value=False)
        self.chk_fecha_prod = Checkbutton(fecha_frame, text="Aplicar", variable=self.fecha_habilitada_prod,
                                          bg="white", font=("Arial", 7), command=self.aplicar_filtros_productos)
        self.chk_fecha_prod.grid(row=0, column=2, rowspan=2, padx=(5, 0))
        
        ttk.Separator(filtros_scroll_frame, orient='horizontal').pack(fill='x', padx=8, pady=5)
        
        # Botones de acción
        self.btn_limpiar_filtros_prod = crear_boton_redondeado_canvas(
            filtros_scroll_frame, texto="Limpiar", comando=self.limpiar_filtros_productos,
            width=210, height=30, corner_radius=5, estilo="custom",
            bg_custom="#95a5a6", hover_custom="#7f8c8d"
        )
        self.btn_limpiar_filtros_prod.pack(padx=5, pady=(3, 5))
        
        # Contador de resultados
        self.lbl_resultados_productos = Label(
            filtros_scroll_frame, text="0 productos", font=("Arial", 7, "italic"),
            bg="white", fg="#7f8c8d", wraplength=200
        )
        self.lbl_resultados_productos.pack(padx=5, pady=(3, 8))
        
        # Botón flotante para mostrar filtros cuando están ocultos
        self.btn_mostrar_filtros_prod = crear_boton_redondeado_canvas(
            frame, texto="▶", comando=self.toggle_filtros_productos,
            width=30, height=40, corner_radius=5, estilo="primario"
        )
        # Inicialmente oculto
        
        # ===== CONTENEDOR PRINCIPAL (DERECHA) =====
        contenedor_principal = Frame(frame, bg=COLOR_FONDO_CLARO)
        contenedor_principal.grid(row=0, column=1, sticky="nsew", padx=(8, 10), pady=10)
        contenedor_principal.grid_rowconfigure(2, weight=1)
        contenedor_principal.grid_columnconfigure(0, weight=1)
        
        # Header con colores UNISON
        header_frame = Frame(contenedor_principal, bg=COLOR_AZUL_UNISON, height=60)
        header_frame.grid(row=0, column=0, sticky="ew")
        header_frame.grid_propagate(False)
        header_frame.grid_columnconfigure(1, weight=1)
        
        # Título con icono
        titulo = Label(header_frame, text="📦 Gestión de Productos", 
                      font=(FUENTE_UNISON, 20, "bold"), bg=COLOR_AZUL_UNISON, fg=COLOR_TEXTO_BLANCO)
        titulo.grid(row=0, column=0, sticky="w", padx=25, pady=15)
        
        # Botón de volver discreto
        self.btn_volver_productos = crear_boton_redondeado_canvas(
            header_frame,
            texto="⬅ Volver",
            comando=lambda: self.show_frame("inicio"),
            width=120,
            height=35,
            corner_radius=BORDE_REDONDEADO,
            estilo="dorado"
        )
        self.btn_volver_productos.grid(row=0, column=1, sticky="e", padx=25, pady=12)
        
        # Frame para formulario con mejor organización
        self.producto_form_frame = Frame(contenedor_principal, bg="white", relief="raised", bd=1)
        self.producto_form_frame.grid(row=1, column=0, sticky="ew", pady=(10, 10))
        self.producto_form_frame.grid_columnconfigure([1, 3, 5, 7, 9, 11], weight=1)
        form_frame = self.producto_form_frame  # Alias para no cambiar resto del código
        
        # Título del formulario
        form_title = Label(form_frame, text="Datos del Producto", 
                          font=("Arial", 14, "bold"), bg="white", fg="#2c3e50")
        form_title.grid(row=0, column=0, columnspan=12, pady=10, sticky="ew")
        
        # Campos del formulario en dos filas para mejor organización
        campos = ["ID", "Nombre", "Precio", "Cantidad", "Departamento", "Almacén"]
        self.producto_entries = {}
        
        # Primera fila: ID, Nombre, Precio
        for i, campo in enumerate(campos[:3]):
            Label(form_frame, text=campo + ":", font=("Arial", 11, "bold"), 
                 bg="white", fg="#34495e").grid(row=1, column=i*2, padx=(15, 5), pady=10, sticky="e")
            entry_container = crear_entry_redondeado(
                form_frame,
                width=180,
                height=38,
                corner_radius=BORDE_REDONDEADO
            )
            entry_container.grid(row=1, column=i*2+1, padx=(0, 15), pady=10, sticky="ew")
            self.producto_entries[campo.lower().replace("ó", "o").replace("é", "e")] = entry_container.entry
        
        # Segunda fila: Cantidad, Departamento, Almacén
        for i, campo in enumerate(campos[3:], 3):
            Label(form_frame, text=campo + ":", font=("Arial", 11, "bold"), 
                 bg="white", fg="#34495e").grid(row=2, column=(i-3)*2, padx=(15, 5), pady=10, sticky="e")
            entry_container = crear_entry_redondeado(
                form_frame,
                width=180,
                height=38,
                corner_radius=BORDE_REDONDEADO
            )
            entry_container.grid(row=2, column=(i-3)*2+1, padx=(0, 15), pady=10, sticky="ew")
            self.producto_entries[campo.lower().replace("ó", "o").replace("é", "e")] = entry_container.entry
        
        # Texto informativo de almacenes
        self.info_almacenes_label = Label(form_frame, text="", 
                                         font=("Arial", 8), bg="white", fg="#7f8c8d",
                                         wraplength=900, justify="left")
        self.info_almacenes_label.grid(row=3, column=0, columnspan=12, padx=15, pady=(5, 5), sticky="w")
        
        # Botones de acción con colores UNISON y bordes redondeados
        btn_form_frame = Frame(form_frame, bg="white")
        btn_form_frame.grid(row=4, column=0, columnspan=12, pady=15)
        
        self.btn_agregar_producto = crear_boton_redondeado_canvas(
            btn_form_frame,
            texto="✅ Agregar Producto",
            comando=None,
            width=220,
            height=45,
            corner_radius=BORDE_REDONDEADO,
            estilo="primario"
        )
        self.btn_agregar_producto.pack(side="left", padx=12)
        
        self.btn_eliminar_producto = crear_boton_redondeado_canvas(
            btn_form_frame,
            texto="❌ Eliminar Producto",
            comando=None,
            width=220,
            height=45,
            corner_radius=BORDE_REDONDEADO,
            estilo="custom",
            bg_custom="#c0392b",
            hover_custom="#a93226"
        )
        self.btn_eliminar_producto.pack(side="left", padx=12)
        
        # Frame para la tabla con título
        table_frame = Frame(contenedor_principal, bg="white", relief="raised", bd=1)
        table_frame.grid(row=2, column=0, sticky="nsew")
        table_frame.grid_rowconfigure(1, weight=1)
        table_frame.grid_columnconfigure(0, weight=1)
        
        # Título de la tabla simplificado
        table_title = Label(table_frame, text="Lista de Productos", 
                           font=("Arial", 14, "bold"), bg="white", fg="#2c3e50")
        table_title.grid(row=0, column=0, pady=10, sticky="ew")
        
        # Frame interno para treeview y scrollbar
        tree_container = Frame(table_frame, bg="white")
        tree_container.grid(row=1, column=0, sticky="nsew", padx=15, pady=(0, 15))
        tree_container.grid_rowconfigure(0, weight=1)
        tree_container.grid_columnconfigure(0, weight=1)
        
        # Configurar Treeview con estilo mejorado
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 11, "bold"), background="#ecf0f1")
        style.configure("Treeview", font=("Arial", 10), rowheight=25)
        
        columns = ("id", "nombre", "precio", "cantidad", "departamento", "almacen", "fecha_modificacion", "usuario_modificacion")
        self.productos_tree = ttk.Treeview(tree_container, columns=columns, show="headings")
        
        # Configurar encabezados y anchos responsivos
        headings = ["ID", "Nombre", "Precio", "Cantidad", "Departamento", "Almacén", "Fecha Modificación", "Usuario"]
        widths = [50, 150, 80, 80, 120, 80, 150, 100]
        
        for col, heading, width in zip(columns, headings, widths):
            self.productos_tree.heading(col, text=heading, 
                command=lambda c=col: self.ordenar_productos(c))
            self.productos_tree.column(col, width=width, anchor="center")
        
        # Scrollbars
        v_scrollbar = ttk.Scrollbar(tree_container, orient="vertical", command=self.productos_tree.yview)
        h_scrollbar = ttk.Scrollbar(tree_container, orient="horizontal", command=self.productos_tree.xview)
        self.productos_tree.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        
        # Grid del treeview y scrollbars
        self.productos_tree.grid(row=0, column=0, sticky="nsew")
        v_scrollbar.grid(row=0, column=1, sticky="ns")
        h_scrollbar.grid(row=1, column=0, sticky="ew")
        
        # Bind para selección de productos
        self.productos_tree.bind("<<TreeviewSelect>>", self.on_producto_select)
        
        return frame
    
    def create_almacenes_frame(self):
        """Crea el frame de gestión de almacenes"""
        frame = Frame(self.container, bg=COLOR_FONDO_CLARO)
        # No hacer grid aquí - se hará en show_frame()
        
        # Configurar grid responsivo
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=0)  # Panel de filtros
        frame.grid_columnconfigure(1, weight=1)  # Contenido principal
        
        # ===== PANEL LATERAL DE FILTROS ALMACENES =====
        self.panel_filtros_almacenes = Frame(frame, bg="white", relief="raised", bd=1, width=240)
        self.panel_filtros_almacenes.grid(row=0, column=0, sticky="nsew", padx=(10, 0), pady=10)
        self.panel_filtros_almacenes.grid_propagate(False)
        
        # Header del panel de filtros
        filtros_alm_header = Frame(self.panel_filtros_almacenes, bg=COLOR_AZUL_UNISON, height=40)
        filtros_alm_header.pack(fill="x")
        
        Label(filtros_alm_header, text="🔍 Filtros", font=(FUENTE_UNISON, 11, "bold"),
              bg=COLOR_AZUL_UNISON, fg=COLOR_TEXTO_BLANCO).pack(side="left", padx=10, pady=8)
        
        self.btn_toggle_filtros_alm = crear_boton_redondeado_canvas(
            filtros_alm_header, texto="◀", comando=self.toggle_filtros_almacenes,
            width=35, height=25, corner_radius=5, estilo="dorado"
        )
        self.btn_toggle_filtros_alm.pack(side="right", padx=8, pady=8)
        
        # Contenedor directo para filtros sin scrollbar
        filtros_alm_scroll_frame = Frame(self.panel_filtros_almacenes, bg="white")
        filtros_alm_scroll_frame.pack(fill="both", expand=True, padx=8, pady=5)
        
        # ===== FILTROS INDIVIDUALES ALMACENES =====
        # Búsqueda por nombre
        Label(filtros_alm_scroll_frame, text="Buscar:", font=("Arial", 8, "bold"),
              bg="white", fg="#2c3e50", anchor="w").pack(fill="x", padx=5, pady=(8, 1))
        buscar_alm_container = crear_entry_redondeado(filtros_alm_scroll_frame, width=210, height=28, corner_radius=5)
        buscar_alm_container.pack(padx=5, pady=(0, 6))
        self.filtro_buscar_almacen = buscar_alm_container.entry
        self.filtro_buscar_almacen.bind('<KeyRelease>', lambda e: self.aplicar_filtros_almacenes())
        
        ttk.Separator(filtros_alm_scroll_frame, orient='horizontal').pack(fill='x', padx=8, pady=3)
        
        # Usuario que modificó (Combobox)
        Label(filtros_alm_scroll_frame, text="Usuario:", font=("Arial", 8, "bold"),
              bg="white", fg="#2c3e50", anchor="w").pack(fill="x", padx=5, pady=(3, 1))
        
        usuario_alm_combo_frame = Frame(filtros_alm_scroll_frame, bg="white")
        usuario_alm_combo_frame.pack(fill="x", padx=5, pady=(0, 6))
        
        self.filtro_usuario_alm_combo = ttk.Combobox(usuario_alm_combo_frame, state="readonly", width=27, font=("Arial", 8))
        self.filtro_usuario_alm_combo.pack(fill="x")
        self.filtro_usuario_alm_combo.set("Todos")
        self.filtro_usuario_alm_combo.bind('<<ComboboxSelected>>', lambda e: self.aplicar_filtros_almacenes())
        
        # Rango de fechas
        Label(filtros_alm_scroll_frame, text="Fecha modificación:", font=("Arial", 8, "bold"),
              bg="white", fg="#2c3e50", anchor="w").pack(fill="x", padx=5, pady=(3, 1))
        
        fecha_alm_frame = Frame(filtros_alm_scroll_frame, bg="white")
        fecha_alm_frame.pack(fill="x", padx=5, pady=(0, 6))
        
        Label(fecha_alm_frame, text="Desde:", font=("Arial", 7), bg="white", fg="#7f8c8d").grid(row=0, column=0, sticky="w")
        self.filtro_fecha_desde_alm = DateEntry(fecha_alm_frame, width=16, background=COLOR_AZUL_UNISON,
                                                 foreground='white', borderwidth=2, font=("Arial", 7),
                                                 date_pattern='yyyy-mm-dd')
        self.filtro_fecha_desde_alm.grid(row=0, column=1, padx=(3, 0), pady=(0, 3))
        self.filtro_fecha_desde_alm.bind('<<DateEntrySelected>>', lambda e: self.aplicar_filtros_almacenes())
        
        Label(fecha_alm_frame, text="Hasta:", font=("Arial", 7), bg="white", fg="#7f8c8d").grid(row=1, column=0, sticky="w")
        self.filtro_fecha_hasta_alm = DateEntry(fecha_alm_frame, width=16, background=COLOR_AZUL_UNISON,
                                                 foreground='white', borderwidth=2, font=("Arial", 7),
                                                 date_pattern='yyyy-mm-dd')
        self.filtro_fecha_hasta_alm.grid(row=1, column=1, padx=(3, 0))
        self.filtro_fecha_hasta_alm.bind('<<DateEntrySelected>>', lambda e: self.aplicar_filtros_almacenes())
        
        # Checkbox para habilitar/deshabilitar filtro de fecha
        self.fecha_habilitada_alm = BooleanVar(value=False)
        self.chk_fecha_alm = Checkbutton(fecha_alm_frame, text="Aplicar", variable=self.fecha_habilitada_alm,
                                         bg="white", font=("Arial", 7), command=self.aplicar_filtros_almacenes)
        self.chk_fecha_alm.grid(row=0, column=2, rowspan=2, padx=(5, 0))
        
        ttk.Separator(filtros_alm_scroll_frame, orient='horizontal').pack(fill='x', padx=8, pady=5)
        
        # Botones de acción
        self.btn_limpiar_filtros_alm = crear_boton_redondeado_canvas(
            filtros_alm_scroll_frame, texto="Limpiar", comando=self.limpiar_filtros_almacenes,
            width=210, height=30, corner_radius=5, estilo="custom",
            bg_custom="#95a5a6", hover_custom="#7f8c8d"
        )
        self.btn_limpiar_filtros_alm.pack(padx=5, pady=(3, 5))
        
        # Contador de resultados
        self.lbl_resultados_almacenes = Label(
            filtros_alm_scroll_frame, text="0 almacenes", font=("Arial", 7, "italic"),
            bg="white", fg="#7f8c8d", wraplength=200
        )
        self.lbl_resultados_almacenes.pack(padx=5, pady=(3, 8))
        
        # Botón flotante para mostrar filtros cuando están ocultos
        self.btn_mostrar_filtros_alm = crear_boton_redondeado_canvas(
            frame, texto="▶", comando=self.toggle_filtros_almacenes,
            width=30, height=40, corner_radius=5, estilo="primario"
        )
        # Inicialmente oculto
        
        # ===== CONTENEDOR PRINCIPAL ALMACENES (DERECHA) =====
        contenedor_alm_principal = Frame(frame, bg=COLOR_FONDO_CLARO)
        contenedor_alm_principal.grid(row=0, column=1, sticky="nsew", padx=(8, 10), pady=10)
        contenedor_alm_principal.grid_rowconfigure(2, weight=1)
        contenedor_alm_principal.grid_columnconfigure(0, weight=1)
        
        # Header con colores UNISON
        header_frame = Frame(contenedor_alm_principal, bg=COLOR_AZUL_UNISON, height=60)
        header_frame.grid(row=0, column=0, sticky="ew")
        header_frame.grid_propagate(False)
        header_frame.grid_columnconfigure(1, weight=1)
        
        # Título con icono
        titulo = Label(header_frame, text="🏪 Gestión de Almacenes", 
                      font=(FUENTE_UNISON, 20, "bold"), bg=COLOR_AZUL_UNISON, fg=COLOR_TEXTO_BLANCO)
        titulo.grid(row=0, column=0, sticky="w", padx=25, pady=15)
        
        # Botón de volver discreto
        self.btn_volver_almacenes = crear_boton_redondeado_canvas(
            header_frame,
            texto="⬅ Volver",
            comando=lambda: self.show_frame("inicio"),
            width=120,
            height=35,
            corner_radius=BORDE_REDONDEADO,
            estilo="dorado"
        )
        self.btn_volver_almacenes.grid(row=0, column=1, sticky="e", padx=25, pady=12)
        
        # Frame para formulario con mejor organización
        self.almacen_form_frame = Frame(contenedor_alm_principal, bg="white", relief="raised", bd=1)
        self.almacen_form_frame.grid(row=1, column=0, sticky="ew", pady=(10, 10))
        self.almacen_form_frame.grid_columnconfigure([1, 3], weight=1)
        form_frame = self.almacen_form_frame  # Alias para no cambiar resto del código
        
        # Título del formulario
        form_title = Label(form_frame, text="Datos del Almacén", 
                          font=("Arial", 14, "bold"), bg="white", fg="#2c3e50")
        form_title.grid(row=0, column=0, columnspan=4, pady=15, sticky="ew")
        
        # Campos del formulario centrados
        self.almacen_entries = {}
        
        # Frame centrado para los campos
        campos_frame = Frame(form_frame, bg="white")
        campos_frame.grid(row=1, column=0, columnspan=4, pady=10)
        
        Label(campos_frame, text="ID:", font=("Arial", 12, "bold"), 
             bg="white", fg="#34495e").grid(row=0, column=0, padx=(0, 10), pady=15, sticky="e")
        id_entry_container = crear_entry_redondeado(
            campos_frame,
            width=220,
            height=42,
            corner_radius=BORDE_REDONDEADO
        )
        id_entry_container.grid(row=0, column=1, padx=(0, 30), pady=15, sticky="ew")
        self.almacen_entries["id"] = id_entry_container.entry
        
        
        Label(campos_frame, text="Nombre:", font=("Arial", 12, "bold"), 
             bg="white", fg="#34495e").grid(row=0, column=2, padx=(0, 10), pady=15, sticky="e")
        nombre_entry_container = crear_entry_redondeado(
            campos_frame,
            width=320,
            height=42,
            corner_radius=BORDE_REDONDEADO
        )
        nombre_entry_container.grid(row=0, column=3, padx=0, pady=15, sticky="ew")
        self.almacen_entries["nombre"] = nombre_entry_container.entry
        
        
        # Botones de acción con colores UNISON y bordes redondeados
        btn_form_frame = Frame(form_frame, bg="white")
        btn_form_frame.grid(row=2, column=0, columnspan=4, pady=15)
        
        self.btn_agregar_almacen = crear_boton_redondeado_canvas(
            btn_form_frame,
            texto="✅ Agregar Almacén",
            comando=None,
            width=220,
            height=45,
            corner_radius=BORDE_REDONDEADO,
            estilo="primario"
        )
        self.btn_agregar_almacen.pack(side="left", padx=12)
        
        self.btn_eliminar_almacen = crear_boton_redondeado_canvas(
            btn_form_frame,
            texto="❌ Eliminar Almacén",
            comando=None,
            width=220,
            height=45,
            corner_radius=BORDE_REDONDEADO,
            estilo="custom",
            bg_custom="#c0392b",
            hover_custom="#a93226"
        )
        self.btn_eliminar_almacen.pack(side="left", padx=12)
        
        # Frame para la tabla con título
        table_frame = Frame(contenedor_alm_principal, bg="white", relief="raised", bd=1)
        table_frame.grid(row=2, column=0, sticky="nsew")
        table_frame.grid_rowconfigure(1, weight=1)
        table_frame.grid_columnconfigure(0, weight=1)
        
        # Título de la tabla simplificado
        table_title = Label(table_frame, text="Lista de Almacenes", 
                           font=("Arial", 14, "bold"), bg="white", fg="#2c3e50")
        table_title.grid(row=0, column=0, pady=10, sticky="ew")
        
        # Frame interno para treeview y scrollbar
        tree_container = Frame(table_frame, bg="white")
        tree_container.grid(row=1, column=0, sticky="nsew", padx=15, pady=(0, 15))
        tree_container.grid_rowconfigure(0, weight=1)
        tree_container.grid_columnconfigure(0, weight=1)
        
        # Configurar Treeview
        columns = ("id", "nombre", "fecha_modificacion", "usuario_modificacion")
        self.almacenes_tree = ttk.Treeview(tree_container, columns=columns, show="headings")
        
        # Configurar encabezados con mejor distribución y ordenamiento
        self.almacenes_tree.heading("id", text="ID", 
            command=lambda: self.ordenar_almacenes("id"))
        self.almacenes_tree.heading("nombre", text="Nombre del Almacén", 
            command=lambda: self.ordenar_almacenes("nombre"))
        self.almacenes_tree.heading("fecha_modificacion", text="Fecha Modificación", 
            command=lambda: self.ordenar_almacenes("fecha_modificacion"))
        self.almacenes_tree.heading("usuario_modificacion", text="Usuario", 
            command=lambda: self.ordenar_almacenes("usuario_modificacion"))
        self.almacenes_tree.column("id", width=80, anchor="center")
        self.almacenes_tree.column("nombre", width=250, anchor="center")
        self.almacenes_tree.column("fecha_modificacion", width=150, anchor="center")
        self.almacenes_tree.column("usuario_modificacion", width=120, anchor="center")
        
        # Scrollbars
        v_scrollbar_almacenes = ttk.Scrollbar(tree_container, orient="vertical", command=self.almacenes_tree.yview)
        h_scrollbar_almacenes = ttk.Scrollbar(tree_container, orient="horizontal", command=self.almacenes_tree.xview)
        self.almacenes_tree.configure(yscrollcommand=v_scrollbar_almacenes.set, xscrollcommand=h_scrollbar_almacenes.set)
        
        # Grid del treeview y scrollbars
        self.almacenes_tree.grid(row=0, column=0, sticky="nsew")
        v_scrollbar_almacenes.grid(row=0, column=1, sticky="ns")
        h_scrollbar_almacenes.grid(row=1, column=0, sticky="ew")
        
        # Bind para selección de almacenes
        self.almacenes_tree.bind("<<TreeviewSelect>>", self.on_almacen_select)
        
        return frame
    
    def show_frame(self, frame_name):
        """Muestra el frame especificado y oculta los demás"""
        # Ocultar todos los frames primero
        for name, frame in self.frames.items():
            frame.grid_remove()
        
        # Mostrar solo el frame solicitado
        frame = self.frames[frame_name]
        frame.grid(row=0, column=0, sticky="nsew")
    
    def update_productos_tree(self, productos):
        """Actualiza el Treeview de productos con los datos proporcionados"""
        # Cachear datos originales sin filtrar
        self.productos_data_original = list(productos)
        self.productos_data_cache = list(productos)
        
        # Actualizar combobox de usuarios con valores únicos
        if hasattr(self, 'filtro_usuario_prod'):
            usuarios_unicos = set(["Todos"])
            for producto in productos:
                if producto[7]:  # columna 7 es ultimo_usuario_modificacion
                    usuarios_unicos.add(str(producto[7]))
            self.filtro_usuario_prod['values'] = sorted(list(usuarios_unicos))
        
        # Aplicar filtros si existen
        self.aplicar_filtros_productos()
    
    def update_almacenes_tree(self, almacenes):
        """Actualiza el Treeview de almacenes con los datos proporcionados"""
        # Cachear datos originales sin filtrar
        self.almacenes_data_original = list(almacenes)
        self.almacenes_data_cache = list(almacenes)
        
        # Actualizar combobox de usuarios con valores únicos
        if hasattr(self, 'filtro_usuario_alm_combo'):
            usuarios_unicos_alm = set(["Todos"])
            for almacen in almacenes:
                if almacen[3]:  # columna 3 es ultimo_usuario_modificacion
                    usuarios_unicos_alm.add(str(almacen[3]))
            self.filtro_usuario_alm_combo['values'] = sorted(list(usuarios_unicos_alm))
        
        # Aplicar filtros si existen
        self.aplicar_filtros_almacenes()
    
    def on_producto_select(self, event):
        """Maneja la selección de un producto en el Treeview"""
        selection = self.productos_tree.selection()
        if selection:
            item = self.productos_tree.item(selection[0])
            values = item['values']
            
            # Llenar los campos del formulario con los datos del producto seleccionado
            self.producto_entries['id'].delete(0, 'end')
            self.producto_entries['id'].insert(0, str(values[0]))
            
            self.producto_entries['nombre'].delete(0, 'end')
            self.producto_entries['nombre'].insert(0, str(values[1]))
            
            self.producto_entries['precio'].delete(0, 'end')
            self.producto_entries['precio'].insert(0, str(values[2]))
            
            self.producto_entries['cantidad'].delete(0, 'end')
            self.producto_entries['cantidad'].insert(0, str(values[3]))
            
            self.producto_entries['departamento'].delete(0, 'end')
            self.producto_entries['departamento'].insert(0, str(values[4]))
            
            self.producto_entries['almacen'].delete(0, 'end')
            self.producto_entries['almacen'].insert(0, str(values[5]))
    
    def on_almacen_select(self, event):
        """Maneja la selección de un almacén en el Treeview"""
        selection = self.almacenes_tree.selection()
        if selection:
            item = self.almacenes_tree.item(selection[0])
            values = item['values']
            
            # Llenar los campos del formulario con los datos del almacén seleccionado
            self.almacen_entries['id'].delete(0, 'end')
            self.almacen_entries['id'].insert(0, str(values[0]))
            
            self.almacen_entries['nombre'].delete(0, 'end')
            self.almacen_entries['nombre'].insert(0, str(values[1]))
    
    def limpiar_formulario_producto(self):
        """Limpia todos los campos del formulario de productos"""
        for entry in self.producto_entries.values():
            entry.delete(0, 'end')
    
    def limpiar_formulario_almacen(self):
        """Limpia los campos del formulario de almacenes"""
        for entry in self.almacen_entries.values():
            entry.delete(0, 'end')
    
    def ordenar_productos(self, columna):
        """Ordena los productos por la columna especificada"""
        if not self.productos_data_cache:
            return
        
        # Mapeo de columnas a índices
        columnas_map = {
            "id": 0,
            "nombre": 1,
            "precio": 2,
            "cantidad": 3,
            "departamento": 4,
            "almacen": 5,
            "fecha_modificacion": 6,
            "usuario_modificacion": 7
        }
        
        col_index = columnas_map.get(columna, 0)
        
        # Determinar orden (alternar entre ascendente y descendente)
        if columna in self.productos_orden and self.productos_orden[columna] == 'asc':
            orden = 'desc'
            reverse = True
        else:
            orden = 'asc'
            reverse = False
        
        self.productos_orden = {columna: orden}  # Solo mantener orden de columna actual
        
        # Ordenar datos según el tipo de columna
        try:
            if columna in ['id', 'cantidad']:
                # Ordenar como números
                datos_ordenados = sorted(self.productos_data_cache, 
                    key=lambda x: int(x[col_index]) if x[col_index] else 0, 
                    reverse=reverse)
            elif columna == 'precio':
                # Ordenar como números decimales
                datos_ordenados = sorted(self.productos_data_cache, 
                    key=lambda x: float(x[col_index]) if x[col_index] else 0.0, 
                    reverse=reverse)
            else:
                # Ordenar como texto (nombre, departamento, almacén, fecha, usuario)
                datos_ordenados = sorted(self.productos_data_cache, 
                    key=lambda x: str(x[col_index]).lower() if x[col_index] else '', 
                    reverse=reverse)
        except (ValueError, TypeError):
            # Si hay error en conversión, ordenar como texto
            datos_ordenados = sorted(self.productos_data_cache, 
                key=lambda x: str(x[col_index]).lower() if x[col_index] else '', 
                reverse=reverse)
        
        # Actualizar encabezado con indicador visual
        headings = ["ID", "Nombre", "Precio", "Cantidad", "Departamento", "Almacén", "Fecha Modificación", "Usuario"]
        columnas = ["id", "nombre", "precio", "cantidad", "departamento", "almacen", "fecha_modificacion", "usuario_modificacion"]
        
        for i, col in enumerate(columnas):
            if col == columna:
                indicador = " ▲" if orden == 'asc' else " ▼"
                self.productos_tree.heading(col, text=headings[i] + indicador)
            else:
                self.productos_tree.heading(col, text=headings[i])
        
        # Limpiar y reinsertar datos ordenados
        for item in self.productos_tree.get_children():
            self.productos_tree.delete(item)
        
        for producto in datos_ordenados:
            self.productos_tree.insert("", "end", values=producto)
    
    def ordenar_almacenes(self, columna):
        """Ordena los almacenes por la columna especificada"""
        if not self.almacenes_data_cache:
            return
        
        # Mapeo de columnas a índices
        columnas_map = {
            "id": 0,
            "nombre": 1,
            "fecha_modificacion": 2,
            "usuario_modificacion": 3
        }
        
        col_index = columnas_map.get(columna, 0)
        
        # Determinar orden (alternar entre ascendente y descendente)
        if columna in self.almacenes_orden and self.almacenes_orden[columna] == 'asc':
            orden = 'desc'
            reverse = True
        else:
            orden = 'asc'
            reverse = False
        
        self.almacenes_orden = {columna: orden}  # Solo mantener orden de columna actual
        
        # Ordenar datos según el tipo de columna
        try:
            if columna == 'id':
                # Ordenar como números
                datos_ordenados = sorted(self.almacenes_data_cache, 
                    key=lambda x: int(x[col_index]) if x[col_index] else 0, 
                    reverse=reverse)
            else:
                # Ordenar como texto (nombre, fecha, usuario)
                datos_ordenados = sorted(self.almacenes_data_cache, 
                    key=lambda x: str(x[col_index]).lower() if x[col_index] else '', 
                    reverse=reverse)
        except (ValueError, TypeError):
            # Si hay error en conversión, ordenar como texto
            datos_ordenados = sorted(self.almacenes_data_cache, 
                key=lambda x: str(x[col_index]).lower() if x[col_index] else '', 
                reverse=reverse)
        
        # Actualizar encabezado con indicador visual
        headings_map = {
            "id": "ID",
            "nombre": "Nombre del Almacén",
            "fecha_modificacion": "Fecha Modificación",
            "usuario_modificacion": "Usuario"
        }
        
        for col in columnas_map.keys():
            if col == columna:
                indicador = " ▲" if orden == 'asc' else " ▼"
                self.almacenes_tree.heading(col, text=headings_map[col] + indicador)
            else:
                self.almacenes_tree.heading(col, text=headings_map[col])
        
        # Limpiar y reinsertar datos ordenados
        for item in self.almacenes_tree.get_children():
            self.almacenes_tree.delete(item)
        
        for almacen in datos_ordenados:
            self.almacenes_tree.insert("", "end", values=almacen)
    
    def get_producto_data(self):
        """Obtiene los datos del formulario de productos"""
        return {
            'id': self.producto_entries['id'].get().strip(),
            'nombre': self.producto_entries['nombre'].get().strip(),
            'precio': self.producto_entries['precio'].get().strip(),
            'cantidad': self.producto_entries['cantidad'].get().strip(),
            'departamento': self.producto_entries['departamento'].get().strip(),
            'almacen': self.producto_entries['almacen'].get().strip()
        }
    
    def get_almacen_data(self):
        """Obtiene los datos del formulario de almacenes"""
        return {
            'id': self.almacen_entries['id'].get().strip(),
            'nombre': self.almacen_entries['nombre'].get().strip()
        }
    
    # ===== FUNCIONES DE FILTRADO =====
    def aplicar_filtros_productos(self):
        """Aplica todos los filtros activos a los productos"""
        if not self.productos_data_original:
            return
        
        datos_filtrados = list(self.productos_data_original)
        
        # Filtro de búsqueda general (busca en nombre)
        if hasattr(self, 'filtro_buscar_producto'):
            texto_buscar = self.filtro_buscar_producto.get().strip().lower()
            if texto_buscar:
                datos_filtrados = [p for p in datos_filtrados 
                                 if texto_buscar in str(p[1]).lower()]  # p[1] = nombre
        
        # Filtro por departamento
        if hasattr(self, 'filtro_departamento'):
            departamento = self.filtro_departamento.get().strip().lower()
            if departamento:
                datos_filtrados = [p for p in datos_filtrados 
                                 if departamento in str(p[4]).lower()]  # p[4] = departamento
        
        # Filtro por almacén
        if hasattr(self, 'filtro_almacen_producto'):
            almacen = self.filtro_almacen_producto.get().strip().lower()
            if almacen:
                datos_filtrados = [p for p in datos_filtrados 
                                 if almacen in str(p[5]).lower()]  # p[5] = almacén
        
        # Filtro por precio mínimo
        if hasattr(self, 'filtro_precio_min'):
            precio_min_str = self.filtro_precio_min.get().strip()
            if precio_min_str:
                try:
                    precio_min = float(precio_min_str)
                    datos_filtrados = [p for p in datos_filtrados 
                                     if float(p[2]) >= precio_min]  # p[2] = precio
                except ValueError:
                    pass
        
        # Filtro por precio máximo
        if hasattr(self, 'filtro_precio_max'):
            precio_max_str = self.filtro_precio_max.get().strip()
            if precio_max_str:
                try:
                    precio_max = float(precio_max_str)
                    datos_filtrados = [p for p in datos_filtrados 
                                     if float(p[2]) <= precio_max]  # p[2] = precio
                except ValueError:
                    pass
        
        # Filtro por cantidad mínima
        if hasattr(self, 'filtro_cantidad_min'):
            cantidad_min_str = self.filtro_cantidad_min.get().strip()
            if cantidad_min_str:
                try:
                    cantidad_min = int(cantidad_min_str)
                    datos_filtrados = [p for p in datos_filtrados 
                                     if int(p[3]) >= cantidad_min]  # p[3] = cantidad
                except ValueError:
                    pass
        
        # Filtro por cantidad máxima
        if hasattr(self, 'filtro_cantidad_max'):
            cantidad_max_str = self.filtro_cantidad_max.get().strip()
            if cantidad_max_str:
                try:
                    cantidad_max = int(cantidad_max_str)
                    datos_filtrados = [p for p in datos_filtrados 
                                     if int(p[3]) <= cantidad_max]  # p[3] = cantidad
                except ValueError:
                    pass
        
        # Filtro por usuario
        if hasattr(self, 'filtro_usuario_prod'):
            usuario_seleccionado = self.filtro_usuario_prod.get()
            if usuario_seleccionado and usuario_seleccionado != "Todos":
                datos_filtrados = [p for p in datos_filtrados 
                                 if str(p[7]) == usuario_seleccionado]  # p[7] = ultimo_usuario_modificacion
        
        # Filtro por rango de fechas
        if hasattr(self, 'fecha_habilitada_prod') and self.fecha_habilitada_prod.get():
            try:
                fecha_desde = self.filtro_fecha_desde_prod.get_date()
                fecha_hasta = self.filtro_fecha_hasta_prod.get_date()
                
                datos_temp = []
                for p in datos_filtrados:
                    try:
                        # p[6] = fecha_ultima_modificacion
                        if p[6]:
                            fecha_str = str(p[6])[:10]  # Tomar solo YYYY-MM-DD
                            fecha_registro = datetime.strptime(fecha_str, '%Y-%m-%d').date()
                            
                            if fecha_desde <= fecha_registro <= fecha_hasta:
                                datos_temp.append(p)
                    except (ValueError, IndexError):
                        # Si hay error al parsear la fecha, incluir el producto
                        datos_temp.append(p)
                
                datos_filtrados = datos_temp
            except Exception as e:
                print(f"Error al aplicar filtro de fecha: {e}")
        
        # Actualizar cache y vista
        self.productos_data_cache = datos_filtrados
        self._actualizar_tree_productos(datos_filtrados)
    
    def _actualizar_tree_productos(self, productos):
        """Método interno para actualizar solo el tree sin tocar cache original"""
        # Limpiar datos existentes
        for item in self.productos_tree.get_children():
            self.productos_tree.delete(item)
        
        # Insertar nuevos datos
        for producto in productos:
            self.productos_tree.insert("", "end", values=producto)
        
        # Actualizar contador
        if hasattr(self, 'lbl_resultados_productos'):
            total = len(self.productos_data_original)
            mostrados = len(productos)
            if total == mostrados:
                self.lbl_resultados_productos.config(text=f"{mostrados} productos")
            else:
                self.lbl_resultados_productos.config(text=f"{mostrados} de {total} productos")
    
    def limpiar_filtros_productos(self):
        """Limpia todos los filtros de productos"""
        if hasattr(self, 'filtro_buscar_producto'):
            self.filtro_buscar_producto.delete(0, 'end')
        if hasattr(self, 'filtro_departamento'):
            self.filtro_departamento.delete(0, 'end')
        if hasattr(self, 'filtro_almacen_producto'):
            self.filtro_almacen_producto.delete(0, 'end')
        if hasattr(self, 'filtro_precio_min'):
            self.filtro_precio_min.delete(0, 'end')
        if hasattr(self, 'filtro_precio_max'):
            self.filtro_precio_max.delete(0, 'end')
        if hasattr(self, 'filtro_cantidad_min'):
            self.filtro_cantidad_min.delete(0, 'end')
        if hasattr(self, 'filtro_cantidad_max'):
            self.filtro_cantidad_max.delete(0, 'end')
        if hasattr(self, 'filtro_usuario_prod'):
            self.filtro_usuario_prod.set("Todos")
        if hasattr(self, 'fecha_habilitada_prod'):
            self.fecha_habilitada_prod.set(False)
        
        # Restaurar todos los datos
        self.productos_data_cache = list(self.productos_data_original)
        self._actualizar_tree_productos(self.productos_data_cache)
    
    def aplicar_filtros_almacenes(self):
        """Aplica todos los filtros activos a los almacenes"""
        if not self.almacenes_data_original:
            return
        
        datos_filtrados = list(self.almacenes_data_original)
        
        # Filtro de búsqueda por nombre
        if hasattr(self, 'filtro_buscar_almacen'):
            texto_buscar = self.filtro_buscar_almacen.get().strip().lower()
            if texto_buscar:
                datos_filtrados = [a for a in datos_filtrados 
                                 if texto_buscar in str(a[1]).lower()]  # a[1] = nombre
        
        # Filtro por usuario (combobox)
        if hasattr(self, 'filtro_usuario_alm_combo'):
            usuario_seleccionado = self.filtro_usuario_alm_combo.get()
            if usuario_seleccionado and usuario_seleccionado != "Todos":
                datos_filtrados = [a for a in datos_filtrados 
                                 if str(a[3]) == usuario_seleccionado]  # a[3] = ultimo_usuario_modificacion
        
        # Filtro por rango de fechas
        if hasattr(self, 'fecha_habilitada_alm') and self.fecha_habilitada_alm.get():
            try:
                fecha_desde = self.filtro_fecha_desde_alm.get_date()
                fecha_hasta = self.filtro_fecha_hasta_alm.get_date()
                
                datos_temp = []
                for a in datos_filtrados:
                    try:
                        # a[2] = fecha_ultima_modificacion
                        if a[2]:
                            fecha_str = str(a[2])[:10]  # Tomar solo YYYY-MM-DD
                            fecha_registro = datetime.strptime(fecha_str, '%Y-%m-%d').date()
                            
                            if fecha_desde <= fecha_registro <= fecha_hasta:
                                datos_temp.append(a)
                    except (ValueError, IndexError):
                        # Si hay error al parsear la fecha, incluir el almacén
                        datos_temp.append(a)
                
                datos_filtrados = datos_temp
            except Exception as e:
                print(f"Error al aplicar filtro de fecha en almacenes: {e}")
        
        # Actualizar cache y vista
        self.almacenes_data_cache = datos_filtrados
        self._actualizar_tree_almacenes(datos_filtrados)
    
    def _actualizar_tree_almacenes(self, almacenes):
        """Método interno para actualizar solo el tree sin tocar cache original"""
        # Limpiar datos existentes
        for item in self.almacenes_tree.get_children():
            self.almacenes_tree.delete(item)
        
        # Insertar nuevos datos
        for almacen in almacenes:
            self.almacenes_tree.insert("", "end", values=almacen)
        
        # Actualizar contador
        if hasattr(self, 'lbl_resultados_almacenes'):
            total = len(self.almacenes_data_original)
            mostrados = len(almacenes)
            if total == mostrados:
                self.lbl_resultados_almacenes.config(text=f"{mostrados} almacenes")
            else:
                self.lbl_resultados_almacenes.config(text=f"{mostrados} de {total} almacenes")
    
    def limpiar_filtros_almacenes(self):
        """Limpia todos los filtros de almacenes"""
        if hasattr(self, 'filtro_buscar_almacen'):
            self.filtro_buscar_almacen.delete(0, 'end')
        if hasattr(self, 'filtro_usuario_alm_combo'):
            self.filtro_usuario_alm_combo.set("Todos")
        if hasattr(self, 'fecha_habilitada_alm'):
            self.fecha_habilitada_alm.set(False)
        
        # Restaurar todos los datos
        self.almacenes_data_cache = list(self.almacenes_data_original)
        self._actualizar_tree_almacenes(self.almacenes_data_cache)
    
    def toggle_filtros_productos(self):
        """Muestra/oculta el panel de filtros de productos"""
        if self.filtros_productos_visible:
            # Ocultar panel de filtros
            self.panel_filtros_productos.grid_remove()
            self.filtros_productos_visible = False
            # Mostrar botón flotante para volver a abrir
            if hasattr(self, 'btn_mostrar_filtros_prod'):
                self.btn_mostrar_filtros_prod.grid(row=0, column=0, sticky="nw", padx=10, pady=50)
        else:
            # Mostrar panel de filtros
            self.panel_filtros_productos.grid()
            self.filtros_productos_visible = True
            # Ocultar botón flotante
            if hasattr(self, 'btn_mostrar_filtros_prod'):
                self.btn_mostrar_filtros_prod.grid_remove()
    
    def toggle_filtros_almacenes(self):
        """Muestra/oculta el panel de filtros de almacenes"""
        if self.filtros_almacenes_visible:
            # Ocultar panel de filtros
            self.panel_filtros_almacenes.grid_remove()
            self.filtros_almacenes_visible = False
            # Mostrar botón flotante para volver a abrir
            if hasattr(self, 'btn_mostrar_filtros_alm'):
                self.btn_mostrar_filtros_alm.grid(row=0, column=0, sticky="nw", padx=10, pady=50)
        else:
            # Mostrar panel de filtros
            self.panel_filtros_almacenes.grid()
            self.filtros_almacenes_visible = True
            # Ocultar botón flotante
            if hasattr(self, 'btn_mostrar_filtros_alm'):
                self.btn_mostrar_filtros_alm.grid_remove()