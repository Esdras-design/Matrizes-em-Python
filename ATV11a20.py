import numpy as np

matriz_3x3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
transposta = matriz_3x3.T
print("Matriz 3x3:\n", matriz_3x3)
print("Transposta:\n", transposta)
   
#--------------------------------------------------------------------12

matriz_4x4_zeros = np.zeros((4, 4))
print("Matriz 4x4 de zeros:\n", matriz_4x4_zeros)

#--------------------------------------------------------------------13

matriz_4x4_uns = np.ones((4, 4))
print("Matriz 4x4 de uns:\n", matriz_4x4_uns)

#--------------------------------------------------------------------14

matriz_3x3_aleatoria = np.random.randint(1, 51, size=(3, 3))
print("Matriz 3x3 com valores aleatórios entre 1 e 50:\n", matriz_3x3_aleatoria)

#--------------------------------------------------------------------15

matriz_a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matriz_b = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
soma = matriz_a + matriz_b
print("Soma das matrizes:\n", soma)

#--------------------------------------------------------------------16

matriz_3x3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
numero_fixo = 2
matriz_multiplicada = matriz_3x3 * numero_fixo
print("Matriz multiplicada por", numero_fixo, ":\n", matriz_multiplicada)

#--------------------------------------------------------------------17


matriz_3x3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matriz_dividida = matriz_3x3 / 2
print(matriz_dividida)

#--------------------------------------------------------------------18

matriz_3x3_determinante = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]])
determinante = np.linalg.det(matriz_3x3_determinante)
print(determinante)

#--------------------------------------------------------------------19

matriz_4x4_colunas = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
soma_colunas = np.sum(matriz_4x4_colunas, axis=0)
print(soma_colunas)

#-------------------------------------------------------------------20

matriz_4x4_linhas = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
soma_linhas = np.sum(matriz_4x4_linhas, axis=1)
print(soma_linhas)