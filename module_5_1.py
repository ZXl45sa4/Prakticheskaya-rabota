class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        self.go_to = int(new_floor)
        i = 0
        if  new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            while i < new_floor:
                i += 1
                print(i)
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 3)
h1.go_to(5)
h2.go_to(10)