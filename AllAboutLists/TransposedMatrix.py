matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
        ]

for row in matrix:
    print(row,'\n')

"""Transposed matrix is where u replace a ith row and jth coulumn value with jth row and ith coulmn"""
#transposed = []

"""for i in range(4):
    for j in range(3):
        transposed.append(0)"""

transposed = [[0 for i in range(3)] for j in range(4)]
"""for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        transposed[j][i] = matrix[i][j]

for row in transposed:
    print(row, '\n')"""

#transposed[:] = []

for row in transposed:
    print(row, '\n')