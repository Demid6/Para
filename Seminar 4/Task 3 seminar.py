# Задача “Новая акция” в.магазине “Долголетие”:
# 1. Если на кассе пробиваются:три товара По возрастанию цен (25,
# 100,310), то выводится "Акция!", а сумма'к оплате делится пополам.
# 2. 2. Если на кассе пробиваются три товара по убыванию цен
# (2500, 400, 50), то выводится "Акция!", а сумма'к оплате делится на 3.
# 3. Во всех остальных случаях сообщение "Акция!" не выводится.
# Покупатель видит только надпись "К оплате:" Напиши
# программу, считающую сумму к оплате:


elements = []
summa_elements = 0
for i in range(3):
    price = int(input("Введите цену товара:"))
    summa_elements += price
    elements.append(price)

if elements[0] > elements[1] > elements[2]:
    summa_elements /= 3
    print("К оплате:", round(summa_elements), "руб")
elif elements[0] < elements[1] < elements[2]:
    summa_elements /= 2
    print("К оплате:", round(summa_elements), "руб")
else:
    print("К оплате:", round(summa_elements), "руб")
