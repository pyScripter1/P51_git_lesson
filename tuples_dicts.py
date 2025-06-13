# Модуль 6. Кортежи, множества, словари

# Котреж - неизменяемая, упорядоченная структура данных.
# my_tuple = (34, 12, "hello", True, 2.34, [12, 34, 45], (1, 4, 5))
# print(my_tuple) # выводим кортеж
# print(my_tuple[0]) # выводим элемент по индексу 0
# print(my_tuple[-3]) # отрицательные индексы тоже есть
# print(my_tuple[1:4]) # выводим срез кортежа
#
# # my_tuple[2] = 100 - ОШИБКА! МЕНЯТЬ ЭЛЕМЕНТЫ КОРТЕЖА НЕЛЬЗЯ
# print(my_tuple.index(12)) # выводим индекс элемента 12
# print(my_tuple.count(34)) # выводим количество вхождений 34 в наш кортеж

# test = (45, 23, 8, 9)
# print(len(test)) # длина кортежа
# print(max(test)) # макс. число в кортеже
# print(min(test)) # мин. число в кортеже
# print(sum(test)) # сумма чисел
# И др. функции

# создание кортежа с одним элементом
# my_tuple = (23,)
# print(my_tuple, type(my_tuple))

# создание пустого кортежа
my_typle1 = tuple()
my_typle2 = ()

# tuple(a) - фукнция преобразует объект а в кортеж
# my_tuple = tuple("Hello")
# print(my_tuple)
#
# my_list = [1, 2, 3, 4]
# print(tuple(my_list))

# Кортеж - итерабельный объект
# my_tuple = (34, 12, 89, 56)
#
# for i in my_tuple:
#     print(i)


# Множество - Неупорядоченная, изменяемая структура данных.
# В множестве нет дубликатов!!!

# my_set = {2, 2, 4, 9, 2, 8, 2, 9, 9, 8, 1, 4, 1}
# print(my_set)
# print(my_set[2]) - Индексов нет!!!
# print(my_set[1:4]) - Срезов нет!!

# Функции для работы со множествами
# set(a) - функция переводит объект в множество
# my_set = set("Hello")
# print(my_set)
# my_list = [12, 3, 54, 23, 54]
# my_set = set(my_list)
# print(my_set)
# print(set(23,)) # ошибка

# my_set = set() # создание пустого множества
# print(my_set, type(my_set))
# my_set = {34, 12, 9, 7, 34, 7, 12}
# print(len(my_set))
# print(max(my_set))
# print(min(my_set))
# print(sum(my_set))

# my_set = {89, 45, 1, 9, 1, 3, 3, 7}
# my_set.add(100) # добавляем 100
# my_set.remove(1) # удаление 1 из множества
# print(my_set)
# print(my_set.pop()) # удаляет случайный элемент из множества и возвращает его
# print(my_set)
# my_set.clear() # очищает множество
# print(my_set)



# Словарь - изменяемая, неупорядоченная структура данных
# Словарь - последовательность пар "ключ":"значение".
# dict

# my_dict = {"name":"Daniil", "age":41, "city":"Kazan",
#            "marks":[2, 2, 4, 5, 2, 2, 3], "is_work":False}
# print(my_dict) # выводим словарь
# print(my_dict["name"]) # получаем значение по ключу
# # print(my_dict[23]) - Ошибка, нет ключа 23
# my_dict2 = dict(name="Daniil", age=58, city="Kazan")
# print(my_dict2)
# print(my_dict2["name"])
# print(my_dict2["age"])
# print(my_dict2["city"])

# Методы для работы со словарями
my_dict = {"name":"Daniil", "age":41, "city":"Kazan"}
print(my_dict.get("key", "Такого ключа нет"))
print(list(my_dict.keys())) # получаем список ключей словаря
print(list(my_dict.values())) # получаем список значений словаря
print(list(my_dict.items())) # получаем список пар (ключ, значение)
my_dict["name"] = "Ivan" # меняем значением по ключу
print(my_dict)
my_dict.update({"name":"Kirill"}) # меняем значением по ключу
print(my_dict)
my_dict["second_name"] = "Ivanov" # добавим новую пару
print(my_dict)
my_dict.update({"third_name":"Ivanovich"}) # добавим новую пару
print(my_dict)
my_dict.pop("second_name") # удаляет всю пару по ключу
print(my_dict)
my_dict.popitem() # удаляет ту пару, которая была добавлена последней
print(my_dict)
del my_dict["city"] # удаляет пару по ключу
print(my_dict)
my_dict.clear() # очищаем словарь
print(my_dict)


















