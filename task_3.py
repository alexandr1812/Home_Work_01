# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# *Пример:*

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('Введите координаты точки х:\n'))
y = int(input('Введите координаты точки y:\n'))

if x > 0 and y > 0:
    print('первая координатная четерть')
elif x < 0 and y > 0:
    print('вторая координатная четерть')
elif x < 0 and y < 0:
    print('третья координатная четерть')
elif x > 0 and y < 0:
    print('четвертая координатная четерть')