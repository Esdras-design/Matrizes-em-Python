matriz_4x4 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
numero_procurado = 1

# Verificar se o número existe na matriz
existe = any(numero_procurado in linha for linha in matriz_4x4)

print("O número", numero_procurado, "existe na matriz?" , existe)  # Saída: True
