# сортировка пузырьком

# Проходится по массиву несколько раз, сравнивая соседние элементы и
# меняя их местами, если они стоят в неправильном порядке.
# За каждый проход "всплывает" наибольший неотсортированный элемент.
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Оптимизация: если за проход не было обмена - всё отсортировано
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
#
# print(bubble_sort([5, 2, 1, 3]))

# сортировка вставками
# Вставляем каждый элемент на правильное место в уже отсортированной части массива.
# Массив делится на отсортированную и неотсортированную части.
# Берётся очередной элемент и вставляется в нужное место в отсортированной части.
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
#
# сортировка выбором
# Ищем минимальный элемент в неотсортированной части и меняем его с первым элементом неотсортированной части.
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr













