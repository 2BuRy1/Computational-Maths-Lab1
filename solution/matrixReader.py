from os.path import exists


def readMatrixFromCIN():
    try:
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
            if len(matrix) != size or len(matrix[i]) != size+1:
                print("Данные чета невалидны")
                exit(1)

    except IndexError and ValueError:
        print("Данные чета невалидны")
        exit(1)
    return matrix, accuracy, size


def readMatrixFromTXT(FilePath):
    try:
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
                if matrix.__len__() != size or matrix[i].__len__() != size+1:
                    print("Данные чета невалидны")
                    exit(1)
    except IndexError and ValueError:
        print("Данные чета невалидны")
        exit(1)
    return matrix, accuracy, size


import random

def generateRandomMatrix(size, accuracy_range=(0.0001, 1.0), value_range=(-100, 100)):

    if size > 20:
        print("Вы хотите ввести слишком большую СЛАУ, ОШИБКА")
        exit(1)

    accuracy = round(random.uniform(*accuracy_range), 6)
    matrix = [[str(random.randint(*value_range)) for _ in range(size + 1)] for _ in range(size)]

    return matrix, accuracy, size