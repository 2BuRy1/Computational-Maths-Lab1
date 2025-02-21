def make_C_and_D_matrix(matrix):
    C = []
    D = []
    print(matrix)

    for i in range(len(matrix)):
        a_ii = matrix[i][i]
        print(f"Диагональный элемент a_{i}{i}: {a_ii}")

        C_row = [0 if i == j else (-matrix[i][j] / a_ii) for j in range(len(matrix) + 1)]
        C.append(C_row)
        D_row = (matrix[i][len(matrix)])/a_ii
        D.append(D_row)
    return C, D


def main_calculation(C, D, matrix):
