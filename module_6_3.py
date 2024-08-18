class Horse:
    def run(self, dx):
        self.x_distance += dx
    x_distance = 0
    sound = 'Frrr'

class Eagle:
    def fly(self, dy):
        self.y_distance += dy
    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'

class Pegasus (Eagle, Horse):
    def move(self, dx: int, dy: int):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(f'{self.sound}')
        return

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()