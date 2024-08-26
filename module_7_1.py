from pprint import pprint
class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        return f'{self.name},{self.weight},{self.category}'

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        f = open(self.__file_name, 'r')
        products = f.read()
        f.close()
        return products

    def add(self, *products):
        f = open(self.__file_name, 'a')
        for product in products:
            current_products = self.get_products()
            if str(product) not in current_products:
                f.write(product.__str__() + '\n')
                current_products += str(product) + '\n'
            else:
                print(f'Продукт {product} уже есть в магазине')
        f.close()



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())