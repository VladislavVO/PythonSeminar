# 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.
# Добавьте проверку числа N: чтобы пользователь не мог ввести буквы.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def check_input_number(inputed):
    is_correct = False
    while not is_correct:
        try:
            number = int(input(f"{inputed}"))
            is_correct = True
        except ValueError:
            print("Please input number")
    return number

def add_in_list(n):
    list = []
    number = 1
    for i in range (1, n+1):
        number *= i
        list.append(number)
    print(f"Произведение чисел от 1 до {n}: {list}")

n = check_input_number('Input number: ')
number = n
add_in_list(number)