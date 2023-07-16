from store import Store
from product import Product

# Create instances of the Product class
product1 = Product("T-shirt", 20, "Clothing")
product2 = Product("Headphones", 50, "Electronics")
product3 = Product("Book", 15, "Books")

# Create an instance of the Store class
store = Store("hammam-lif", [])

# Add the products to the store
store.add_product(product1)
store.add_product(product2)
store.add_product(product3)

# Test the sell_product method using unique product ID
store.sell_product(1)

# Test the inflation method
store.inflation(0.1)

# Test the set_clearance method
store.set_clearance("Clothing", 0.2)

# Print the updated product information
for product in Store.products:
    product.print_info()
