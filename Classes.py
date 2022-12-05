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