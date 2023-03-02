kol = int(input('Введите количество слов, котороgu собираетесь ввести: '))
text = ''

for i in range(1, kol + 1):
    word = input()
    text = text + word + ' '
    word =''

print(text)

def z2():
    word = input()
    word1 = ''

    while word != 'stop':
        word1 += word + ' '
        word = input()

    print(word1)

z2()

def z3():
    word = input()

    if ('ф' in word) or ('Ф' in word):
        print('Ого! Вы нашли чёртову ф!!')
    else:
        print('У вас не редкое слово :)')

z3()

def z4():
    import random

    f = 0

    while f < 3:
        r = random.randint(0, 11)
        d = random.randint(0, 11)
        a = int(input(str(r) + '+' + str(d) + '='))
        if a == r + d:
            print('Правильно!')
        else:
            print('Не верно :(')

z4()
