# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# in:
# - 3
# - 6
# - 2
# - 1
# out:
# 5.099

x_1 = int(input('Enter coordinates for x_1:\n'))
x_2 = int(input('Enter coordinates for x_2:\n'))

y_1 = int(input('Enter coordinates for y_1:\n'))
y_2 = int(input('Enter coordinates for y_2:\n'))

coordinates = ((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2) * 0.5

print(coordinates)
