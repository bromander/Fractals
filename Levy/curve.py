import turtle as t
from progress.bar import Bar

codem = '- f + + f -'

def setting(speed, long, how_many, window_width, window_height):
    tracer = 2
    gotoY = 0
    bar = Bar('Loading Settings... ', max=7)
    bar.next()

    if True:
        if how_many >= 1:
            long = 200
        if how_many >= 4:
            long = 80
        if how_many >= 6:
            long = 40
        if how_many >= 8:
            long = 20
        if how_many >= 10:
            long = 10
            tracer = 3
        if how_many >= 12:
            long = 5
            tracer = 4
        if how_many >= 14:
            long = 2

    bar.next()
    goto = 100
    bar.next()
    t.setup(width=window_width, height=window_height)
    bar.next()

    t.tracer(tracer)

    bar.next()
    t.speed(speed)

    bar.next()

    t.up()

    t.goto(-goto, gotoY)

    t.down()

    bar.next()
    bar.finish()

    return long

def compiling(codem, how_many):
    code1 = codem.split(' ')
    code2 = codem.split(' ')
    for i in range(0, how_many-1):
        now = 0
        for i in code1:
            if i == 'f':
                code2.pop(now)
                code2.insert(now, f' {codem} ')
                now += 1
            else:
                now += 1
                if now >= len(code1):
                    break
        code2 = ' '.join(code2)
        code2 = code2.split(' ')
        code1 = code2

    return code2

def create_curve(codes, long, angle):
    t.showturtle()
    bar = Bar('Drawing... ', max=len(codes))
    for code in codes:
        if code == 'f':
            bar.next()
            t.forward(long)
        elif code == '+':
            bar.next()
            t.right(angle)
        elif code == '-':
            bar.next()
            t.left(angle)
        elif code == '':
            bar.next()
        else:
            print(f'Error, unknown code element: {code}')
            exit()
    t.forward(1)
    t.hideturtle()

def main(long, angle, codem, how_many, speed, window_width, window_height):
    print('Starting...')
    long = setting(speed, long, how_many, window_width, window_height)
    print('Compiling...')
    codes = compiling(codem, how_many)
    create_curve(codes, long, angle)
    print('\nEnd!')


main(100, 45, codem, 10, 0, 1910, 1080)

"""
Purpose of variables in 'main' function:

long (1) - the long of section
angle (2) - angle of the segments
codem (3) - reference to a variable 'codem'
how_many (4) - how_many iterations
speed (5) - speed of the turtle (0 - max, 1 - slow, 2 ang > - faster)
window_width (6) - window width
window_height (7) - window height
"""

t.exitonclick()