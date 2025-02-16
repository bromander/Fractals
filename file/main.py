import os

files = ['Fractals especially for the project', 'Hilbert', 'Koch', 'Levy', 'others', 'Sierpinski']

def main():
    print('\n'*20)
    print('Добро пожаловать в программу для генерации фракталов')
    print('Выберите создателя/группу фракталов:\n')
    os.chdir('files')
    print(', '.join(os.listdir()))
    while True:
        fract = str(input('>> '))
        try:
            os.chdir(fract)
            break
        except FileNotFoundError:
            print('Неправильное название директории, попробуйте ещё раз')
    print('Выберите файл: ')
    print(', '.join(f for f in os.listdir() if not f.endswith('.py')))
    while True:
        fracts = str(input('>> '))
        if fracts in os.listdir():
            os.system(fracts)
            return
        else:
            print('Ошибка, неправильное название')

while True:
    main()