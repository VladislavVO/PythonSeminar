# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. Учтите, что числа могут быть отрицательными
# Пример:
# 67.82 -> 23
# 0.56 -> 11


def check_input_number(inputed):
    is_correct = False
    while not is_correct:
        try:
            number = float(input(f"{inputed}"))
            is_correct = True
        except ValueError:
            print("Please input number")
    return number

def convert_to_list(n):
    if n < 0:
        n = n * -1
    temp_int = str(n)
    temp_int = temp_int.translate({ord('.'): None})  
    new_list = list(temp_int)      
    return new_list

def find_sum(arr):
    result = 0
    for n in range(0, len(arr)):
        result +=int(int(arr[n]))
    print(result)

number = check_input_number('Input number: ')
find_sum(convert_to_list(number))
