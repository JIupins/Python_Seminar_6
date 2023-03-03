# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести склавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d. Каждое число вводится с новой строки.
# Пример: Ввод: 7 2 5  =>  Вывод: 7 9 11 13 15

def create_number(phrase):
    number = int(input(phrase))
    return number


def create_list(one, two, three):
    new_list = [i for i in range(one, (three - 1) * two + one + two, two)]
    print(f"Создан массив элементов {new_list} .")


num_one = create_number("Введите 1-й элемент арифметической прогрессии: ")
num_two = create_number("Введите разность между эллементами: ")
num_three = create_number("Введите кол-во элементов арифметической прогрессии: ")

create_list(num_one, num_two, num_three)
