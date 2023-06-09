def make_matrix(n):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(n):
            matrix[i].append(int(i == j))

    return matrix


list_ = [1, 2, 4, 3, 6]
matrix_list = list(map(make_matrix, list_))
print(matrix_list)
