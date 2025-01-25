import turtle as t
from progress.bar import Bar

codem = 'f + f - - f + f'
code = ''

def setting(speed, long, how_many, window_width, window_height):
    delitel = 2
    bar = Bar('Setting... ', max=7)
    bar.next()
    gotoY = 0
    goto = 0
    t.setup(width=window_width, height=window_height)
    bar.next()
    t.tracer(2)
    long = long / (how_many + 1)
    bar.next()
    t.speed(speed)
    bar.next()

    if how_many <= 3:
        goto = 300
    if how_many >= 4:
        gotoY = 50
        goto = 500
    if how_many >= 6:
        gotoY = 100
        goto = 900
    if how_many > 6:
        print(f'Error, too big iteration!')
        exit()
    bar.next()

    t.up()
    t.goto(-goto, -gotoY)
    t.down()
    bar.next()

    for i in range(0, how_many):
        long = long / delitel
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

    print(f'\ncode = {' '.join(code2)}\n')
    return code2

def create_curve(codes, long, angle):
    bar = Bar('Drawing... ', max=len(codes))
    t.showturtle()
    for code in codes:
        bar.next()
        if code == 'f':
            t.forward(long)
        elif code == '+':
            t.left(angle)
        elif code == '-':
            t.right(angle)
        elif code == '':
            pass
        else:
            print(f'Error, unknown code element: {code}')
            exit()
    bar.finish()
    t.forward(1)
    t.hideturtle()

def main(long, angle, codem, how_many, speed, window_width, window_height):
    print('Starting...')
    long = setting(speed, long, how_many, window_width, window_height)
    print('Compiling...')
    codes = compiling(codem, how_many)
    create_curve(codes, long, angle)
    print('End!')


how_many = int(input('\n>> Enter the number of iterations: '))

main(500, 45, codem, how_many, 100, 1910, 1080)

t.exitonclick()