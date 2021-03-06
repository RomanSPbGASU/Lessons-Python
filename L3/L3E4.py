from datetime import datetime
from locale import *
while 1:
    try:
        monthNum = int(input("Введите номер месяца: "))
        if monthNum < 1 or monthNum > 12:
            raise Exception("Номер месяца должен быть от 1 до 12")
        break
    except ValueError:
        print("Ошибка. Введите число")
    except Exception as ex:
        print(ex)
while 1:
    try:
        firstWeekday = int(input("Введите номер первого дня месяца: "))
        if 1 > firstWeekday or firstWeekday > 7: 
            raise Exception("Номер дня недели должен быть от 1 до 7")
        break
    except ValueError:
        print("Ошибка. Введите число")
    except Exception as ex:
        print(ex)
setlocale(LC_ALL, "ru")
monthLen = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month = datetime(1, monthNum, 1, 0, 0)
print("{:^50}".format(month.strftime("%B")), end = "")
for i in range(0, monthLen[monthNum - 1] + firstWeekday - 1):
    if i % 7 == 0:
        print()
    print(" {: <6}".format("" if i + 1 < firstWeekday else i - firstWeekday + 2), end = "")
print()