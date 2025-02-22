from os.path import exists


def readMatrixFromCIN():
    print("Введите размерность матрицы ≤20: ")
    size = int(input());
    if size > 20:
        print("Вы хотите ввести слишком большую СЛАУ, ОШИБКА")
        exit(1)
    print("Введите точность: ")
    accuracy = float(input())
    print("Введите матрицу: ")
    matrix = [input().strip().split(" ") for i in range(size)]
    for i in range(size):
        try:
            #fprint(len(matrix[i]))
            if len(matrix) != size or len(matrix[i]) != size+1:
                print("Данные чета невалидны")
                exit(1)
        except IndexError:
            print("Данные чета невалидны")
            print("Данные чета невалидны")
            exit(1)
    return matrix, accuracy, size


def readMatrixFromTXT(FilePath):
    if not exists(FilePath):
        print("Такого файла нет:(")
        exit(1)
    with open(FilePath) as f:
        size = int(f.readline());
        if size > 20:
            print("Вы хотите ввести слишком большую СЛАУ, ОШИБКА")
            exit(1)
        accuracy = float(f.readline())
        matrix = [i.strip().split(" ") for i in f.readlines()]
        for i in range(size):
            try:
                if matrix.__len__() != size or matrix[i].__len__() != size+1:
                    print("Данные чета невалидны")
                    exit(1)
            except IndexError:
                print("Данные чета невалидны")
                exit(1)
        return matrix, accuracy, size