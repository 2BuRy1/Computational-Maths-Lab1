import solution.matrixReader as reader
import solution.matrixValidator as validator
import solution.calculations as calculations

def getData():
    flag = input("Если хотите вводить данные через файл, напишите f, иначе введите любой символ: ") == "f"

    if flag:
        print("Введите название файла: ")
        matrix, accuracy, n = reader.readMatrixFromTXT(input().strip())
    else:
        matrix, accuracy, n = reader.readMatrixFromCIN()
    return matrix, accuracy, n


def main():
    matrix, accuracy, n = getData()
    matrix = validator.parseMatrixValues(matrix)
    if not validator.check_diagonal_dominance(matrix, n):
        matrix = validator.do_diagonal_dominance(matrix)
        if (matrix == None):
            print("Ну все, кранты йоу " + "пока!!")
            exit(1)
    C, D = calculations.make_C_and_D_matrix(matrix)
   # print(D)
  #  print(C)
    calculations.main_calculation(C, D , accuracy, n)


if __name__ == "__main__":
    main()
