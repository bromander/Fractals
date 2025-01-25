import turtle as t
from progress.bar import Bar

codem = '- f + + f -'
code = ''

def setting(speed, long, how_many, window_width, window_height):
    tracer = 2
    bar = Bar('Loading Settings... ', max=7)
    bar.next()

    if True:
        if how_many >= 1:
            long = 200
        if how_many >= 4:
            long = 100
        if how_many >= 6:
            long = 40
        if how_many >= 8:
            long = 20
        if how_many >= 10:
            gotoY = 100
            long = 10
            tracer = 3
        if how_many >= 12:
            gotoY = 200
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
            t.left(angle)
        elif code == '-':
            bar.next()
            t.right(angle)
        elif code == '':
            bar.next()
            pass
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


main(200, 45, codem, 15, 100, 1910, 1080)

t.exitonclick()