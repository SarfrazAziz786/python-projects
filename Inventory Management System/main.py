from abc import ABC, abstractmethod 
from datetime import datetime


class Product(ABC):   #ABC makes Product an abstract base class, meaning it can’t be instantiated directly.
    def __init__(self, product_id: str, name: str, price: float, quantity: int):
        self._product_id = product_id   #protected attribute single underscore
        self._name = name               #protected attribute single underscore
        self._price = price             #protected attribute single underscore
        self._quantity_in_stock = quantity #protected attribute single underscore

    @property  #property decorator to create getter methods
    def product_id(self):
        return self._product_id

    @property   #property decorator to create getter methods
    def name(self):
        return self._name

    @property   #property decorator to create getter methods
    def price(self):
        return self._price

    @property           #property decorator to create getter methods
    def quantity(self):
        return self._quantity_in_stock

    def restock(self, amount: int):    
        if amount > 0:
            self._quantity_in_stock += amount

    def sell(self, quantity: int):
        if quantity <= self._quantity_in_stock:
            self._quantity_in_stock -= quantity
            return True
        return False

    def get_total_value(self):
        return self._price * self._quantity_in_stock

    @abstractmethod 
    def __str__(self) -> str:
        pass        

class Electronics(Product):     #inharit from Product class
    def __init__(self, product_id: str, name: str, price: float, quantity: int,
                 warranty_years: int, brand: str):
        super().__init__(product_id, name, price, quantity)
        self._warranty_years = warranty_years
        self._brand = brand

    def __str__(self) -> str:   ##override __str__ method to provide string representation of the object
        return f"Electronics - {self._name} ({self._brand}) | ID: {self._product_id} | " \
               f"Price: Rs.{self._price:.2f} | Stock: {self._quantity_in_stock} | " \
               f"Warranty: {self._warranty_years} years"

class Grocery(Product):   #inharit from Product class
    def __init__(self, product_id: str, name: str, price: float, quantity: int,
                 expiry_date: datetime): #use datetime for expiry date
        super().__init__(product_id, name, price, quantity)
        self._expiry_date = expiry_date

    def is_expired(self):
        return datetime.now() > self._expiry_date #check if the product is expired

    def __str__(self):   ##override __str__ method to provide string representation of the object
        return f"Grocery - {self._name} | ID: {self._product_id} | " \
               f"Price: Rs.{self._price:.2f} | Stock: {self._quantity_in_stock} | " \
               f"Expires: {self._expiry_date.strftime('%Y-%m-%d')}"

class Clothing(Product):
    def __init__(self, product_id: str, name: str, price: float, quantity: int,
                 size: str, material: str):
        super().__init__(product_id, name, price, quantity)
        self._size = size
        self._material = material

    def __str__(self):
        return f"Clothing - {self._name} | ID: {self._product_id} | " \
               f"Price: Rs.{self._price:.2f} | Stock: {self._quantity_in_stock} | " \
               f"Size: {self._size} | Material: {self._material}"

class Inventory:
    def __init__(self):
        self._products = {}

    def add_product(self, product: Product) -> None:
        self._products[product.product_id] = product  #use product_id as key 

    def remove_product(self, product_id: str):
        if product_id in self._products:
            del self._products[product_id]
            return True
        return False

    def search_by_name(self, name: str):
        return [product for product in self._products.values() #list comprehension to filter products
                if name.lower() in product.name.lower()]

    def search_by_type(self, product_type: type):
        return [product for product in self._products.values()  #list comprehension to filter products by type
                if isinstance(product, product_type)]

    def list_all_products(self):
        return list(self._products.values())

    def sell_product(self, product_id: str, quantity: int):
        product = self._products.get(product_id)
        if product:
            return product.sell(quantity)
        return False

    def restock_product(self, product_id: str, quantity: int):
        product = self._products.get(product_id)
        if product:
            product.restock(quantity)
            return True
        return False

    def total_inventory_value(self) -> float:
        return sum(product.get_total_value() for product in self._products.values())

    def remove_expired_products(self):
        expired_products = []
        for product_id, product in list(self._products.items()):
            if isinstance(product, Grocery) and product.is_expired():
                del self._products[product_id]
                expired_products.append(product_id)
        return expired_products


def main():
    # Create an inventory instance or object
    inventory = Inventory()

    # Add some products
    mobile = Electronics("M001", "V60", 34000, 5, 1, "LG")
    banana = Grocery("G001", "Banana", 200, 100, datetime(2025, 5, 30))
    tshirt = Clothing("C001", "Cotton T-Shirt", 400, 50, "M", "Cotton")

    inventory.add_product(mobile)
    inventory.add_product(banana)
    inventory.add_product(tshirt)

    # Display all products
    print("\nAll Products:")
    for product in inventory.list_all_products():
        print(product)

    # Sell some products
    print("\nSelling 2 Mobiles...")
    if inventory.sell_product("E001", 2):
        print("Sale successful!")
    
    # Check total value
    print(f"\nTotal inventory value: Rs.{inventory.total_inventory_value():.2f}")

    # Search by name
    print("\nSearching for 'cotton':")
    for product in inventory.search_by_name("cotton"):
        print(product)

if __name__ == "__main__":
    main()