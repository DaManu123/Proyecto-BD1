import tkinter as tk
from tkinter import ttk, Frame, Label, Button, Entry, Canvas
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
        frame.grid(row=0, column=0, sticky="nsew")
        
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
        frame.grid(row=0, column=0, sticky="nsew")
        
        # Configurar grid responsivo
        frame.grid_rowconfigure(2, weight=1)  # El treeview se expande
        frame.grid_columnconfigure(0, weight=1)
        
        # Header con colores UNISON
        header_frame = Frame(frame, bg=COLOR_AZUL_UNISON, height=60)
        header_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=(10, 0))
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
        self.producto_form_frame = Frame(frame, bg="white", relief="raised", bd=1)
        self.producto_form_frame.grid(row=1, column=0, sticky="ew", padx=10, pady=10)
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
            entry = Entry(form_frame, width=15, font=(FUENTE_UNISON, 11), 
                         relief="flat", bd=0, highlightthickness=2,
                         highlightcolor=COLOR_AZUL_UNISON, highlightbackground=COLOR_GRIS_CLARO)
            entry.grid(row=1, column=i*2+1, padx=(0, 15), pady=10, ipady=5, sticky="ew")
            self.producto_entries[campo.lower().replace("ó", "o").replace("é", "e")] = entry
        
        # Segunda fila: Cantidad, Departamento, Almacén
        for i, campo in enumerate(campos[3:], 3):
            Label(form_frame, text=campo + ":", font=("Arial", 11, "bold"), 
                 bg="white", fg="#34495e").grid(row=2, column=(i-3)*2, padx=(15, 5), pady=10, sticky="e")
            entry = Entry(form_frame, width=15, font=(FUENTE_UNISON, 11),
                         relief="flat", bd=0, highlightthickness=2,
                         highlightcolor=COLOR_AZUL_UNISON, highlightbackground=COLOR_GRIS_CLARO)
            entry.grid(row=2, column=(i-3)*2+1, padx=(0, 15), pady=10, ipady=5, sticky="ew")
            self.producto_entries[campo.lower().replace("ó", "o").replace("é", "e")] = entry
        
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
        table_frame = Frame(frame, bg="white", relief="raised", bd=1)
        table_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=(0, 10))
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
            self.productos_tree.heading(col, text=heading)
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
        frame.grid(row=0, column=0, sticky="nsew")
        
        # Configurar grid responsivo
        frame.grid_rowconfigure(2, weight=1)  # El treeview se expande
        frame.grid_columnconfigure(0, weight=1)
        
        # Header con colores UNISON
        header_frame = Frame(frame, bg=COLOR_AZUL_UNISON, height=60)
        header_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=(10, 0))
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
        self.almacen_form_frame = Frame(frame, bg="white", relief="raised", bd=1)
        self.almacen_form_frame.grid(row=1, column=0, sticky="ew", padx=10, pady=10)
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
        id_entry = Entry(campos_frame, width=20, font=(FUENTE_UNISON, 12),
                        relief="flat", bd=0, highlightthickness=2,
                        highlightcolor=COLOR_AZUL_UNISON, highlightbackground=COLOR_GRIS_CLARO)
        id_entry.grid(row=0, column=1, padx=(0, 30), pady=15, ipady=5, sticky="ew")
        self.almacen_entries["id"] = id_entry
        
        Label(campos_frame, text="Nombre:", font=("Arial", 12, "bold"), 
             bg="white", fg="#34495e").grid(row=0, column=2, padx=(0, 10), pady=15, sticky="e")
        nombre_entry = Entry(campos_frame, width=30, font=(FUENTE_UNISON, 12),
                            relief="flat", bd=0, highlightthickness=2,
                            highlightcolor=COLOR_AZUL_UNISON, highlightbackground=COLOR_GRIS_CLARO)
        nombre_entry.grid(row=0, column=3, padx=0, pady=15, ipady=5, sticky="ew")
        self.almacen_entries["nombre"] = nombre_entry
        
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
        table_frame = Frame(frame, bg="white", relief="raised", bd=1)
        table_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=(0, 10))
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
        
        # Configurar encabezados con mejor distribución
        self.almacenes_tree.heading("id", text="ID")
        self.almacenes_tree.heading("nombre", text="Nombre del Almacén")
        self.almacenes_tree.heading("fecha_modificacion", text="Fecha Modificación")
        self.almacenes_tree.heading("usuario_modificacion", text="Usuario")
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
        frame = self.frames[frame_name]
        frame.tkraise()
    
    def update_productos_tree(self, productos):
        """Actualiza el Treeview de productos con los datos proporcionados"""
        # Limpiar datos existentes
        for item in self.productos_tree.get_children():
            self.productos_tree.delete(item)
        
        # Insertar nuevos datos
        for producto in productos:
            self.productos_tree.insert("", "end", values=producto)
    
    def update_almacenes_tree(self, almacenes):
        """Actualiza el Treeview de almacenes con los datos proporcionados"""
        # Limpiar datos existentes
        for item in self.almacenes_tree.get_children():
            self.almacenes_tree.delete(item)
        
        # Insertar nuevos datos
        for almacen in almacenes:
            self.almacenes_tree.insert("", "end", values=almacen)
    
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
        """Limpia todos los campos del formulario de almacenes"""
        for entry in self.almacen_entries.values():
            entry.delete(0, 'end')
    
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