class Horse:
    def __init__(self):
        self.x_distance = 0
        self.sound = "Frrr"

    def run(self, dx):
        self.x_distance += dx
        return self.x_distance


class Eagle:
    def __init__(self):
        self.y_distance = 0
        self.sound = "I train, eat, sleep, and repeat"

    def fly(self, dy):
        self.y_distance += dy
        return self.y_distance


class Pegasus(Horse, Eagle):
    def __init__(self):
        super().__init__()
        Eagle.__init__(self)

    # Не понимаю почему этот кусок не работает? Поэтому только явная инициализация 2го родительского класса (выше).
    # def __init__(self):
    #     super().__init__(x_distance, y_distance)
    #     self.x_distance = x_distance
    #     self.y_distance = y_distance

    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)
        return self.x_distance, self.y_distance

    def get_pos(self):
        position = (self.x_distance, self.y_distance)
        return position

    def voice(self):
        print(self.sound)


p1 = Pegasus()


print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
