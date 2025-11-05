from tkinter import Frame, Label, Entry, Button, ttk
from models.warehouse import Warehouse
from controllers.warehouse_controller import WarehouseController

class WarehouseView(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.controller = WarehouseController(self)
        self.create_widgets()
        self.load_warehouses()

    def create_widgets(self):
        Label(self, text="Warehouse Management").grid(row=0, column=1)

        self.tree = ttk.Treeview(self, columns=("ID", "Name"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.grid(row=1, column=0, columnspan=2)

        Label(self, text="Warehouse ID:").grid(row=2, column=0)
        self.entry_id = Entry(self)
        self.entry_id.grid(row=2, column=1)

        Label(self, text="Warehouse Name:").grid(row=3, column=0)
        self.entry_name = Entry(self)
        self.entry_name.grid(row=3, column=1)

        Button(self, text="Add Warehouse", command=self.add_warehouse).grid(row=4, column=0)
        Button(self, text="Delete Warehouse", command=self.delete_warehouse).grid(row=4, column=1)

    def load_warehouses(self):
        warehouses = self.controller.get_all_warehouses()
        for warehouse in warehouses:
            self.tree.insert("", "end", values=(warehouse.id, warehouse.name))

    def add_warehouse(self):
        name = self.entry_name.get()
        if name:
            self.controller.add_warehouse(name)
            self.load_warehouses()

    def delete_warehouse(self):
        selected_item = self.tree.selection()
        if selected_item:
            warehouse_id = self.tree.item(selected_item, 'values')[0]
            self.controller.delete_warehouse(warehouse_id)
            self.load_warehouses()