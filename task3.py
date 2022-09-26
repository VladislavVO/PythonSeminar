# 3 - Палиндромом называется слово, которое в обе стороны читается одинаково: "шалаш", "кабак".
# А еще есть палиндром числа - смысл также в том, чтобы число в обе стороны читалось одинаково, но есть одно "но".
# Если перевернутое число не равно исходному, то они складываются и проверяются на палиндром еще раз.
# Это происходит до тех пор, пока не будет найден палиндром.
# Напишите такую программу, которая найдет палиндром введенного пользователем числа

def check_input_number(inputed):
    is_correct = False
    while not is_correct:
        try:
            number = int(input(f"{inputed}"))
            is_correct = True
        except ValueError:
            print("Please input number")
    return number

def find_palindrom (number):
    number = str(number)
    while True:
        number2 = "".join(reversed(number))
        if number2 == number:
            print("Poly is: ", number2)
            break
        else:
            number = str(int(number) + int(number2))

number = check_input_number('Input number: ')
find_palindrom (number)