class Horse: #класс описывающий лошадь
    def __init__(self):
        self.x_distance = 0  # пройденный путь
        self.sound = 'Frrr'  # звук, который издаёт лошадь

    def run(self, dx):  #где dx - изменение дистанции
        self.x_distance += dx   #увеличивает x_distance на dx

class Eagle:    # класс описывающий орла
    def __init__(self):
        self.y_distance = 0  # высота полёта
        self.sound = 'I train, eat, sleep, and repeat'  # звук, который издаёт орёл (отсылка)

    def fly(self, dy):  #где dy - изменение дистанции
        self.y_distance += dy   #увеличивает y_distance на dy

class Pegasus (Horse, Eagle):   #класс описывающий пегаса
    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)

    def move(self, dx: int, dy: int):   #где dx и dy изменения дистанции/
        self.run(dx)    #запускаться наследованные методы run
        self.fly(dy)    ##запускаться наследованные методы fly

    def get_pos(self):  #возвращает текущее положение пегаса в виде кортежа
        return (self.x_distance, self.y_distance)

    def voice(self):    #который печатает значение унаследованного атрибута sound
        print(f'{self.sound}')
        return

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()