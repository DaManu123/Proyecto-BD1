"""
Controlador integrado simplificado con login y aplicación principal
"""
from models.database import DatabaseModel
from views.login_view_split import LoginViewUnisonSplit
from views.main_view import MainView
from tkinter import messagebox
import tkinter as tk
import re
import sys
import os

# Importar el sistema de temas UNISON - Agregar ruta absoluta
current_dir = os.path.dirname(os.path.abspath(__file__))
utils_path = os.path.join(current_dir, '..', 'utils')
if utils_path not in sys.path:
    sys.path.insert(0, utils_path)
from theme_unison import COLOR_FONDO_BLANCO

class IntegratedController:
    def __init__(self, root):
        """Inicializa el controlador integrado con login y aplicación principal"""
        self.root = root
        self.root.title("Sistema de Inventario - Universidad de Sonora")
        self.root.geometry("1000x700")
        self.root.configure(bg=COLOR_FONDO_BLANCO)
        self.root.resizable(True, True)
        self.root.minsize(800, 600)
        
        # Crear un frame contenedor principal que siempre permanecerá
        self.main_container = tk.Frame(self.root, bg=COLOR_FONDO_BLANCO)
        self.main_container.pack(fill=tk.BOTH, expand=True)
        
        # Inicializar el modelo (base de datos)
        self.model = DatabaseModel()
        
        # Crear las tablas si no existen
        self.model.create_tables_if_not_exist()
        
        # Variable para almacenar información del usuario logueado
        self.current_user = None
        self.current_user_role = None  # Rol del usuario actual
        
        # Vistas
        self.login_view = None
        self.main_view = None
        
        # Estado actual de la aplicación
        self.current_state = "login"  # "login" o "main"
        
        # Mostrar la vista de login inicialmente
        self.show_login()
        
        # Vincular eventos de cierre de ventana
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def show_login(self):
        """Muestra la vista de login"""
        # Limpiar solo el contenedor, no toda la ventana
        for widget in self.main_container.winfo_children():
            widget.destroy()
        
        # Crear vista de login dentro del contenedor
        self.login_view = LoginViewUnisonSplit(self.main_container, self.handle_login)
        self.current_state = "login"
        self.root.title("Sistema de Inventario - Login - UNISON")
    
    def handle_login(self, username, password):
        """Maneja el proceso de login con validación de base de datos"""
        # Validar credenciales contra la base de datos (ahora retorna tupla)
        resultado, rol = self.model.validar_usuario(username, password)
        
        if resultado:
            self.current_user = username
            self.current_user_role = rol
            messagebox.showinfo("Bienvenido", f"¡Bienvenido al sistema, {username}!\nRol: {rol}")
            self.show_main_application()
        else:
            messagebox.showerror("Error de Autenticación", 
                               "Usuario o contraseña incorrectos.\n\n"
                               "Por favor verifique sus credenciales e intente nuevamente.")
            # Limpiar campos después de error
            if hasattr(self, 'login_view') and self.login_view:
                self.login_view.clear_fields()
    
    def show_main_application(self):
        """Muestra la vista principal y oculta la vista de login"""
        # Limpiar solo el contenedor, no toda la ventana
        for widget in self.main_container.winfo_children():
            widget.destroy()
        
        # Crear y mostrar la vista principal dentro del contenedor
        self.main_view = MainView(self.main_container)
        self.setup_main_view_commands()
        
        self.current_state = "main"
        self.root.title("Sistema de Inventario - Universidad de Sonora")
        
        # Mostrar el frame de inicio por defecto
        self.main_view.show_frame("inicio")
    
    def tiene_permiso_productos(self):
        """Verifica si el usuario tiene permiso para modificar productos"""
        return self.current_user_role in ['ADMIN', 'PRODUCTOS']
    
    def tiene_permiso_almacenes(self):
        """Verifica si el usuario tiene permiso para modificar almacenes"""
        return self.current_user_role in ['ADMIN', 'ALMACEN']
    
    def aplicar_permisos_interfaz(self):
        """Aplica los permisos de interfaz según el rol del usuario"""
        if not self.main_view:
            return
        
        # ===== PERMISOS PARA PRODUCTOS =====
        tiene_permiso_prod = self.tiene_permiso_productos()
        
        # Ocultar/mostrar formulario completo de productos
        if hasattr(self.main_view, 'producto_form_frame'):
            if tiene_permiso_prod:
                self.main_view.producto_form_frame.grid()
            else:
                self.main_view.producto_form_frame.grid_remove()
        
        # Ocultar/mostrar botones de productos (usan pack, no grid)
        if hasattr(self.main_view, 'btn_agregar_producto'):
            if tiene_permiso_prod:
                self.main_view.btn_agregar_producto.pack(side="left", padx=12)
            else:
                self.main_view.btn_agregar_producto.pack_forget()
        
        if hasattr(self.main_view, 'btn_eliminar_producto'):
            if tiene_permiso_prod:
                self.main_view.btn_eliminar_producto.pack(side="left", padx=12)
            else:
                self.main_view.btn_eliminar_producto.pack_forget()
        
        # ===== PERMISOS PARA ALMACENES =====
        tiene_permiso_alm = self.tiene_permiso_almacenes()
        
        # Ocultar/mostrar formulario completo de almacenes
        if hasattr(self.main_view, 'almacen_form_frame'):
            if tiene_permiso_alm:
                self.main_view.almacen_form_frame.grid()
            else:
                self.main_view.almacen_form_frame.grid_remove()
        
        # Ocultar/mostrar botones de almacenes (usan pack, no grid)
        if hasattr(self.main_view, 'btn_agregar_almacen'):
            if tiene_permiso_alm:
                self.main_view.btn_agregar_almacen.pack(side="left", padx=12)
            else:
                self.main_view.btn_agregar_almacen.pack_forget()
        
        if hasattr(self.main_view, 'btn_eliminar_almacen'):
            if tiene_permiso_alm:
                self.main_view.btn_eliminar_almacen.pack(side="left", padx=12)
            else:
                self.main_view.btn_eliminar_almacen.pack_forget()
    
    def setup_main_view_commands(self):
        """Configura los comandos de todos los botones de la vista principal"""
        if not self.main_view:
            return
            
        # Buscar y configurar botones en las vistas
        try:
            # Buscar botones de productos
            if hasattr(self.main_view, 'btn_agregar_producto'):
                self.main_view.btn_agregar_producto.config(command=self.agregar_producto)
            if hasattr(self.main_view, 'btn_eliminar_producto'):
                self.main_view.btn_eliminar_producto.config(command=self.eliminar_producto)
            
            # Buscar botones de almacenes
            if hasattr(self.main_view, 'btn_agregar_almacen'):
                self.main_view.btn_agregar_almacen.config(command=self.agregar_almacen)
            if hasattr(self.main_view, 'btn_eliminar_almacen'):
                self.main_view.btn_eliminar_almacen.config(command=self.eliminar_almacen)
            
            # Buscar botones de navegación (en el frame de inicio)
            if hasattr(self.main_view, 'btn_productos'):
                self.main_view.btn_productos.config(command=self.show_productos_frame)
            if hasattr(self.main_view, 'btn_almacenes'):
                self.main_view.btn_almacenes.config(command=self.show_almacenes_frame)
            
            # Configurar el botón de cerrar sesión
            if hasattr(self.main_view, 'btn_cerrar_sesion'):
                self.main_view.btn_cerrar_sesion.config(command=self.logout)
            
            # Aplicar permisos de interfaz según rol
            self.aplicar_permisos_interfaz()
        except Exception as e:
            print(f"Error configurando comandos: {e}")
    
    def logout(self):
        """Cierra sesión y vuelve a la pantalla de login"""
        if messagebox.askyesno("Cerrar Sesión", 
                              "¿Está seguro de que desea cerrar sesión?"):
            self.current_user = None
            self.current_user_role = None
            self.show_login()
    
    def show_productos_frame(self):
        """Muestra el frame de productos y carga los datos"""
        if self.main_view:
            self.main_view.show_frame("productos")
            self.load_productos_data()
            # Reaplicar permisos al cambiar de frame
            self.aplicar_permisos_interfaz()
            # Auto-completar ID con el siguiente disponible
            self.autocompletar_id_producto()
    
    def show_almacenes_frame(self):
        """Muestra el frame de almacenes y carga los datos"""
        if self.main_view:
            self.main_view.show_frame("almacenes")
            self.load_almacenes_data()
            # Reaplicar permisos al cambiar de frame
            self.aplicar_permisos_interfaz()
    
    def load_productos_data(self):
        """Carga los datos de productos desde la base de datos"""
        try:
            productos = self.model.get_all_productos()
            if self.main_view:
                self.main_view.update_productos_tree(productos)
                # Actualizar información de almacenes disponibles
                almacenes_info = self.get_almacenes_info_breve()
                if hasattr(self.main_view, 'info_almacenes_label'):
                    self.main_view.info_almacenes_label.config(
                        text=f"💡 Almacenes disponibles: {almacenes_info}")
            print(f"Cargados {len(productos)} productos")
        except Exception as e:
            print(f"Error al cargar productos: {e}")
    
    def autocompletar_id_producto(self):
        """Auto-completa el campo ID con el siguiente ID disponible"""
        try:
            if not self.main_view or not hasattr(self.main_view, 'producto_entries'):
                return
            
            # Obtener el siguiente ID disponible
            productos = self.model.get_all_productos()
            if productos:
                # Obtener el ID más alto y sumar 1
                max_id = max([int(p[0]) for p in productos])
                siguiente_id = max_id + 1
            else:
                siguiente_id = 1
            
            # Auto-completar el campo ID
            id_entry = self.main_view.producto_entries.get('id')
            if id_entry:
                id_entry.delete(0, 'end')
                id_entry.insert(0, str(siguiente_id))
        except Exception as e:
            print(f"Error al autocompletar ID: {e}")
    
    def load_almacenes_data(self):
        """Carga los datos de almacenes desde la base de datos"""
        try:
            almacenes = self.model.get_all_almacenes()
            if self.main_view:
                self.main_view.update_almacenes_tree(almacenes)
            print(f"Cargados {len(almacenes)} almacenes")
        except Exception as e:
            print(f"Error al cargar almacenes: {e}")
    
    def agregar_producto(self):
        """Función para agregar producto con validaciones"""
        # Verificar permisos
        if not self.tiene_permiso_productos():
            messagebox.showerror("Acceso Denegado", 
                               f"Su rol ({self.current_user_role}) no tiene permiso para agregar productos.\n\n"
                               "Solo los roles ADMIN y PRODUCTOS pueden realizar esta acción.")
            return
        
        try:
            if not self.main_view:
                return
                
            data = self.main_view.get_producto_data()
            
            # Convertir el almacén (nombre o ID) a ID numérico
            almacen_id = self.convertir_almacen_a_id(data['almacen'])
            if almacen_id is None:
                almacenes_info = self.get_almacenes_info()
                messagebox.showerror("Error de Validación", 
                    f"El almacén '{data['almacen']}' no es válido.\n\n"
                    f"Almacenes disponibles:\n{almacenes_info}")
                return
            
            # Actualizar data con el ID numérico para la validación
            data['almacen'] = str(almacen_id)
            
            if not self.validar_producto(data):
                return
            
            precio = float(data['precio'])
            cantidad = int(data['cantidad'])
            
            if not self.model.almacen_existe(almacen_id):
                almacenes_info = self.get_almacenes_info()
                messagebox.showerror("Error", 
                    f"El ID de almacén '{almacen_id}' no existe.\\n\\n"
                    f"IDs de almacenes disponibles:\\n{almacenes_info}")
                return
            
            # Verificar si es actualización o creación
            producto_id = data['id'].strip()
            if producto_id and self.model.producto_existe(int(producto_id)):
                # Actualizar producto existente
                if self.model.actualizar_producto(int(producto_id), data['nombre'], precio, cantidad, 
                                                 data['departamento'], almacen_id, self.current_user):
                    messagebox.showinfo("Éxito", f"Producto '{data['nombre']}' actualizado exitosamente")
                    self.main_view.limpiar_formulario_producto()
                    self.load_productos_data()
                    self.autocompletar_id_producto()
                else:
                    messagebox.showerror("Error", "No se pudo actualizar el producto")
            else:
                # Crear nuevo producto
                if self.model.agregar_producto(data['nombre'], precio, cantidad, 
                                             data['departamento'], almacen_id, self.current_user):
                    messagebox.showinfo("Éxito", f"Producto '{data['nombre']}' agregado exitosamente")
                    self.main_view.limpiar_formulario_producto()
                    self.load_productos_data()
                    self.autocompletar_id_producto()
                else:
                    messagebox.showerror("Error", "No se pudo agregar el producto")
                
        except ValueError:
            messagebox.showerror("Error de Validación", 
                               "Precio debe ser un número decimal, Cantidad debe ser un número entero")
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {str(e)}")
    
    def eliminar_producto(self):
        """Función para eliminar producto seleccionado"""
        # Verificar permisos
        if not self.tiene_permiso_productos():
            messagebox.showerror("Acceso Denegado", 
                               f"Su rol ({self.current_user_role}) no tiene permiso para eliminar productos.\n\n"
                               "Solo los roles ADMIN y PRODUCTOS pueden realizar esta acción.")
            return
        
        try:
            if not self.main_view:
                return
                
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
        # Verificar permisos
        if not self.tiene_permiso_almacenes():
            messagebox.showerror("Acceso Denegado", 
                               f"Su rol ({self.current_user_role}) no tiene permiso para agregar almacenes.\n\n"
                               "Solo los roles ADMIN y ALMACEN pueden realizar esta acción.")
            return
        
        try:
            if not self.main_view:
                return
                
            data = self.main_view.get_almacen_data()
            
            if not self.validar_almacen(data):
                return
            
            # Verificar si es actualización o creación
            almacen_id = data['id'].strip()
            if almacen_id and self.model.almacen_existe_por_id(int(almacen_id)):
                # Actualizar almacén existente
                if self.model.actualizar_almacen(int(almacen_id), data['nombre'], self.current_user):
                    messagebox.showinfo("Éxito", f"Almacén '{data['nombre']}' actualizado exitosamente")
                    self.main_view.limpiar_formulario_almacen()
                    self.load_almacenes_data()
                else:
                    messagebox.showerror("Error", "No se pudo actualizar el almacén")
            else:
                # Crear nuevo almacén
                if self.model.agregar_almacen(data['nombre'], self.current_user):
                    messagebox.showinfo("Éxito", f"Almacén '{data['nombre']}' agregado exitosamente")
                    self.main_view.limpiar_formulario_almacen()
                    self.load_almacenes_data()
                else:
                    messagebox.showerror("Error", "No se pudo agregar el almacén")
                
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {str(e)}")
    
    def eliminar_almacen(self):
        """Función para eliminar almacén seleccionado"""
        # Verificar permisos
        if not self.tiene_permiso_almacenes():
            messagebox.showerror("Acceso Denegado", 
                               f"Su rol ({self.current_user_role}) no tiene permiso para eliminar almacenes.\n\n"
                               "Solo los roles ADMIN y ALMACEN pueden realizar esta acción.")
            return
        
        try:
            if not self.main_view:
                return
                
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
        # Nota: El ID no es obligatorio ya que se auto-genera
        
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
            almacenes_info = self.get_almacenes_info()
            messagebox.showerror("Error de Validación", 
                f"El ID del almacén es obligatorio.\n\n"
                f"IDs de almacenes disponibles:\n{almacenes_info}")
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
            almacenes_info = self.get_almacenes_info()
            messagebox.showerror("Error de Validación", 
                f"El ID del almacén debe ser un número entero válido.\n\n"
                f"IDs de almacenes disponibles:\n{almacenes_info}")
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
        
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ0-9\s\-_]+$', data['nombre']):
            messagebox.showerror("Error de Validación", 
                                "El nombre solo puede contener letras, números, espacios, guiones y guiones bajos")
            return False
        
        return True
    
    def convertir_almacen_a_id(self, almacen_input):
        """Convierte el nombre o ID de almacén a ID numérico"""
        try:
            # Si ya es un número, devolverlo
            return int(almacen_input)
        except ValueError:
            # Si es un nombre, buscar el ID correspondiente
            try:
                almacenes = self.model.get_all_almacenes()
                for almacen in almacenes:
                    if almacen[1].lower() == almacen_input.lower():
                        return almacen[0]
                # Si no se encontró, devolver None
                return None
            except Exception as e:
                return None
    
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
    
    def get_almacenes_info_breve(self):
        """Obtiene información breve de los almacenes (para mostrar en UI)"""
        try:
            almacenes = self.model.get_all_almacenes()
            info_parts = []
            for almacen in almacenes:
                info_parts.append(f"{almacen[0]}={almacen[1]}")
            return " | ".join(info_parts)
        except Exception as e:
            return "Error al cargar almacenes"
    
    def on_closing(self):
        """Función que se ejecuta al cerrar la aplicación"""
        print("Cerrando aplicación...")
        if self.model:
            self.model.disconnect()
        self.root.destroy()