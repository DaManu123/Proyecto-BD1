class Product:
    def __init__(self, product_id, name, price, quantity, department, warehouse):
        self.id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.department = department
        self.warehouse = warehouse

    def __repr__(self):
        return f"Product(id={self.id}, name={self.name}, price={self.price}, quantity={self.quantity}, department={self.department}, warehouse={self.warehouse})"