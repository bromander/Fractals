'''Здесь я просто проверяю всякие вещи'''

import turtle as t

long = 100
angle = 90

codes = 'F X + Y F + + − F X + Y F + − Y F + + − F X + Y F + + − F X + Y F + − Y F + − − F X + Y F + − Y F +'
X = 'X + Y F +'
Y = '− F X − Y'

codes.split(' ')

for i in codes:
    if i == 'F':
        t.forward(long)
    elif i == '-':
        t.left(angle)
    elif i == '+':
        t.right(angle)

t.exitonclick()