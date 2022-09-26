# 4 - Реализуйте выдачу случайного числа
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time или datetime (миллисекунды или наносекунды) - для задания случайности
# Учтите, что есть диапазон: от(минимальное) и до (максимальное)

def check_input_number(inputed):
    is_correct = False
    while not is_correct:
        try:
            number = float(input(f"{inputed}"))
            is_correct = True
        except ValueError:
            print("Please input number")
    return number

import time
def random(max, min):

    t_data = '%.9f' % time.time()
    time.sleep(0.00001) 
    interval = max - min
    razrad = len(str(interval)) * -1
    smech = int(t_data[razrad:])

    while smech > interval:
        smech = int(smech / 2)

        rnd = min + smech
    return rnd

max = check_input_number('Input number max: ')
min = check_input_number('Input number min: ')
print(random(max,min))