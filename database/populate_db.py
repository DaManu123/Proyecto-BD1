import sqlite3
import os

def populate_database():
    """Crea y llena la base de datos con datos de prueba"""
    
    # Conectar a la base de datos
    db_path = os.path.join(os.path.dirname(__file__), 'InventarioBD_2.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        # Crear tabla almacenes
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS almacenes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL
            )
        ''')
        
        # Crear tabla productos
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                precio REAL NOT NULL,
                cantidad INTEGER NOT NULL,
                departamento TEXT NOT NULL,
                almacen TEXT NOT NULL
            )
        ''')
        
        # Limpiar datos existentes
        cursor.execute('DELETE FROM productos')
        cursor.execute('DELETE FROM almacenes')
        
        # Insertar datos de prueba en almacenes
        almacenes_data = [
            ('Almacén Central',),
            ('Almacén Norte',),
            ('Almacén Sur',),
            ('Almacén Este',),
            ('Almacén Oeste',)
        ]
        
        cursor.executemany('INSERT INTO almacenes (nombre) VALUES (?)', almacenes_data)
        
        # Insertar datos de prueba en productos
        productos_data = [
            ('Laptop Dell XPS 13', 25000.00, 10, 'Electrónicos', 'Almacén Central'),
            ('Mouse Logitech MX', 1200.00, 50, 'Electrónicos', 'Almacén Norte'),
            ('Teclado Mecánico', 2500.00, 25, 'Electrónicos', 'Almacén Central'),
            ('Monitor Samsung 24"', 8000.00, 15, 'Electrónicos', 'Almacén Sur'),
            ('Silla Ergonómica', 4500.00, 20, 'Mobiliario', 'Almacén Este'),
            ('Escritorio de Madera', 6000.00, 8, 'Mobiliario', 'Almacén Oeste'),
            ('Calculadora Casio', 450.00, 100, 'Oficina', 'Almacén Norte'),
            ('Cuaderno A4', 25.00, 500, 'Papelería', 'Almacén Central'),
            ('Pluma BIC', 15.00, 200, 'Papelería', 'Almacén Sur'),
            ('Impresora HP LaserJet', 12000.00, 5, 'Electrónicos', 'Almacén Central')
        ]
        
        cursor.executemany('''
            INSERT INTO productos (nombre, precio, cantidad, departamento, almacen) 
            VALUES (?, ?, ?, ?, ?)
        ''', productos_data)
        
        # Confirmar cambios
        conn.commit()
        print("Base de datos poblada exitosamente!")
        print(f"- {len(almacenes_data)} almacenes insertados")
        print(f"- {len(productos_data)} productos insertados")
        
    except sqlite3.Error as e:
        print(f"Error al poblar la base de datos: {e}")
        conn.rollback()
    
    finally:
        conn.close()

if __name__ == "__main__":
    populate_database()