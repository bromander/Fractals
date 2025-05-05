import turtle as t

'''Переменные которые можно изменять:'''
long = 15       #Длинна отрезков
iterations = 4   #Кол-во итераций


codem = 'F + F + F + F'  #Аксиома фрактала

F = 'F F + F + F + F + F F' #множество пораждающих правил

#Настройка
def setting():
    t.setup(width=1910, height=1080)
    t.speed(0)
    t.tracer(5)
    t.up()
    t.goto(-400, -300)
    t.down()

#генерация ключа
def compiling(codem, how_many):
    code1 = codem.split(' ')
    code2 = codem.split(' ')
    for i in range(0, how_many-1):
        now = 0
        for i in code1:
            if i == 'F':
                code2.pop(now)
                code2.insert(now, f' {F} ')
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

#Выполнение движения черепашки следуя ключу
def drawing(angle, long, codes):
    for i in codes:
        if i == 'F':
            t.forward(long)
        elif i == '-':
            t.right(angle)
        elif i == '+':
            t.left(angle)

def main(angle, long, codem, how_many):
    setting()
    code = compiling(codem, how_many)
    drawing(angle, long, code)


main(90, long, codem, iterations)


t.exitonclick()