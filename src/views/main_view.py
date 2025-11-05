import tkinter as tk
from tkinter import ttk, Frame, Label, Button, Entry, Canvas
import os

class MainView:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de Inventario - Universidad de Sonora - Manuel Munguia Rubio")
        self.master.geometry("900x650")
        self.master.configure(bg="#f0f0f0")
        self.master.resizable(True, True)
        self.master.minsize(750, 550)
        
        # Intentar establecer el icono de la ventana con el logo
        try:
            logo_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'unilogo.gif')
            if os.path.exists(logo_path):
                icon = tk.PhotoImage(file=logo_path)
                self.master.iconphoto(True, icon)
        except Exception as e:
            print(f"No se pudo establecer el icono: {e}")
        
        # Configurar el grid principal para que sea responsivo
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        
        # Contenedor principal para todos los frames
        self.container = Frame(self.master, bg="#f0f0f0")
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
        frame = Frame(self.container, bg="#f0f0f0")
        frame.grid(row=0, column=0, sticky="nsew")
        
        # Configurar el grid principal
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        
        # Crear Canvas y Scrollbar para scroll vertical
        canvas = tk.Canvas(frame, bg="#f0f0f0", highlightthickness=0)
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollable_frame = Frame(canvas, bg="#f0f0f0")
        
        # Configurar el scroll
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Grid del canvas y scrollbar
        canvas.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")
        
        # Configurar el frame scrollable para que sea responsivo
        scrollable_frame.grid_columnconfigure(0, weight=1)
        
        # Contenido principal dentro del frame scrollable
        main_content = Frame(scrollable_frame, bg="#f0f0f0")
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
                logo_placeholder = Label(main_content, text="UNISON", font=("Arial", 24, "bold"), bg="#f0f0f0", fg="#2c3e50")
                logo_placeholder.grid(row=0, column=0, pady=(10, 8), sticky="n")
        except Exception as e:
            print(f"Error cargando logo: {e}")
            logo_placeholder = Label(main_content, text="UNISON", font=("Arial", 24, "bold"), bg="#f0f0f0", fg="#2c3e50")
            logo_placeholder.grid(row=0, column=0, pady=(10, 8), sticky="n")
        
        # Título Universidad (tamaño responsivo)
        titulo = Label(main_content, text="Universidad de Sonora", 
                      font=("Arial", 20, "bold"), bg="#f0f0f0", fg="#2c3e50")
        titulo.grid(row=1, column=0, pady=(0, 5), sticky="ew")
        
        # Subtítulo del sistema
        subtitulo = Label(main_content, text="Sistema de Inventario - Base de Datos 1", 
                         font=("Arial", 12, "italic"), bg="#f0f0f0", fg="#34495e")
        subtitulo.grid(row=2, column=0, pady=(0, 15), sticky="ew")
        
        # Separador visual
        separator = Frame(main_content, height=2, bg="#bdc3c7")
        separator.grid(row=3, column=0, sticky="ew", padx=30, pady=10)
        
        # Nombres de estudiantes
        nombres = Label(main_content, text="Manuel Munguia Rubio", 
                       font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#34495e")
        nombres.grid(row=4, column=0, pady=(10, 5), sticky="ew")
        
        # Información adicional
        info = Label(main_content, text="Carrera: Ingeniería en Sistemas de Información", 
                    font=("Arial", 11), bg="#f0f0f0", fg="#7f8c8d")
        info.grid(row=5, column=0, pady=(0, 25), sticky="ew")
        
        # Container para botones con diseño centrado y responsivo
        buttons_container = Frame(main_content, bg="#f0f0f0")
        buttons_container.grid(row=6, column=0, sticky="ew", pady=20)
        buttons_container.grid_columnconfigure(0, weight=1)
        
        # Frame interno para centrar los botones
        buttons_frame = Frame(buttons_container, bg="#f0f0f0")
        buttons_frame.grid(row=0, column=0)
        
        # Botones de navegación con mejor espaciado
        self.btn_productos = Button(buttons_frame, text="Productos", 
                                   font=("Arial", 13, "bold"), bg="#3498db", fg="white",
                                   width=14, height=3, relief="raised", cursor="hand2",
                                   borderwidth=2,
                                   command=lambda: self.show_frame("productos"))
        self.btn_productos.grid(row=0, column=0, padx=20, pady=10)
        
        self.btn_almacenes = Button(buttons_frame, text="Almacenes", 
                                   font=("Arial", 13, "bold"), bg="#e74c3c", fg="white",
                                   width=14, height=3, relief="raised", cursor="hand2",
                                   borderwidth=2,
                                   command=lambda: self.show_frame("almacenes"))
        self.btn_almacenes.grid(row=0, column=1, padx=20, pady=10)
        
        # Efectos hover
        def on_enter_productos(e):
            self.btn_productos.config(bg="#2980b9")
        def on_leave_productos(e):
            self.btn_productos.config(bg="#3498db")
        def on_enter_almacenes(e):
            self.btn_almacenes.config(bg="#c0392b")
        def on_leave_almacenes(e):
            self.btn_almacenes.config(bg="#e74c3c")
            
        self.btn_productos.bind("<Enter>", on_enter_productos)
        self.btn_productos.bind("<Leave>", on_leave_productos)
        self.btn_almacenes.bind("<Enter>", on_enter_almacenes)
        self.btn_almacenes.bind("<Leave>", on_leave_almacenes)
        
        # Espacio adicional al final para asegurar que todo sea visible
        spacer = Frame(main_content, bg="#f0f0f0", height=50)
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
        frame = Frame(self.container, bg="#f0f0f0")
        frame.grid(row=0, column=0, sticky="nsew")
        
        # Configurar grid responsivo
        frame.grid_rowconfigure(2, weight=1)  # El treeview se expande
        frame.grid_columnconfigure(0, weight=1)
        
        # Header con título simplificado
        header_frame = Frame(frame, bg="#34495e", height=50)
        header_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=(10, 0))
        header_frame.grid_propagate(False)
        header_frame.grid_columnconfigure(1, weight=1)
        
        # Título sin icono
        titulo = Label(header_frame, text="Gestión de Productos", 
                      font=("Arial", 18, "bold"), bg="#34495e", fg="white")
        titulo.grid(row=0, column=0, sticky="w", padx=20, pady=12)
        
        # Botón de volver en el header
        self.btn_volver_productos = Button(header_frame, text="Volver al Inicio", 
                                          font=("Arial", 11, "bold"), bg="#95a5a6", fg="white",
                                          relief="raised", cursor="hand2", borderwidth=1,
                                          command=lambda: self.show_frame("inicio"))
        self.btn_volver_productos.grid(row=0, column=1, sticky="e", padx=20, pady=10)
        
        # Frame para formulario con mejor organización
        form_frame = Frame(frame, bg="white", relief="raised", bd=1)
        form_frame.grid(row=1, column=0, sticky="ew", padx=10, pady=10)
        form_frame.grid_columnconfigure([1, 3, 5, 7, 9, 11], weight=1)
        
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
            entry = Entry(form_frame, width=15, font=("Arial", 11), relief="solid", bd=1)
            entry.grid(row=1, column=i*2+1, padx=(0, 15), pady=10, sticky="ew")
            self.producto_entries[campo.lower().replace("ó", "o").replace("é", "e")] = entry
        
        # Segunda fila: Cantidad, Departamento, Almacén
        for i, campo in enumerate(campos[3:], 3):
            Label(form_frame, text=campo + ":", font=("Arial", 11, "bold"), 
                 bg="white", fg="#34495e").grid(row=2, column=(i-3)*2, padx=(15, 5), pady=10, sticky="e")
            entry = Entry(form_frame, width=15, font=("Arial", 11), relief="solid", bd=1)
            entry.grid(row=2, column=(i-3)*2+1, padx=(0, 15), pady=10, sticky="ew")
            self.producto_entries[campo.lower().replace("ó", "o").replace("é", "e")] = entry
        
        # Nota informativa para el campo Almacén
        nota_almacen = Label(form_frame, text="Nota: Almacén debe ser el ID numérico (ej: 1, 2, 3...)", 
                           font=("Arial", 9, "italic"), bg="white", fg="#7f8c8d")
        nota_almacen.grid(row=3, column=6, columnspan=6, padx=15, pady=(0, 10), sticky="w")
        
        # Botones de acción en el formulario simplificados
        btn_form_frame = Frame(form_frame, bg="white")
        btn_form_frame.grid(row=4, column=0, columnspan=12, pady=15)
        
        self.btn_agregar_producto = Button(btn_form_frame, text="Agregar Producto", 
                                          font=("Arial", 12, "bold"), bg="#27ae60", fg="white",
                                          width=16, relief="raised", cursor="hand2", 
                                          borderwidth=2, pady=5)
        self.btn_agregar_producto.pack(side="left", padx=10)
        
        self.btn_eliminar_producto = Button(btn_form_frame, text="Eliminar Producto", 
                                           font=("Arial", 12, "bold"), bg="#e74c3c", fg="white",
                                           width=16, relief="raised", cursor="hand2", 
                                           borderwidth=2, pady=5)
        self.btn_eliminar_producto.pack(side="left", padx=10)
        
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
        
        columns = ("id", "nombre", "precio", "cantidad", "departamento", "almacen")
        self.productos_tree = ttk.Treeview(tree_container, columns=columns, show="headings")
        
        # Configurar encabezados y anchos responsivos
        headings = ["ID", "Nombre", "Precio", "Cantidad", "Departamento", "Almacén"]
        widths = [80, 200, 100, 100, 150, 150]
        
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
        frame = Frame(self.container, bg="#f0f0f0")
        frame.grid(row=0, column=0, sticky="nsew")
        
        # Configurar grid responsivo
        frame.grid_rowconfigure(2, weight=1)  # El treeview se expande
        frame.grid_columnconfigure(0, weight=1)
        
        # Header con título simplificado
        header_frame = Frame(frame, bg="#e74c3c", height=50)
        header_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=(10, 0))
        header_frame.grid_propagate(False)
        header_frame.grid_columnconfigure(1, weight=1)
        
        # Título sin icono
        titulo = Label(header_frame, text="Gestión de Almacenes", 
                      font=("Arial", 18, "bold"), bg="#e74c3c", fg="white")
        titulo.grid(row=0, column=0, sticky="w", padx=20, pady=12)
        
        # Botón de volver en el header
        self.btn_volver_almacenes = Button(header_frame, text="Volver al Inicio", 
                                          font=("Arial", 11, "bold"), bg="#95a5a6", fg="white",
                                          relief="raised", cursor="hand2", borderwidth=1,
                                          command=lambda: self.show_frame("inicio"))
        self.btn_volver_almacenes.grid(row=0, column=1, sticky="e", padx=20, pady=10)
        
        # Frame para formulario con mejor organización
        form_frame = Frame(frame, bg="white", relief="raised", bd=1)
        form_frame.grid(row=1, column=0, sticky="ew", padx=10, pady=10)
        form_frame.grid_columnconfigure([1, 3], weight=1)
        
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
        id_entry = Entry(campos_frame, width=20, font=("Arial", 12), relief="solid", bd=1)
        id_entry.grid(row=0, column=1, padx=(0, 30), pady=15, sticky="ew")
        self.almacen_entries["id"] = id_entry
        
        Label(campos_frame, text="Nombre:", font=("Arial", 12, "bold"), 
             bg="white", fg="#34495e").grid(row=0, column=2, padx=(0, 10), pady=15, sticky="e")
        nombre_entry = Entry(campos_frame, width=30, font=("Arial", 12), relief="solid", bd=1)
        nombre_entry.grid(row=0, column=3, padx=0, pady=15, sticky="ew")
        self.almacen_entries["nombre"] = nombre_entry
        
        # Botones de acción en el formulario simplificados
        btn_form_frame = Frame(form_frame, bg="white")
        btn_form_frame.grid(row=2, column=0, columnspan=4, pady=15)
        
        self.btn_agregar_almacen = Button(btn_form_frame, text="Agregar Almacén", 
                                         font=("Arial", 12, "bold"), bg="#27ae60", fg="white",
                                         width=16, relief="raised", cursor="hand2", 
                                         borderwidth=2, pady=5)
        self.btn_agregar_almacen.pack(side="left", padx=10)
        
        self.btn_eliminar_almacen = Button(btn_form_frame, text="Eliminar Almacén", 
                                          font=("Arial", 12, "bold"), bg="#e74c3c", fg="white",
                                          width=16, relief="raised", cursor="hand2", 
                                          borderwidth=2, pady=5)
        self.btn_eliminar_almacen.pack(side="left", padx=10)
        
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
        columns = ("id", "nombre")
        self.almacenes_tree = ttk.Treeview(tree_container, columns=columns, show="headings")
        
        # Configurar encabezados con mejor distribución
        self.almacenes_tree.heading("id", text="ID")
        self.almacenes_tree.heading("nombre", text="Nombre del Almacén")
        self.almacenes_tree.column("id", width=100, anchor="center")
        self.almacenes_tree.column("nombre", width=400, anchor="center")
        
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