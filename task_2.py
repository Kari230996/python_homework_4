'''
1. Напишите функцию для транспонирования матрицы
'''

def transpose_matrix(matrix):
    if not matrix:
        return []
    
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    transposed = [[0 for _ in range(num_rows)] for _ in range(num_cols)]

    for i in range(num_rows):
        for j in range(num_cols):
            transposed[j][i] = matrix[i][j]

    return transposed

matrix = [
    [0, 4, 6],
    [4, 7, 2],
]

result = transpose_matrix(matrix)

for row in result:
    print(row)