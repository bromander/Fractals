import turtle as t


codem = 'A'

A = 'B - A - B'
B = 'A + B + A'

def settings(speed, tracer, long, how_many):
    window_width = 1910
    window_height = 1080
    t.setup(width=window_width, height=window_height)

    t.up()
    t.speed(0)
    t.goto(-500, -400)
    t.down()

    t.speed(speed)
    t.tracer(tracer)

    long = long / how_many
    return long

def compiling(codem, how_many):
    code1 = codem.split(' ')
    code2 = codem.split(' ')
    for i in range(0, how_many-1):
        now = 0
        for i in code1:
            if i == 'A':
                code2.pop(now)
                code2.insert(now, f' {A} ')
                now += 1
            elif i == 'B':
                code2.pop(now)
                code2.insert(now, f' {B} ')
                now += 1
            else:
                now += 1
                if now >= len(code1):
                    break
        code2 = ' '.join(code2)
        code2 = code2.split(' ')
        code1 = code2

    return code2

def drawing(long, angle, code):
    for i in code:
        if i == '-':
            t.right(angle)
        elif i == 'A':
            t.forward(long)
        elif i == 'B':
            t.forward(long)
        elif i == '+':
            t.left(angle)

def main(long, angle, codem, how_many, speed, tracer):
    long = settings(speed, tracer, long, how_many)
    codem = compiling(codem, how_many)
    t.left(angle)
    drawing(long, angle, codem)

main(20, 60, codem, 10, 0, 2)

"""
Purpose of variables in 'main' function:

long (1) - the long of section
angle (2) - angle of the segments
codem (3) - reference to a variable 'codem'
how_many (4) - how_many iterations
speed (5) - speed of the turtle (0 - max, 1 - slow, 2 ang > - faster)
tracer (6) - just... tThe same as 'speed' variable
"""


t.exitonclick()