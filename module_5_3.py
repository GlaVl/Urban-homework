class House:
    def __init__(self, name, numbers_of_floor):
        self.name = name
        self.numbers_of_floor = numbers_of_floor

    def go_to(self, new_floor):
        if new_floor > int(self.numbers_of_floor) or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.numbers_of_floor

    def __str__(self):
        return f"Название {self.name}, кол-во этажей: {self.numbers_of_floor}"

    def __eq__(self, other):
        if isinstance(other, House):
            return self.numbers_of_floor == other.numbers_of_floor
        return False

    def __lt__(self, other):
        if isinstance(other, House):
            return  self.numbers_of_floor < other.numbers_of_floor
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, House):
            return self.numbers_of_floor <= other.numbers_of_floor
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, House):
            return self.numbers_of_floor > other.numbers_of_floor
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, House):
            return self.numbers_of_floor >= other.numbers_of_floor
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, House):
            return self.numbers_of_floor != other.numbers_of_floor
        return NotImplemented

    def __add__(self, value):
        if isinstance(value, int):
            self.numbers_of_floor += value
            return self
        return NotImplemented

    def __radd__(self, value):
        if isinstance(value, int):
            self.numbers_of_floor += value
            return self
        return NotImplemented

    def __iradd__(self, value):
        if isinstance(value, int):
            self.numbers_of_floor += value
            return self
        return NotImplemented


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__

