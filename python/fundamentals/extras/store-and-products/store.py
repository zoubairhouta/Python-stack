from product import Product


class Store:
    products = []

    def __init__(self, name, list_of_products):
        self.name = name
        self.list_of_products = list_of_products

    def add_product(self, new_product):
        if isinstance(new_product, Product):
            Store.products.append(new_product)
        else:
            print("Error: Invalid product. Please enter a valid product.")

    def sell_product(self, product_id):
        for product in Store.products:
            if product.get_id() == product_id:
                Store.products.remove(product)
                print(f"Sold {product.get_name()}.")
                break
        else:
            print("Error: Invalid product ID.")

    def inflation(self, percent_increase):
        for product in Store.products:
            product.update_price(percent_increase, is_increased=True)

    def set_clearance(self, category, percent_discount):
        for product in Store.products:
            if product.get_category() == category:
                product.update_price(percent_discount, is_increased=False)
