import tkinter as tk
from tkinter import messagebox
import sys
import os

# Añadir el directorio al path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from models.database import DatabaseModel

def test_login():
    """Función de prueba simple para el login"""
    print("=== PRUEBA SIMPLE DE LOGIN ===")
    
    # Crear ventana de prueba
    root = tk.Tk()
    root.title("Prueba de Login")
    root.geometry("400x300")
    root.configure(bg="#2c3e50")
    
    # Forzar que aparezca al frente
    root.lift()
    root.attributes('-topmost', True)
    root.focus_force()
    root.attributes('-topmost', False)
    
    # Centrar ventana
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (400 // 2)
    y = (root.winfo_screenheight() // 2) - (300 // 2)
    root.geometry(f"400x300+{x}+{y}")
    
    # Crear un label simple
    label = tk.Label(root, text="Ventana de Prueba\n¿Puedes verme?", 
                     bg="#2c3e50", fg="white", font=("Arial", 16))
    label.pack(expand=True)
    
    # Botón de cerrar
    btn = tk.Button(root, text="Cerrar", command=root.quit, 
                    bg="#e74c3c", fg="white", font=("Arial", 12))
    btn.pack(pady=20)
    
    print("Ventana de prueba creada y mostrada")
    print("Si no puedes ver la ventana, hay un problema con Tkinter")
    
    # Iniciar mainloop
    root.mainloop()
    print("Ventana de prueba cerrada")

if __name__ == "__main__":
    test_login()