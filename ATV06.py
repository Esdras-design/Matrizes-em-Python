matriz_3x3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
diagonal_secundaria = [matriz_3x3[i][2 - i] for i in range(3)]
print(diagonal_secundaria)  # Saída: [3, 5, 7]
   