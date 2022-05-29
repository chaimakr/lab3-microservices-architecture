class Product:
    def __init__(self, product_code, warehouse, product_category, date, order_demand):
        self.product_code = product_code
        self.warehouse = warehouse
        self.product_category = product_category
        self.date = date
        self.order_demand = order_demand
    
    def set_code(self, product_code):
        self.product_code = product_code

    def set_warehouse(self, warehouse):
        self.warehouse = warehouse

    def set_product_category(self, product_category):
        self.product_category = product_category

    def set_date(self, date):
        self.date = date

    def set_order_demand(self, order_demand):
        self.order_demand = order_demand