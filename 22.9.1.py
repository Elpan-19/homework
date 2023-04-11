array =  [int(x) for x in input('Введите положительные числа через пробел: ').split()]

def list_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

array = list_sort(array)
print(array)
while True:
    try:
        element = int(input('Введите число из списка '))
        if element < min(array) or element > max(array):
            print('Введенное число не входит в диапазон списка')
        if element <= 0:
            raise Exception
        break
    except ValueError:
        print('Введите целое число')
    except Exception:
        print('Введите положительное число')

def binary_search(array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

print(binary_search(array, element, 0, len(array) - 1))