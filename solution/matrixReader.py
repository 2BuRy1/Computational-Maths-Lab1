def readMatrixFromCIN():
    print("Введите размерность матрицы ≤20: ")
    size = int(input());
    if size > 20:
        return None
    print("Введите точность: ")
    accuracy = float(input())
    print("Введите матрицу: ")
    matrix = [input().strip().split(" ") for i in range(size)]
    for i in range(size):
        try:
            print(len(matrix[i]))
            if len(matrix) != size or len(matrix[i]) != size+1:
                return None, None, None
        except IndexError:
            print("Данные чета невалидны")
            return None, None, None
    return matrix, accuracy, size


def readMatrixFromTXT(FilePath):
    with open(FilePath) as f:
        print("Введите размерность матрицы ≤20: ")
        size = int(f.readline());
        if size > 20:
            return None
        print("Введите точность: ")
        accuracy = float(f.readline())
        matrix = [i.strip().split(" ") for i in f.readlines()]
        for i in range(size):
            try:
                if matrix.__len__() != size or matrix[i].__len__() != size+1:
                    return None
            except IndexError:
                print("Данные чета невалидны")
                return None
        return matrix, accuracy, size