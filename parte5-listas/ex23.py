numeros = [2, 4, 6, 8, 10]

maior = numeros[0]

for numero in numeros:
    if numero > maior:
        maior = numero

print("o maior valor da lista é:", maior)
