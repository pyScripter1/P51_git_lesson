# Строки продолжение. Таблица ASCII

# ord(a) - возвращает код символа а из таблицы ASCII
# print(ord("🛺"))

# chr(a) - возвращает символ кода а
# print(chr(3456))

# for i in range(10000, 30000):
#     print(chr(i), end=" ")

# Срезы - часть строк.
# text[START:STOP:STEP]
# text = "Programming"
# print(text[0:8])
# print(text[10::-1])
# print(text[::2])
# print(text[1::2])

# text = "hello"
# print(text[::].upper() * 2)

# Проверка на палиндром
# word = input("Введите слово: ")
#
# if word.lower() == word[::-1].lower():
#     print("Good")
# else:
#     print("Bad")


# логический оператор in со строками
# print("a" in "Msh")

# Пользователь вводит строчку, программа должна вывести Yes, если
# в этой строке есть гласная, иначе выводит No

# word = input("Введите строку: ").lower()
# vowels = "aeuioy"
#
# for i in word:
#     if i in vowels:
#         print("Yes")
#         break
# else:
#     print("No")


# Пользователь вводит двузначное число, программа должна поменять цифры местами
# num = input("Введите число: ")
# print(num[::-1])
# a, b = num[0], num[1]
# print(b+a)


# Список - упорядоченная, изменяемая структура данных.
# Список - набор элементов.
# a = 8
# my_list = [23, 45, -12, [1, 2, 3], "hello", a, 2.1, 90, 7]
# print(my_list) # выводим весь список
# print(my_list[4]) # "hello"
# # print(my_list[100]) # - Error
# print(my_list[-1]) # 7
# a = [] # пустой список
# print(a)

# можно поменять элемент списка по его индексу
# test = [1, 2, 3, 4, 5]
# test[2] = 45
# print(test)


# Срезы
# numbers = [12, 90, 45, 23, 9, 0, 23, 34, 234, 23, 34, 12, 54, 10, 67]
# print(numbers[1:4])
# print(numbers[::-1])
# print(numbers[1::2])
# print(numbers[0:len(numbers)//2])


# Функцию для работы со списками
# len(list) - функция, которая возвращает длину списка (кол-во элементов)
# print(len([156, 234, 93]))

# max(list) - функция, которая возвращает максимум вашего числового!!!
# списка
# my_list = [1, 43, 909, 23, 0]
# print(max(my_list))
# print(min(my_list))

# sum(list) - функция, которая возвращает сумму списка
# my_list = [1, 2, 3, 4, 5, 6]
# print(f"Сумма = {sum(my_list)}")

# list1 = [1, 2, 3, 4, 5, 9]
# print(sum(list1)/len(list1))

# list(a) - функция преобразует объект а в список (если это возможно)
print(list("hello world"))
print(list(range(1, 101)))
print(list([1, 2, 3]))





