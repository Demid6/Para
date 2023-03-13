category = input('Категория товара: ')
if category == 'продукты':
    money = int(input('ввод цены: '))
    if money <= 100:
        print('Попробуй нашу выпечку!')
    elif 100 > money > 500:
        print('Как на счёт орехов в шоколаде?')
    elif money > 500:
        print('Попробуй экзотические фрукты!')
else:
    print('Загляните в товары для дома!')
