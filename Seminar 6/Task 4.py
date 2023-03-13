"""Создайте словарь с количеством элементов не менее 5-ти.
Поменяйте местами первый и последний элемент объекта.
 Удалите второй элемент. Добавьте в конец ключ «new_key» со значением «new_value». Выведите на печать итоговый словарь. Важно, чтобы словарь остался тем же (имел тот же адрес в памяти).
"""
dict = {
   "key1": "первый",
   "key2": "второй",
   "key3": "третий",
   "key4": "четвёртый",
   "key5": "пятый"
}

first_key = list(dict.keys())[0]
last_key = list(dict.keys())[-1]
first_value = dict[first_key]
last_value = dict[last_key]
dict[first_key] = last_value
dict[last_key] = first_value

del dict[list(dict.keys())[1]]

dict["new_key"] = "new_value"

print(dict)