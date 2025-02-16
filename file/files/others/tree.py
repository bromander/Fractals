import turtle as t


t.setup(width=1910, height=1080)
t.speed(0)
t.tracer(0)

t.up()
t.goto(0, -400)
t.down()

codem = 'X F'

code = ''

X = 'F − [ [ X ] + X ] + F [ + F X ] − X'
F = 'F F'

codem.split(' ')

def compiling(codem, how_many):
    code1 = codem.split(' ')
    code2 = codem.split(' ')
    for i in range(0, how_many-1):
        now = 0
        for i in code1:
            if i == 'X':
                code2.pop(now)
                code2.insert(now, f' {X} ')
                now += 1
            elif i == 'F':
                code2.pop(now)
                code2.insert(now, f'{F}')
                now += 1
            else:
                now += 1
                if now >= len(code1):
                    break
        code2 = ' '.join(code2)
        code2 = code2.split(' ')
        code1 = code2

    print(f'\ncode = {' '.join(code2)}\n')
    return code2

def drawing(angle, long, codes):
    t.left(65)
    coord = []
    for i in codes:
        if i == 'F':
            t.forward(long)
        elif i == '-':
            t.right(angle)
        elif i == '+':
            t.left(angle)
        elif i == '[':
            coord.append((t.pos(), t.heading()))
            print(f'Добавляется, coord = {coord}')
        elif i == ']':
            goto, heading = coord.pop()
            t.up()
            t.goto(goto)
            t.setheading(heading)
            t.down()
            print(f'Возвращается, coord = {coord}')

def main(angle, long, codem, how_many):
    code = compiling(codem, how_many)
    drawing(angle, long, code)

loong = int(input('Введите длину отрезка:'))
how = int(input('Введите кол-во итераций:'))

main(25, loong, codem, how)

"""
Purpose of variables in 'main' function:

angle (1) - angle of the segments
long (2) - the long of section
codem (3) - reference to a variable 'codem'
how_many (4) - how_many iterations
"""

t.exitonclick()