# Задание 1

class Bottle:
    color = 'color'
    volume = 0.0

b1 = Bottle()
b2 = Bottle()
b3 = Bottle()

b1.color = 'Красная'
b2.color = 'Белая'
b3.color = 'Черная'

b1.volume = 0.7
b2.volume = 0.3
b3.volume = 1.0

print(b1.color, b1.volume)
print(b2.color, b2.volume)
print(b3.color, b3.volume)

# Задание 2

class Bottle:
    color = 'color'
    contains = 0
    def get_content(self):
        return self.contains

    def fill(self, volume):
       self.contains += volume
       return self.contains

b1 = Bottle()
b2 = Bottle()

b1.color = 'Красная'
b2.color = 'Синяя'

print(b1.color, b1.get_content())
b1.fill(100)
print(b1.color, b1.get_content())
print(b2.color, b2.get_content())
b2.fill(500)
print(b2.color, b2.get_content())