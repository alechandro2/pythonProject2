# Программа просит ввести числа от 1 до 99
# Вводим числа : 2 11 14 23 25 33 38  45 46 58 60 77  81 94 98
# Программа попросит ввести число от 1 до 99
# Вводим число: 38
# Ответ : 6 (программа показывает количество чисел  перед введенным числом).
# Если введёное число имеет отрицательное значение, то программа выдаст ответ: "Неправильный диапазон!"
# Если введённого числа нет в списке для ввода, например число 333 то, FALSE.

array = [int(x) for x in input("Введите числа от 1 до 99 в любом порядке, через пробел: ").split()]
def merge_sort(array):  # "разделяй"
    if len(array) < 2:  # если кусок массива равен 2,
        return array[:]  # выходим из рекурсии
    else:
        middle = len(array) // 2  # ищем середину
        left = merge_sort(array[:middle])  # рекурсивно делим левую часть
        right = merge_sort(array[middle:])  # и правую
        return merge(left, right)  # выполняем слияние
def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result
print(merge_sort(array))
while True:
    try:
        element = int(input("Введите число от 1 до 99:"))
        if element < 0 or element > 99:
            raise Exception
        break
    except ValueError:
        print("Нужно ввести число!")
    except Exception:
        print("Неправильный диапазон!")

def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует
    middle = (right + left) // 2  # находим середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)

if element <= min(array) or element > max(array):
    print("Условие не удовлетворяется")
else:
    print(binary_search(array, element, 0, len(array)-2))