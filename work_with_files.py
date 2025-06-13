# Работа с Файлами в python.

# file_name = open("file_name.txt", "режим открытия")
# работа с файлом
# работа с файлом
# работа с файлом
# file_name.close() - закрытия файла

# w - для записи
# file = open("newfile.txt", "w", encoding="utf-8")
# for i in range(1, 11):
#     file.write(f"{i}\n")
# file.close()

# a - для дозаписи
# file = open("newfile2.txt", "a")
# a = 45
# b = 12
# file.write(str(a + b))
# file.close()

# x - cоздает новый файл, если его нет, иначе ошибка
# file = open("newfile3.txt", "x")


# Режим для чтения
# r - режим для чтения
# file = open("newfile3.txt", "r")
# # read(a) - считывает a - символов из файла
# print(file.read(3))
# print(file.read())

# file = open("newfile3.txt", "r")
# # проход по файлу циклом for
# for line in file:
#     for i in line:
#         print(i)

# file = open("newfile3.txt", "r")
# # readlines() - возвращает список, в котором
# # каждый элемент это строка фалйа
# print(file.readlines())

# Второй способ открытия файла
# with open("newfile3.txt", "r", encoding="utf-8") as file:
#     # работа с открытым файлом
#     print(file.read(5))
#     print(file.read(4))
#     print(file.read(19))
# print(file.read()) - операция над закрытым файлом



# Задание 1
# Дан текстовыйфайл. Необходимо создать новыйфайл,
# в который требуется переписать из исходного файла все
# слова, состоящие не менее чем из семи букв.

# Легкий вариант
# old_file = open("newfile3.txt", "r") # исходный файл со словами
# new_file = open("result.txt", "w") # новый файл, сюда будем записывать
# # слова, длина которых 7 или более
#
# for word in old_file:
#     if len(word)-1 >= 7:
#         new_file.write(word)
#
# old_file.close()
# new_file.close()

# old_file = open("newfile3.txt", "r") # исходный файл со словами
# new_file = open("result.txt", "w") # новый файл, сюда будем записывать
#
# for line in old_file:
#     words = line.split()
#     for word in words:
#          if len(word.replace("\n", "")) >= 7:
#              new_file.write(word + "\n")
#
# old_file.close()
# new_file.close()


# Задание 2
# Дан текстовый файл. Необходимо переписать его
# строки в другой файл. Порядок строк во втором файле
# должен совпадать с порядком строк в заданном файле.

# old_file = open("newfile3.txt", "r")
# new_file = open("result.txt", "w")
#
# for line in old_file:
#     new_file.write(line)

# Задание 3
# Дан текстовый файл. Необходимо переписать его
# строки в другой файл. Порядок строк во втором файле
# должен быть обратным по отношению к порядку строк
# в заданном файле.

old_file = open("newfile3.txt", "r")
new_file = open("result.txt", "w")

lines = old_file.readlines()
for line in lines[::-1]:
    if "\n" not in line:
        line += "\n"
    new_file.write(line)
