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
    print("ERRADA", end=" ")

# INPUTS PORTA 2

dir_2 = input("")
cor_2 = input("")
pla_2 = input("")
mac_2 = input("")

# MECANISMO PORTA 2

if cor_2 == "dourada" or cor_2 == "prateada" or (pla_2 == "avenca" and mac_2 == "redonda") or (pla_2 == "espadinha" and mac_2 == "redonda"):
    pontos += 200
    print("CERTA", end=" ")
else:
    print("ERRADA", end=" ")

# INPUTS PORTA 3

dir_3 = input("")
cor_3 = input("")
num_3 = int(input(""))
pla_3 = input("")
mac_3 = input("")

# MECANISMO PORTA 3

