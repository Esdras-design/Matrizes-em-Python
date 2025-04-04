matriz_3x3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


maior_elemento = max(max(linha) for linha in matriz_3x3)
menor_elemento = min(min(linha) for linha in matriz_3x3)

print("Maior elemento:", maior_elemento) # Saída: 9
print("Menor elemento:", menor_elemento) # Saída: 1 
