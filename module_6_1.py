"""
                        РОДИТЕЛЬ
Для класса Animal атрибуты alive = True(живой) и fed = False(накормленный),
name - индивидуальное название каждого животного.
"""
class Animal:
    alive = True        # Живой
    fed = False         # Накормленный
"""
                        НАСЛЕДНИК
"""

class Predator(Animal):# 'Волк с Уолл-Стрит'
    def __init__(self,name):
        self.name = name
    def eat(self, food):
        self.food = food
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False
"""
                        НАСЛЕДНИК
"""
class Mammal(Animal): #'Хатико'
    def __init__(self,name):
        self.name = name
    def eat(self, food):
        self.food = food
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False
#================================================================================
"""
                        РОДИТЕЛЬ
Для класса Plant атрибут edible = False(съедобность), 
name - индивидуальное название каждого растения
"""
class Plant:
    edible = False

"""
                        НАСЛЕДНИК
"""
class Flower(Plant):    #'Цветик семицветик'
    def __init__(self,name):
        self.name = name
"""
                        НАСЛЕДНИК
"""
class Fruit(Plant): #'Заводной апельсин'
    def __init__(self,name):
        self.name = name
        self.edible = True
#=======================================================================================
animal = Animal()
plant = Plant()
#
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')
# #
print(a1.name)
print(p1.name)
#
print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.