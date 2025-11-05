from models.database import DatabaseModel
from views.main_view import MainView
from tkinter import messagebox
import re

class MainController:
    def __init__(self, root):
        """Inicializa el controlador principal"""
        self.root = root
        
        # Inicializar el modelo (base de datos)
        self.model = DatabaseModel()
        
        # Crear las tablas si no existen (para pruebas)
        self.model.create_tables_if_not_exist()
        
        # Inicializar la vista
        self.view = MainView(root)
        
        # Configurar los comandos de los botones
        self.setup_button_commands()
        
        # Vincular eventos de cierre de ventana
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def setup_button_commands(self):
        """Configura los comandos de todos los botones"""
        # Botones de agregar y eliminar (funciones vacías por ahora)
        self.view.btn_agregar_producto.config(command=self.agregar_producto)
        self.view.btn_eliminar_producto.config(command=self.eliminar_producto)
        self.view.btn_agregar_almacen.config(command=self.agregar_almacen)
        self.view.btn_eliminar_almacen.config(command=self.eliminar_almacen)
        
        # Override los botones de navegación para cargar datos
        self.view.btn_productos.config(command=self.show_productos_frame)
        self.view.btn_almacenes.config(command=self.show_almacenes_frame)
    
    def show_frame(self, frame_name):
        """Muestra el frame especificado y carga los datos si es necesario"""
        self.view.show_frame(frame_name)
        
        # Cargar datos según el frame mostrado
        if frame_name == "productos":
            self.load_productos_data()
        elif frame_name == "almacenes":
            self.load_almacenes_data()
    
    def show_productos_frame(self):
        """Muestra el frame de productos y carga los datos"""
        self.view.show_frame("productos")
        self.load_productos_data()
    
    def show_almacenes_frame(self):
        """Muestra el frame de almacenes y carga los datos"""
        self.view.show_frame("almacenes")
        self.load_almacenes_data()
    
    def load_productos_data(self):
        """Carga los datos de productos desde la base de datos"""
        try:
            productos = self.model.get_all_productos()
            self.view.update_productos_tree(productos)
            print(f"Cargados {len(productos)} productos")
        except Exception as e:
            print(f"Error al cargar productos: {e}")
    
    def load_almacenes_data(self):
        """Carga los datos de almacenes desde la base de datos"""
        try:
            almacenes = self.model.get_all_almacenes()
            self.view.update_almacenes_tree(almacenes)
            print(f"Cargados {len(almacenes)} almacenes")
        except Exception as e:
            print(f"Error al cargar almacenes: {e}")
    
    # Funciones CRUD completas con validaciones
    def agregar_producto(self):
        """Función para agregar producto con validaciones"""
        try:
            # Obtener datos del formulario
            data = self.view.get_producto_data()
            
            # Validar campos requeridos
            if not self.validar_producto(data):
                return
            
            # Convertir tipos de datos
            precio = float(data['precio'])
            cantidad = int(data['cantidad'])
            almacen_id = int(data['almacen'])  # Convertir a entero para ID
            
            # Validar que el almacén existe
            if not self.model.almacen_existe(almacen_id):
                # Obtener información de almacenes para mostrar al usuario
                almacenes_info = self.get_almacenes_info()
                messagebox.showerror("Error", 
                    f"El ID de almacén '{almacen_id}' no existe.\n\n"
                    f"IDs de almacenes disponibles:\n{almacenes_info}")
                return
            
            # Agregar producto a la base de datos
            if self.model.agregar_producto(data['nombre'], precio, cantidad, 
                                         data['departamento'], almacen_id):
                messagebox.showinfo("Éxito", f"Producto '{data['nombre']}' agregado exitosamente")
                self.view.limpiar_formulario_producto()
                self.load_productos_data()  # Recargar la tabla
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
            # Obtener ID del producto seleccionado
            data = self.view.get_producto_data()
            
            if not data['id']:
                messagebox.showwarning("Advertencia", 
                                     "Seleccione un producto de la tabla para eliminar")
                return
            
            producto_id = int(data['id'])
            
            # Confirmar eliminación
            respuesta = messagebox.askyesno("Confirmar Eliminación", 
                                          f"¿Está seguro de eliminar el producto '{data['nombre']}'?")
            
            if respuesta:
                if self.model.eliminar_producto(producto_id):
                    messagebox.showinfo("Éxito", "Producto eliminado exitosamente")
                    self.view.limpiar_formulario_producto()
                    self.load_productos_data()  # Recargar la tabla
                else:
                    messagebox.showerror("Error", "No se pudo eliminar el producto")
                    
        except ValueError:
            messagebox.showerror("Error", "ID de producto inválido")
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {str(e)}")
    
    def agregar_almacen(self):
        """Función para agregar almacén con validaciones"""
        try:
            # Obtener datos del formulario
            data = self.view.get_almacen_data()
            
            # Validar campos requeridos
            if not self.validar_almacen(data):
                return
            
            # Agregar almacén a la base de datos
            if self.model.agregar_almacen(data['nombre']):
                messagebox.showinfo("Éxito", f"Almacén '{data['nombre']}' agregado exitosamente")
                self.view.limpiar_formulario_almacen()
                self.load_almacenes_data()  # Recargar la tabla
            else:
                messagebox.showerror("Error", "No se pudo agregar el almacén")
                
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {str(e)}")
    
    def eliminar_almacen(self):
        """Función para eliminar almacén seleccionado"""
        try:
            # Obtener ID del almacén seleccionado
            data = self.view.get_almacen_data()
            
            if not data['id']:
                messagebox.showwarning("Advertencia", 
                                     "Seleccione un almacén de la tabla para eliminar")
                return
            
            almacen_id = int(data['id'])
            
            # Confirmar eliminación
            respuesta = messagebox.askyesno("Confirmar Eliminación", 
                                          f"¿Está seguro de eliminar el almacén '{data['nombre']}'?")
            
            if respuesta:
                if self.model.eliminar_almacen(almacen_id):
                    messagebox.showinfo("Éxito", "Almacén eliminado exitosamente")
                    self.view.limpiar_formulario_almacen()
                    self.load_almacenes_data()  # Recargar la tabla
                else:
                    messagebox.showerror("Error", "No se pudo eliminar el almacén")
                    
        except ValueError:
            messagebox.showerror("Error", "ID de almacén inválido")
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {str(e)}")
    
    def validar_producto(self, data):
        """Valida los datos de un producto"""
        # Validar campos obligatorios
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
        
        # Validar formato del precio (debe ser número)
        try:
            precio = float(data['precio'])
            if precio < 0:
                messagebox.showerror("Error de Validación", "El precio no puede ser negativo")
                return False
        except ValueError:
            messagebox.showerror("Error de Validación", "El precio debe ser un número válido")
            return False
        
        # Validar formato de la cantidad (debe ser entero)
        try:
            cantidad = int(data['cantidad'])
            if cantidad < 0:
                messagebox.showerror("Error de Validación", "La cantidad no puede ser negativa")
                return False
        except ValueError:
            messagebox.showerror("Error de Validación", "La cantidad debe ser un número entero")
            return False
        
        # Validar formato del ID de almacén (debe ser entero)
        try:
            almacen_id = int(data['almacen'])
            if almacen_id <= 0:
                messagebox.showerror("Error de Validación", "El ID del almacén debe ser un número positivo")
                return False
        except ValueError:
            messagebox.showerror("Error de Validación", "El ID del almacén debe ser un número entero válido")
            return False
        
        # Validar longitud de campos de texto
        if len(data['nombre']) > 100:
            messagebox.showerror("Error de Validación", "El nombre no puede exceder 100 caracteres")
            return False
        
        if len(data['departamento']) > 50:
            messagebox.showerror("Error de Validación", "El departamento no puede exceder 50 caracteres")
            return False
        
        return True
    
    def validar_almacen(self, data):
        """Valida los datos de un almacén"""
        # Validar campos obligatorios
        if not data['nombre']:
            messagebox.showerror("Error de Validación", "El nombre del almacén es obligatorio")
            return False
        
        # Validar longitud
        if len(data['nombre']) > 50:
            messagebox.showerror("Error de Validación", "El nombre no puede exceder 50 caracteres")
            return False
        
        # Validar caracteres permitidos (solo letras, números, espacios y algunos símbolos)
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ0-9\s\-_]+$', data['nombre']):
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
            return "\n".join(info_lines)
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