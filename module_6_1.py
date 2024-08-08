class Animal:

    def __init__(self, name):
        self.name = name
    alive = True
    fed = False

    def eat(self, food):
        if not food.edible:
            self.fed = False
            self.alive = False
            print(f'{self.name} не стал есть {food.name}')
        else:
            self.fed = True
            self.alive = True
            print(f'{self.name} съел {food.name}')

class Plant:

    def __init__(self, name):
        self.name = name

class Mammal(Animal):

    def __init__(self, name):
        self.name = name

class Predator(Animal):

    def __init__(self, name):
        self.name = name

class Flower(Plant):
    def __init__(self, name, edible: bool = False):
        self.name = name
        self.edible = edible

class Fruit(Plant):
    def __init__(self, name, edible: bool = True):
        self.name = name
        self.edible = edible


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

