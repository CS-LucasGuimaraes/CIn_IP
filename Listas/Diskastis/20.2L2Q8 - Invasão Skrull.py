meta = int(input(""))
infiltrados = int(input(""))
numAcontecimentos = int(input(""))

alerta = 0

for c in range(0, numAcontecimentos):
    acontecimento = input("")

    if acontecimento == "Substituicao":
        infiltrados += int(input(""))
    elif acontecimento == "Contra-ataque":
        infiltrados -= int(input(""))
    elif acontecimento == "Exposicao":
        alerta += 30

    if infiltrados <= 0 or alerta >= 100 or infiltrados >= meta:
        break

if infiltrados <= 0:
    print("Falhamos completamente, não há mais nenhum Skrull infiltrado")
elif alerta >= 100:
    print("Não vale a pena continuar, vamos recuar e bolar um novo plano")
elif infiltrados >= meta:
    print("Ordenar ataque imediatamente, dessa vez dominaremos a Terra")
elif infiltrados < meta:
    print("Ainda não estamos preparados para atacar, vamos esperar mais um pouco")