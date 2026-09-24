numerospositivos = 0

numero = 1 


while numero != 0:
    numero = int(input("Digite o numero que deseja: "))

    if numero > 0:
        numerospositivos += 1
    

print("A quantidade de numeros positivos digitados foi: ", numerospositivos)    



