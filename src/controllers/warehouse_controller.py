class WarehouseController:
    def __init__(self, warehouse_view, database):
        self.warehouse_view = warehouse_view
        self.database = database
        self.warehouse_view.load_button.config(command=self.load_warehouses)

    def load_warehouses(self):
        warehouses = self.database.fetch_all_warehouses()
        self.warehouse_view.clear_treeview()
        for warehouse in warehouses:
            self.warehouse_view.insert_warehouse(warehouse)