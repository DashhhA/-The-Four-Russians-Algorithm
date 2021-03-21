import unittest
import main
import random


class TestStringMethods(unittest.TestCase):

    def test_randommatrix13size(self):
        self.assertEquals(main.four_russian_algo(first_matrix,second_matrix,result), main.matrixmult(first_matrix, second_matrix))


if __name__ == '__main__':
    size = 13

    first_matrix = [[0 for j in range(size)] for i in range(size)]
    second_matrix = [[0 for j in range(size)] for i in range(size)]
    result = [[0 for j in range(size)] for i in range(size)]

    for i in range(size):
        for j in range(size):
            first_matrix[i][j] = random.randint(0, 1)
            second_matrix[i][j] = random.randint(0, 1)
            result[i][j] = 0

    unittest.main()
