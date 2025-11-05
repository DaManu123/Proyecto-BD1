import sqlite3
import os

class DatabaseModel:
    def __init__(self):
        """Inicializa la conexión a la base de datos SQLite"""
        # Ruta relativa al archivo de base de datos
        db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'database', 'InventarioBD_2.db')
        self.db_path = db_path
        self.connection = None
        self.connect()
    
    def connect(self):
        """Establece la conexión con la base de datos"""
        try:
            self.connection = sqlite3.connect(self.db_path)
            self.connection.row_factory = sqlite3.Row  # Para acceder a las columnas por nombre
            print(f"Conexión exitosa a la base de datos: {self.db_path}")
        except sqlite3.Error as e:
            print(f"Error al conectar con la base de datos: {e}")
    
    def disconnect(self):
        """Cierra la conexión con la base de datos"""
        if self.connection:
            self.connection.close()
            print("Conexión cerrada")
    
    def get_all_productos(self):
        """Obtiene todos los registros de la tabla productos"""
        if not self.connection:
            print("No hay conexión a la base de datos")
            return []
        
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                SELECT id, nombre, precio, cantidad, departamento, almacen 
                FROM productos 
                ORDER BY id
            """)
            productos = cursor.fetchall()
            # Convertir Row objects a tuplas para mejor manejo
            return [tuple(producto) for producto in productos]
        except sqlite3.Error as e:
            print(f"Error al obtener productos: {e}")
            return []
    
    def get_all_almacenes(self):
        """Obtiene todos los registros de la tabla almacenes"""
        if not self.connection:
            print("No hay conexión a la base de datos")
            return []
        
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                SELECT id, nombre 
                FROM almacenes 
                ORDER BY id
            """)
            almacenes = cursor.fetchall()
            # Convertir Row objects a tuplas para mejor manejo
            return [tuple(almacen) for almacen in almacenes]
        except sqlite3.Error as e:
            print(f"Error al obtener almacenes: {e}")
            return []
    
    def create_tables_if_not_exist(self):
        """Crea las tablas si no existen (para pruebas)"""
        if not self.connection:
            print("No hay conexión a la base de datos")
            return
        
        try:
            cursor = self.connection.cursor()
            
            # Crear tabla almacenes
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS almacenes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL
                )
            """)
            
            # Crear tabla productos
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS productos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    precio REAL NOT NULL,
                    cantidad INTEGER NOT NULL,
                    departamento TEXT NOT NULL,
                    almacen TEXT NOT NULL
                )
            """)
            
            self.connection.commit()
            print("Tablas creadas o verificadas exitosamente")
            
        except sqlite3.Error as e:
            print(f"Error al crear tablas: {e}")
    
    def agregar_producto(self, nombre, precio, cantidad, departamento, almacen_id):
        """Agrega un nuevo producto a la base de datos"""
        if not self.connection:
            print("No hay conexión a la base de datos")
            return False
        
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO productos (nombre, precio, cantidad, departamento, almacen)
                VALUES (?, ?, ?, ?, ?)
            """, (nombre, precio, cantidad, departamento, almacen_id))
            self.connection.commit()
            print(f"Producto '{nombre}' agregado exitosamente")
            return True
        except sqlite3.Error as e:
            print(f"Error al agregar producto: {e}")
            return False
    
    def eliminar_producto(self, producto_id):
        """Elimina un producto por su ID"""
        if not self.connection:
            print("No hay conexión a la base de datos")
            return False
        
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM productos WHERE id = ?", (producto_id,))
            
            if cursor.rowcount > 0:
                self.connection.commit()
                print(f"Producto con ID {producto_id} eliminado exitosamente")
                return True
            else:
                print(f"No se encontró producto con ID {producto_id}")
                return False
        except sqlite3.Error as e:
            print(f"Error al eliminar producto: {e}")
            return False
    
    def agregar_almacen(self, nombre):
        """Agrega un nuevo almacén a la base de datos"""
        if not self.connection:
            print("No hay conexión a la base de datos")
            return False
        
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO almacenes (nombre) VALUES (?)", (nombre,))
            self.connection.commit()
            print(f"Almacén '{nombre}' agregado exitosamente")
            return True
        except sqlite3.Error as e:
            print(f"Error al agregar almacén: {e}")
            return False
    
    def eliminar_almacen(self, almacen_id):
        """Elimina un almacén por su ID"""
        if not self.connection:
            print("No hay conexión a la base de datos")
            return False
        
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM almacenes WHERE id = ?", (almacen_id,))
            
            if cursor.rowcount > 0:
                self.connection.commit()
                print(f"Almacén con ID {almacen_id} eliminado exitosamente")
                return True
            else:
                print(f"No se encontró almacén con ID {almacen_id}")
                return False
        except sqlite3.Error as e:
            print(f"Error al eliminar almacén: {e}")
            return False
    
    def get_almacenes_nombres(self):
        """Obtiene solo los nombres de almacenes para validación"""
        if not self.connection:
            return []
        
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT nombre FROM almacenes ORDER BY nombre")
            return [row[0] for row in cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"Error al obtener nombres de almacenes: {e}")
            return []
    
    def get_almacenes_ids(self):
        """Obtiene los IDs de almacenes válidos para validación"""
        if not self.connection:
            return []
        
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT id FROM almacenes ORDER BY id")
            return [row[0] for row in cursor.fetchall()]
        except sqlite3.Error as e:
            print(f"Error al obtener IDs de almacenes: {e}")
            return []
    
    def almacen_existe(self, almacen_id):
        """Verifica si un ID de almacén existe"""
        if not self.connection:
            return False
        
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT COUNT(*) FROM almacenes WHERE id = ?", (almacen_id,))
            return cursor.fetchone()[0] > 0
        except sqlite3.Error as e:
            print(f"Error al verificar almacén: {e}")
            return False