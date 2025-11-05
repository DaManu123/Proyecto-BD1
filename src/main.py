from tkinter import Tk
from controllers.main_controller import MainController

def main():
    root = Tk()
    root.title("Databases Inventory App")
    app = MainController(root)
    root.mainloop()

if __name__ == "__main__":
    main()