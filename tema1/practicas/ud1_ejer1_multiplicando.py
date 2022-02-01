# This Python file uses the following encoding: utf-8
num = int(input('Dame un número entero entre 1 y 10:'))
if (num >= 1 and num <= 10):
    for i in range(1, 11):
        print("%s * %d = %s" % (str(i).rjust(2), num, str(num * i).rjust(2)))
else:
    print('Error: El número debe estar comprendido entre 1 y 10')