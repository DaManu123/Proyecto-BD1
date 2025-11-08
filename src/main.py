from tkinter import Tk
from controllers.integrated_controller_simple import IntegratedController

def main():
    root = Tk()
    app = IntegratedController(root)
    root.mainloop()

if __name__ == "__main__":
    main()