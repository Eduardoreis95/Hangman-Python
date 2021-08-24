palavra_secreta = ["P","R","O","G","R","A","M","A","C","A","O"]
letras_descobertas = []

print("\n********** JOGO DA FORCA **********")

for i in range(0, len(palavra_secreta)):
    letras_descobertas.append("-")

acertou = False

while acertou == False:
    letra = str(input("Digite a letra: "))

    for i in range(0, len(palavra_secreta)):
        if letra == palavra_secreta[i]:
            letras_descobertas[i] = letra
        print(letras_descobertas[i])

    acertou = True

    for x in range(0, len(letras_descobertas)):
        if letras_descobertas[x] == "-":
            acertou = False
