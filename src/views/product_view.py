from tkinter import Frame, Label, Entry, Button, Treeview, Scrollbar, END
from tkinter import messagebox
from models.product import Product
from controllers.product_controller import ProductController

class ProductView(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.controller = ProductController()
        self.create_widgets()
        self.load_products()

    def create_widgets(self):
        self.label_name = Label(self, text="Product Name:")
        self.label_name.grid(row=0, column=0)

        self.entry_name = Entry(self)
        self.entry_name.grid(row=0, column=1)

        self.label_price = Label(self, text="Price:")
        self.label_price.grid(row=1, column=0)

        self.entry_price = Entry(self)
        self.entry_price.grid(row=1, column=1)

        self.label_quantity = Label(self, text="Quantity:")
        self.label_quantity.grid(row=2, column=0)

        self.entry_quantity = Entry(self)
        self.entry_quantity.grid(row=2, column=1)

        self.label_department = Label(self, text="Department:")
        self.label_department.grid(row=3, column=0)

        self.entry_department = Entry(self)
        self.entry_department.grid(row=3, column=1)

        self.label_warehouse = Label(self, text="Warehouse ID:")
        self.label_warehouse.grid(row=4, column=0)

        self.entry_warehouse = Entry(self)
        self.entry_warehouse.grid(row=4, column=1)

        self.button_add = Button(self, text="Add Product", command=self.add_product)
        self.button_add.grid(row=5, column=0, columnspan=2)

        self.tree = Treeview(self, columns=("ID", "Name", "Price", "Quantity", "Department", "Warehouse"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Price", text="Price")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.heading("Department", text="Department")
        self.tree.heading("Warehouse", text="Warehouse")

        self.scrollbar = Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=self.scrollbar.set)

        self.tree.grid(row=6, column=0, columnspan=2)
        self.scrollbar.grid(row=6, column=2, sticky='ns')

    def load_products(self):
        for product in self.controller.get_all_products():
            self.tree.insert("", END, values=(product.id, product.name, product.price, product.quantity, product.department, product.warehouse))

    def add_product(self):
        name = self.entry_name.get()
        price = self.entry_price.get()
        quantity = self.entry_quantity.get()
        department = self.entry_department.get()
        warehouse = self.entry_warehouse.get()

        if not all([name, price, quantity, department, warehouse]):
            messagebox.showerror("Input Error", "All fields must be filled out.")
            return

        try:
            price = float(price)
            quantity = int(quantity)
            warehouse = int(warehouse)
        except ValueError:
            messagebox.showerror("Input Error", "Price must be a number and Quantity/Warehouse ID must be integers.")
            return

        product = Product(name=name, price=price, quantity=quantity, department=department, warehouse=warehouse)
        self.controller.add_product(product)
        self.tree.insert("", END, values=(product.id, product.name, product.price, product.quantity, product.department, product.warehouse))
        self.clear_entries()

    def clear_entries(self):
        self.entry_name.delete(0, END)
        self.entry_price.delete(0, END)
        self.entry_quantity.delete(0, END)
        self.entry_department.delete(0, END)
        self.entry_warehouse.delete(0, END)