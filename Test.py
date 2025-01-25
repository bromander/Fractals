

code = 'f + f - - f + f'
code1 = code.split(' ')
code2 = code.split(' ')

how_many = 2
now = 0
string = []
print(code)
print('f + f - - f + f + f + f - - f + f - - f + f - - f + f + f + f - - f + f')
for i in code1:
    if i == 'f':
        code2.pop(now)
        code2.insert(now, f' {code} ')
        now += 1
    else:
        now += 1
        if now >= len(code1):
            now = 0
            break

print((' '.join(code2)))