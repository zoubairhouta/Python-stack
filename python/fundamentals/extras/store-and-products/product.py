class Product:
    id_counter = 0

    def __init__(self, name, price, category):
        self._id = Product.id_counter
        Product.id_counter += 1
        self._name = name
        self._price = price
        self._category = category

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_category(self):
        return self._category

    def update_price(self, percent_change, is_increased):
        if is_increased:
            self._price *= (1 + percent_change)
        else:
            self._price *= (1 - percent_change)

    def print_info(self):
        print(f"The ID of the product is {self._id}")
        print(f"The name of the product is {self._name}")
        print(f"The category of the product is {self._category}")
        print(f"The price of the product is {self._price}")
