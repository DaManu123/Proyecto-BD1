from models.database import DatabaseModel
from views.login_view_split import LoginViewUnisonSplit
from views.main_view import MainView
from tkinter import messagebox
import re
import sys
import os

# Importar el sistema de temas UNISON - Agregar ruta absoluta
current_dir = os.path.dirname(os.path.abspath(__file__))
utils_path = os.path.join(current_dir, '..', 'utils')
if utils_path not in sys.path:
    sys.path.insert(0, utils_path)
from theme_unison import *

class IntegratedController:
    def __init__(self, root):
        """Inicializa el controlador integrado con login y aplicación principal"""
        self.root = root
        self.root.title("Sistema de Inventario - Universidad de Sonora")
        self.root.geometry("1000x700")
        self.root.configure(bg=COLOR_FONDO_NEUTRAL)
        self.root.resizable(True, True)
        self.root.minsize(800, 600)
        
        # Aplicar estilo global UNISON
        aplicar_estilo_global_tkinter()
        
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
        # Crear el contenedor principal con tema UNISON
        self.main_container = crear_frame_unison(self.root, azul=False)
        self.main_container.grid(row=0, column=0, sticky="nsew")
        self.main_container.grid_rowconfigure(0, weight=1)
        self.main_container.grid_columnconfigure(0, weight=1)
        
        # Crear la vista de login con nuevo diseño split
        self.login_view = LoginViewUnisonSplit(self.main_container, self.handle_login)
        
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
        
        # Configurar el botón de cerrar sesión
        self.main_view.btn_cerrar_sesion.config(command=self.logout)
    
    def handle_login(self, username):
        """Maneja el proceso de login exitoso"""
        self.current_user = username
        # Login exitoso - cambiar a la vista principal
        self.show_main_application()
    
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
            self.main_view.pack_forget()
        
        self.current_state = "login"
        
        # Cambiar el título de la ventana
        self.root.title("Sistema de Inventario - Login - UNISON")
    
    def show_main_application(self):
        """Muestra la vista principal y oculta la vista de login"""
        # Destruir la vista de login
        self.login_view.destroy()
        
        # Crear y mostrar la vista principal
        self.main_view = MainView(self.main_container)
        self.setup_main_view_commands()
        
        self.current_state = "main"
        
        # Cambiar el título de la ventana
        self.root.title("Sistema de Inventario - Universidad de Sonora")
    
    def logout(self):
        """Cierra sesión y vuelve a la pantalla de login"""
        # Confirmar cierre de sesión
        if messagebox.askyesno("Cerrar Sesión", 
                              "¿Está seguro de que desea cerrar sesión?"):
            # Limpiar datos de usuario
            self.current_user = None
            
            # Destruir vista principal
            if self.main_view:
                self.main_view.destroy()
            
            # Recrear vista de login
            self.login_view = LoginViewUnisonSplit(self.main_container, self.handle_login)
            
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