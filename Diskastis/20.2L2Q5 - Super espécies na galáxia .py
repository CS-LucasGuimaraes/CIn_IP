nomeEspecie = input("")

count = int()

especie1 = str()

while 1:

    especie1 = input("")
    if especie1 == "fim":
        break
    especie2 = input("")
    caracteristica1 = input("")
    caracteristica2 = input("")
    probabilidade1 = int(input(""))
    probabilidade2 = int(input(""))
    potencial1 = int(input(""))
    potencial2 = int(input(""))

    teste_especie1 = (probabilidade1 - potencial1)**2
    teste_especie2 = (probabilidade2 - potencial2)**2

    if teste_especie1 > teste_especie2:
        print(f"O bebê ET gerado é da espécie {especie1} e tem como característica {caracteristica1}")
        if especie1 == nomeEspecie:
            count += 1
    else:
        print(f"O bebê ET gerado é da espécie {especie2} e tem como característica {caracteristica2}")
        if especie2 == nomeEspecie:
            count += 1

print(f"nasceram {count} bebês ETs da espécie {nomeEspecie}")
