def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        strings = []
        matrix.append(strings)
        for j in range(m):
            strings.append(value)
    return matrix

result = get_matrix(3, 3, 12)
print(result)