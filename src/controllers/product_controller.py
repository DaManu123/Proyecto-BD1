class ProductController:
    def __init__(self, product_view, database):
        self.product_view = product_view
        self.database = database
        self.product_view.load_products_button.config(command=self.load_products)

    def load_products(self):
        products = self.database.fetch_all_products()
        self.product_view.populate_product_treeview(products)