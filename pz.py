def summa(list):
    if len(list) == 1:
        return float(list[0])
    else:
        return float(list[0]) + float(summa(list[1:]))


def multi(list):
    if len(list) == 1:
        return float(list[0])
    else:
        return float(list[0]) * float(multi(list[1:]))


def minimum(list):
        mini = float(list[0])
        length = len(list)
        for i in range(length):
            if float(list[i]) < mini: mini = list[i]
        return mini


def maximum(list):
        maxi = float(list[0])
        length = len(list)
        for i in range(length):
            if float(list[i]) > maxi: maxi = float(list[i])
        return(maxi)


def creategiven(filename):
    showFile = open(filename, 'r')
    for string in showFile:
       return string.split(' ')


z = input('Порядок ответов: minValue, maxValue, summ, mult. Для теста на правильное чтение нужен text.txt.'
          'Введите имя файла, вставьте флаг -s: ')
given = creategiven(z)

minValue = minimum(given)
maxValue = maximum(given)
summ = summa(given)
mult = multi(given)
print(minValue, maxValue, summ, mult)
