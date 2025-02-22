import solution.matrixPrinter as printer


def make_C_and_D_matrix(matrix):
    C = []
    D = []

    for i in range(len(matrix)):
        a_ii = matrix[i][i]

        C_row = [0 if i == j else (-matrix[i][j] / a_ii) for j in range(len(matrix))]
        C.append(C_row)
        D_row = (matrix[i][len(matrix)])/a_ii
        D.append(D_row)
    return C, D


def get_tochnost(x_k, x_k1):

    a = [abs(x_k[i] - x_k1[i]) for i in range(len(x_k))]
    return max(a)

def main_calculation(C, D, EPS, n):
    iterations = 0;
    x_k=D
    x_k1= [0] * n
    while not (get_tochnost(x_k, x_k1) < EPS) :
        x_k, x_k1 = x_k1, [0] * n
        if iterations == 0:
            x_k = D
            x_k1 = [0] * n

        for i in range(n):
            x = 0
            for j in range(i, n):
                x+= (C[i][j] * x_k[j])
            #print(x)
            for k in range(0, i):
                x+= (C[i][k] * x_k1[k])
            x+= D[i]
            x_k1[i] = float(round(x, 6))
            #print(x)
        #print(x_k1)
        iterations+=1
        printer.printFinalTable(iterations, x_k, round(get_tochnost(x_k, x_k1), 5))

    return x_k1, iterations