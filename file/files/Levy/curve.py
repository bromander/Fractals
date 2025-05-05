import turtle as t

'''Переменные которые можно изменять:'''
long = 10       #Длинна отрезков
iterations = 8   #Кол-во итераций


codem = '- f + + f -'  #Аксиома фрактала и множество пораждающик правил

#Настройка
def setting(speed, long, how_many, window_width, window_height):
    tracer = 2
    gotoY = 0

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

    goto = 100
    t.setup(width=window_width, height=window_height)
    t.tracer(tracer)
    t.speed(speed)
    t.up()
    t.goto(-goto, gotoY)
    t.down()
    return long

#генерация ключа
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

#Выполнение движения черепашки следуя ключу
def create_curve(codes, long, angle):
    t.showturtle()

    for code in codes:
        if code == 'f':
            t.forward(long)
        elif code == '+':
            t.right(angle)
        elif code == '-':
            t.left(angle)
    t.forward(1)
    t.hideturtle()

def main(long, angle, codem, how_many, speed, window_width, window_height):
    long = setting(speed, long, how_many, window_width, window_height)
    codes = compiling(codem, how_many)
    create_curve(codes, long, angle)


main(long, 45, codem, iterations, 0, 1910, 1080)

t.exitonclick()