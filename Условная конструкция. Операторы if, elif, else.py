number1 = int(input('Введите число: '))
number2 = int(input('Введите число2: '))
number3 = int(input('Введите число3: '))
if number1 == number2 and number2 == number3:
              print(3, 'все три числа равны')
elif number1 == number2 or number2 == number3 or number1 == number3:
              print(2, 'два числа равны между собой')
else:
    print(0, 'равных чисел не обнаружено')