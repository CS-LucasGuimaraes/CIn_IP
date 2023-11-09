pontos = 0
print("ARISU, VOCÊ FEZ SUAS ESCOLHAS E AGORA VEREMOS SE ESCOLHEU AS PORTAS CERTAS:")

# INPUTS PORTA 1

dir_1 = input("")
num_1 = int(input(""))

# MECANISMO PORTA 1

if (num_1%2 == 1 and dir_1 == "direita") or (num_1%2 == 0 and dir_1 == "esquerda"):
    pontos += 150
    print("CERTA", end=" ")
else:
    pontos -= 150
    print("ERRADA", end=" ")

# INPUTS PORTA 2

dir_2 = input("")
cor_2 = input("")
pla_2 = input("")
mac_2 = input("")

# MECANISMO PORTA 2

if (dir_2 == "direita" and (cor_2 == "dourada" or cor_2 == "prateada" or (pla_2 == "avenca" and mac_2 == "redonda") or (pla_2 == "espadinha" and mac_2 == "redonda"))) or (dir_2 == "esquerda" and (cor_2 == "dourada" or cor_2 == "prateada" or (pla_2 == "avenca" and mac_2 == "redonda") or (pla_2 == "espadinha" and mac_2 == "redonda"))):
    pontos += 200
    print("CERTA", end=" ")
else:
    pontos -= 200
    print("ERRADA", end=" ")

# INPUTS PORTA 3

dir_3 = input("")
cor_3 = input("")
num_3 = int(input(""))
pla_3 = input("")
mac_3 = input("")

# MECANISMO PORTA 3

if dir_3 == "esquerda" and ( (num_3%5 == 0 and pla_3 == "espadinha" and mac_3 == "quadrada") or (cor_3 == "perolada") ):
    pontos += 250
    print("CERTA", end=" ")

elif dir_3 == "direita" and ( (num_3%5 != 0 or pla_3 != "espadinha" or mac_3 != "quadrada") and (cor_3 != "perolada") ):
    pontos += 250
    print("CERTA", end=" ")

else:
    pontos -= 250
    print("ERRADA", end=" ")

# INPUTS PORTA 4

dir_4 = input("")
num_4 = int(input(""))

# MECANISMO PORTA 4

if (dir_4 == "direita" and (num_4 % 3 == 0 and num_4 % 2 != 0 and num_4 % 5 != 0) or (dir_4 == "esquerda" and not (num_4 % 3 == 0 and num_4 % 2 != 0 and num_4 % 5 != 0))):
    pontos += 300
    print("CERTA", end=" ")
else:
    pontos -= 300
    print("ERRADA", end=" ")

# INPUTS PORTA 5

cor_5 = input("")
num_5 = int(input(""))
pla_5 = input("")
flo_5 = input("")
mac_5 = input("")

# MECANISMO PORTA 5

if cor_5 == "acobreada" and (num_5 % 2 == 1 or (mac_5 == "triangular" or mac_5 == "quadrada")):
    pontos += 500
    print("CERTA")

elif cor_5 == "prateada" and (flo_5 != ("margarida") and flo_5 != "papoula" and flo_5 != "cosmos") and (mac_5 == "hexagonal" or mac_5 == "redonda"):
    pontos += 450
    print("CERTA")

elif cor_5 == "dourada" and (flo_5 == "lirio" or flo_5 == "ixora") and mac_5 == "hexagonal":
    pontos += 400
    print("CERTA")

else:
    pontos -= 500
    print("ERRADA")

if pontos >= 1300:
    print(f"Parece que a sorte está ao seu favor, Arisu... Você conseguiu passar com {pontos} pontos!")

elif pontos > 0:
    print(f"Você passou com {pontos} pontos, mas faça melhores escolhas da próxima vez.")

elif pontos == -1400:
    print(f"Todas suas escolhas foram erradas, Arisu, esperávamos mais de você... Você será executado pois obteve {pontos} pontos.")

else:
    print(f"Por mais que você tenha feito escolhas corretas, não foi suficiente para sobreviver. Você finalizou o jogo com {pontos} pontos")
