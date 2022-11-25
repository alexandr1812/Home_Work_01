# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# *Пример:*

# - 6 -> да
# - 7 -> да
# - 1 -> нет
# number_day = int(input('введите день недели:\n'))

while True:
    num_day = int(input('Enter the day of the week:\n'))
    if num_day == 6 or num_day == 7:
        print("Weekday")
        break
    elif num_day > 0 and num_day < 6:
        print("Workday")
        break
    elif num_day <= 0 or num_day > 7:
        print("lt's not a day of the week!\nTry again")

    