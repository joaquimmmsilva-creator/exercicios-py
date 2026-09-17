media = input("Digite a média do aluno: ")


if float(media) >= 6:
    print("Aprovado")   
elif float(media) < 6 and float(media) >= 4:
    print("Recuperação")
else:
    print("Reprovado")