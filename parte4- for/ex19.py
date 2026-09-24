numero = int(input("Digite um número: "))

fatorial = 1

if numero < 0:
    print("Não existe fatorial de número negativo")
else:
    for i in range(numero, 0, -1):
        fatorial = fatorial * i

    print("O fatorial de", numero, "é:", fatorial)
