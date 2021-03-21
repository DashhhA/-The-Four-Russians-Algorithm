import random
import math

size = 13
pieces_of_first_matrix = list()
pieces_of_second_matrix = list()


# Used resources: https://louridas.github.io/rwa/assignments/four-russians/

def get_column(array, idx):
    sz = len(array)
    columns = [0 for j in range(sz)]

    for i in range(sz):
        columns[i] = array[i][idx]

    return columns


def row_from_bottom(array, k):
    return array[len(array) - k - 1]


def row_sum(A, B):
    sum_row = [0 for j in range(size)]

    for i in range(size):
        if A[i] + B[i] > 0:
            sum_row[i] = 1
        else:
            sum_row[i] = 0

    return sum_row


def number(row):
    num = 0

    for i in range(len(row)):

        if row[i] != 0:
            num += 2 ** i

    return num


def array_sum(A, B):
    res = [[0 for j in range(size)] for i in range(size)]

    for i in range(size):
        for j in range(size):
            res[i][j] = A[i][j] + B[i][j]
            if res[i][j] > 1:
                res[i][j] = 1

    return res


def prep(A, B, m):
    for i in range(int(size / m)):
        add_piece_to_first_matrix(A, m, i * m)
        add_piece_to_second_matrix(B, m, i * m)


def add_piece_to_first_matrix(A, m, idx):
    pieces = [[0 for j in range(m)] for i in range(size)]

    for i in range(m):
        tmp = get_column(A, idx + i)
        for j in range(size):
            pieces[j][i] = tmp[j]

    pieces_of_first_matrix.append(pieces)


def add_piece_to_second_matrix(B, m, idx):
    pieces = [[0 for j in range(size)] for i in range(m)]
    for i in range(m):
        pieces[i] = B[idx + i]

    pieces_of_second_matrix.append(pieces)


def four_russian_algo(A, B, res):
    m = math.floor(math.log10(size))

    for i in range(int(math.ceil(size / m))):
        r_s = [[0 for j in range(size)] for i in range(2 ** m)]

        for d in range(size):
            r_s[0][i] = 0

        prep(A, B, m)

        bp = 1
        k = 0
        for j in range(1, 2 ** m):
            r_s[j] = row_sum(r_s[j - (2 ** k)], row_from_bottom(pieces_of_second_matrix[i], k))

            if bp == 1:
                bp = j + 1
                k = k + 1
            else:
                bp = bp - 1

        piece_of_result = [[0 for j in range(size)] for i in range(size)]

        for j in range(size):
            piece_of_result[j] = r_s[number(pieces_of_first_matrix[i][j])]

        res = array_sum(res, piece_of_result)

    return res

# for tests
# https://stackoverflow.com/questions/10508021/matrix-multiplication-in-pure-python
def matrixmult(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        print("Cannot multiply the two matrices. Incorrect dimensions.")
        return

    # Create the result matrix
    # Dimensions would be rows_A x cols_B
    C = [[0 for row in range(cols_B)] for col in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]

                if C[i][j] > 1:
                    C[i][j] = 1

    return C


if __name__ == '__main__':
    first_matrix = [[0 for j in range(size)] for i in range(size)]
    second_matrix = [[0 for j in range(size)] for i in range(size)]
    result = [[0 for j in range(size)] for i in range(size)]

    for i in range(size):
        for j in range(size):
            first_matrix[i][j] = random.randint(0, 1)
            second_matrix[i][j] = random.randint(0, 1)
            result[i][j] = 0

    copy_first = first_matrix
    copy_second = second_matrix

    print("Four russians: " + str(four_russian_algo(first_matrix, second_matrix, result)))
    print("\nSimple multiplication: " + str(matrixmult(copy_first, copy_second)))
