from models.database import DatabaseModel
from views.login_view_integrated import LoginViewIntegrated
from views.main_view import MainView
from tkinter import messagebox
import re

class IntegratedController:
    def __init__(self, root):
        """Inicializa el controlador integrado con login y aplicación principal"""
        self.root = root
        self.root.title("Sistema de Inventario - Universidad de Sonora")
        self.root.geometry("900x650")
        self.root.configure(bg="#f0f0f0")
        self.root.resizable(True, True)
        self.root.minsize(750, 550)
        
        # Inicializar el modelo (base de datos)
        self.model = DatabaseModel()
        
        # Crear las tablas si no existen
        self.model.create_tables_if_not_exist()
        
        # Variable para almacenar información del usuario logueado
        self.current_user = None
        
        # Configurar el grid principal para que sea responsivo
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        # Contenedor principal que alojará tanto el login como la vista principal
        self.main_container = None
        
        # Vistas
        self.login_view = None
        self.main_view = None
        
        # Estado actual de la aplicación
        self.current_state = "login"  # "login" o "main"
        
        # Inicializar las vistas
        self.initialize_views()
        
        # Mostrar la vista de login inicialmente
        self.show_login()
        
        # Vincular eventos de cierre de ventana
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def initialize_views(self):
        """Inicializa todas las vistas pero las mantiene ocultas"""
        # Crear el contenedor principal
        from tkinter import Frame
        self.main_container = Frame(self.root, bg="#f0f0f0")
        self.main_container.grid(row=0, column=0, sticky="nsew")
        self.main_container.grid_rowconfigure(0, weight=1)
        self.main_container.grid_columnconfigure(0, weight=1)
        
        # Crear la vista de login integrada
        self.login_view = LoginViewIntegrated(self.main_container)
        self.login_view.set_login_callback(self.handle_login)
        self.login_view.bind_enter_key(self.root)
        
        # Crear la vista principal (inicialmente oculta)
        self.main_view = MainView(self.main_container)
        
        # Configurar los comandos de los botones de la vista principal
        self.setup_main_view_commands()
        
        # Ocultar la vista principal inicialmente
        self.main_view.container.grid_remove()
    
    def setup_main_view_commands(self):
        """Configura los comandos de todos los botones de la vista principal"""
        # Botones de agregar y eliminar
        self.main_view.btn_agregar_producto.config(command=self.agregar_producto)
        self.main_view.btn_eliminar_producto.config(command=self.eliminar_producto)
        self.main_view.btn_agregar_almacen.config(command=self.agregar_almacen)
        self.main_view.btn_eliminar_almacen.config(command=self.eliminar_almacen)
        
        # Override los botones de navegación para cargar datos
        self.main_view.btn_productos.config(command=self.show_productos_frame)
        self.main_view.btn_almacenes.config(command=self.show_almacenes_frame)
        
        # Agregar botón de cerrar sesión en la vista principal
        self.add_logout_button()
    
    def add_logout_button(self):
        """Agrega un botón de cerrar sesión a la vista principal"""
        from tkinter import Button
        
        # Obtener el frame de inicio de la vista principal
        inicio_frame = self.main_view.frames["inicio"]
        
        # Buscar el frame de botones en la vista de inicio
        for widget in inicio_frame.winfo_children():
            if hasattr(widget, 'winfo_children'):
                for child in widget.winfo_children():
                    if hasattr(child, 'winfo_children'):
                        for grandchild in child.winfo_children():
                            if hasattr(grandchild, 'winfo_children'):
                                for ggchild in grandchild.winfo_children():
                                    if str(ggchild.__class__.__name__) == "Frame":
                                        # Este podría ser el frame de botones
                                        try:
                                            # Intentar agregar el botón de logout
                                            logout_btn = Button(ggchild, text="Cerrar Sesión", 
                                                              font=("Arial", 11, "bold"), 
                                                              bg="#e67e22", fg="white",
                                                              width=14, height=2, 
                                                              relief="raised", cursor="hand2",
                                                              borderwidth=2,
                                                              command=self.logout)
                                            logout_btn.grid(row=1, column=0, columnspan=2, padx=20, pady=10)
                                            
                                            # Efectos hover
                                            def on_enter_logout(e):
                                                logout_btn.config(bg="#d35400")
                                            def on_leave_logout(e):
                                                logout_btn.config(bg="#e67e22")
                                            
                                            logout_btn.bind("<Enter>", on_enter_logout)
                                            logout_btn.bind("<Leave>", on_leave_logout)
                                            break
                                        except:
                                            continue
    
    def handle_login(self, credentials):
        """Maneja el proceso de login"""
        username = credentials['usuario']
        password = credentials['password']
        
        # Por ahora, validación simple (puedes integrar con base de datos después)
        if self.validate_login(username, password):
            # Login exitoso - cambiar a la vista principal
            self.show_main_application()
        else:
            # Login fallido - mostrar mensaje de error
            messagebox.showerror("Error de Autenticación", 
                               "Usuario o contraseña incorrectos")
            self.login_view.clear_form()
    
    def validate_login(self, username, password):
        """
        Valida las credenciales de login
        Por ahora es una validación simple, pero puede integrarse con la base de datos
        """
        # Validación simple para demostración
        # En una implementación real, verificarías contra la base de datos
        return len(username) > 0 and len(password) > 0
    
    def show_login(self):
        """Muestra la vista de login y oculta la vista principal"""
        if self.main_view:
            self.main_view.container.grid_remove()
        
        self.login_view.show()
        self.current_state = "login"
        
        # Cambiar el título de la ventana
        self.root.title("Sistema de Inventario - Login")
        
        # Focus en el campo de usuario
        self.login_view.user_entry.focus()
    
    def show_main_application(self):
        """Muestra la vista principal y oculta la vista de login"""
        # Ocultar la vista de login
        self.login_view.hide()
        
        # Mostrar la vista principal
        self.main_view.container.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        
        self.current_state = "main"
        
        # Cambiar el título de la ventana
        self.root.title("Sistema de Inventario - Universidad de Sonora")
        
        # Mostrar el frame de inicio por defecto
        self.main_view.show_frame("inicio")
    
    def logout(self):
        """Cierra sesión y vuelve a la pantalla de login"""
        # Confirmar cierre de sesión
        if messagebox.askyesno("Cerrar Sesión", 
                              "¿Está seguro de que desea cerrar sesión?"):
            # Limpiar datos de usuario
            self.current_user = None
            
            # Limpiar formulario de login
            self.login_view.clear_form()
            
            # Volver a la vista de login
            self.show_login()
    
    # Métodos heredados del MainController original para mantener funcionalidad
    
    def show_frame(self, frame_name):
        """Muestra el frame especificado y carga los datos si es necesario"""
        if self.current_state == "main":
            self.main_view.show_frame(frame_name)
            
            # Cargar datos según el frame mostrado
            if frame_name == "productos":
                self.load_productos_data()
            elif frame_name == "almacenes":
                self.load_almacenes_data()
    
    def show_productos_frame(self):
        """Muestra el frame de productos y carga los datos"""
        self.main_view.show_frame("productos")
        self.load_productos_data()
    
    def show_almacenes_frame(self):
        """Muestra el frame de almacenes y carga los datos"""
        self.main_view.show_frame("almacenes")
        self.load_almacenes_data()
    
    def load_productos_data(self):
        """Carga los datos de productos desde la base de datos"""
        try:
            productos = self.model.get_all_productos()
            self.main_view.update_productos_tree(productos)
            print(f"Cargados {len(productos)} productos")
        except Exception as e:
            print(f"Error al cargar productos: {e}")
    
    def load_almacenes_data(self):
        """Carga los datos de almacenes desde la base de datos"""
        try:
            almacenes = self.model.get_all_almacenes()
            self.main_view.update_almacenes_tree(almacenes)
            print(f"Cargados {len(almacenes)} almacenes")
        except Exception as e:
            print(f"Error al cargar almacenes: {e}")
    
    # Funciones CRUD completas (copiadas del MainController original)
    def agregar_producto(self):
        """Función para agregar producto con validaciones"""
        try:
            # Obtener datos del formulario
            data = self.main_view.get_producto_data()
            
            # Validar campos requeridos
            if not self.validar_producto(data):
                return
            
            # Convertir tipos de datos
            precio = float(data['precio'])
            cantidad = int(data['cantidad'])
            almacen_id = int(data['almacen'])
            
            # Validar que el almacén existe
            if not self.model.almacen_existe(almacen_id):
                almacenes_info = self.get_almacenes_info()
                messagebox.showerror("Error", 
                    f"El ID de almacén '{almacen_id}' no existe.\\n\\n"
                    f"IDs de almacenes disponibles:\\n{almacenes_info}")
                return
            
            # Agregar producto a la base de datos
            if self.model.agregar_producto(data['nombre'], precio, cantidad, 
                                         data['departamento'], almacen_id):
                messagebox.showinfo("Éxito", f"Producto '{data['nombre']}' agregado exitosamente")
                self.main_view.limpiar_formulario_producto()
                self.load_productos_data()
            else:
                messagebox.showerror("Error", "No se pudo agregar el producto")
                
        except ValueError as e:
            messagebox.showerror("Error de Validación", 
                               "Precio debe ser un número decimal, Cantidad debe ser un número entero, y Almacén debe ser un ID numérico válido")
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {str(e)}")
    
    def eliminar_producto(self):
        """Función para eliminar producto seleccionado"""
        try:
            data = self.main_view.get_producto_data()
            
            if not data['id']:
                messagebox.showwarning("Advertencia", 
                                     "Seleccione un producto de la tabla para eliminar")
                return
            
            producto_id = int(data['id'])
            
            respuesta = messagebox.askyesno("Confirmar Eliminación", 
                                          f"¿Está seguro de eliminar el producto '{data['nombre']}'?")
            
            if respuesta:
                if self.model.eliminar_producto(producto_id):
                    messagebox.showinfo("Éxito", "Producto eliminado exitosamente")
                    self.main_view.limpiar_formulario_producto()
                    self.load_productos_data()
                else:
                    messagebox.showerror("Error", "No se pudo eliminar el producto")
                    
        except ValueError:
            messagebox.showerror("Error", "ID de producto inválido")
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {str(e)}")
    
    def agregar_almacen(self):
        """Función para agregar almacén con validaciones"""
        try:
            data = self.main_view.get_almacen_data()
            
            if not self.validar_almacen(data):
                return
            
            if self.model.agregar_almacen(data['nombre']):
                messagebox.showinfo("Éxito", f"Almacén '{data['nombre']}' agregado exitosamente")
                self.main_view.limpiar_formulario_almacen()
                self.load_almacenes_data()
            else:
                messagebox.showerror("Error", "No se pudo agregar el almacén")
                
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {str(e)}")
    
    def eliminar_almacen(self):
        """Función para eliminar almacén seleccionado"""
        try:
            data = self.main_view.get_almacen_data()
            
            if not data['id']:
                messagebox.showwarning("Advertencia", 
                                     "Seleccione un almacén de la tabla para eliminar")
                return
            
            almacen_id = int(data['id'])
            
            respuesta = messagebox.askyesno("Confirmar Eliminación", 
                                          f"¿Está seguro de eliminar el almacén '{data['nombre']}'?")
            
            if respuesta:
                if self.model.eliminar_almacen(almacen_id):
                    messagebox.showinfo("Éxito", "Almacén eliminado exitosamente")
                    self.main_view.limpiar_formulario_almacen()
                    self.load_almacenes_data()
                else:
                    messagebox.showerror("Error", "No se pudo eliminar el almacén")
                    
        except ValueError:
            messagebox.showerror("Error", "ID de almacén inválido")
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {str(e)}")
    
    def validar_producto(self, data):
        """Valida los datos de un producto"""
        if not data['nombre']:
            messagebox.showerror("Error de Validación", "El nombre del producto es obligatorio")
            return False
        
        if not data['precio']:
            messagebox.showerror("Error de Validación", "El precio es obligatorio")
            return False
        
        if not data['cantidad']:
            messagebox.showerror("Error de Validación", "La cantidad es obligatoria")
            return False
        
        if not data['departamento']:
            messagebox.showerror("Error de Validación", "El departamento es obligatorio")
            return False
        
        if not data['almacen']:
            messagebox.showerror("Error de Validación", "El ID del almacén es obligatorio")
            return False
        
        try:
            precio = float(data['precio'])
            if precio < 0:
                messagebox.showerror("Error de Validación", "El precio no puede ser negativo")
                return False
        except ValueError:
            messagebox.showerror("Error de Validación", "El precio debe ser un número válido")
            return False
        
        try:
            cantidad = int(data['cantidad'])
            if cantidad < 0:
                messagebox.showerror("Error de Validación", "La cantidad no puede ser negativa")
                return False
        except ValueError:
            messagebox.showerror("Error de Validación", "La cantidad debe ser un número entero")
            return False
        
        try:
            almacen_id = int(data['almacen'])
            if almacen_id <= 0:
                messagebox.showerror("Error de Validación", "El ID del almacén debe ser un número positivo")
                return False
        except ValueError:
            messagebox.showerror("Error de Validación", "El ID del almacén debe ser un número entero válido")
            return False
        
        if len(data['nombre']) > 100:
            messagebox.showerror("Error de Validación", "El nombre no puede exceder 100 caracteres")
            return False
        
        if len(data['departamento']) > 50:
            messagebox.showerror("Error de Validación", "El departamento no puede exceder 50 caracteres")
            return False
        
        return True
    
    def validar_almacen(self, data):
        """Valida los datos de un almacén"""
        if not data['nombre']:
            messagebox.showerror("Error de Validación", "El nombre del almacén es obligatorio")
            return False
        
        if len(data['nombre']) > 50:
            messagebox.showerror("Error de Validación", "El nombre no puede exceder 50 caracteres")
            return False
        
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ0-9\\s\\-_]+$', data['nombre']):
            messagebox.showerror("Error de Validación", 
                                "El nombre solo puede contener letras, números, espacios, guiones y guiones bajos")
            return False
        
        return True
    
    def get_almacenes_info(self):
        """Obtiene información formateada de los almacenes disponibles"""
        try:
            almacenes = self.model.get_all_almacenes()
            info_lines = []
            for almacen in almacenes:
                info_lines.append(f"ID: {almacen[0]} - {almacen[1]}")
            return "\\n".join(info_lines)
        except Exception as e:
            return "Error al obtener información de almacenes"
    
    def on_closing(self):
        """Función que se ejecuta al cerrar la aplicación"""
        print("Cerrando aplicación...")
        # Cerrar conexión a la base de datos
        if self.model:
            self.model.disconnect()
        # Cerrar la ventana
        self.root.destroy()