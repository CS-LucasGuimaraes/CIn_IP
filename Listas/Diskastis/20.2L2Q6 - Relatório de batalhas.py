oponentesVivos = int()

numeroOponentes = int(input(""))
media = int(input(""))

for i in range(0, numeroOponentes):

    nomeOponente = input("")
    vidaOponente = int(input(""))
    numAtaques = int(input(""))

    if vidaOponente < media / 2:
        nomePlaneta = "Asgard"
    elif vidaOponente <= media * (8/10):
        nomePlaneta = "Xandar"
    elif vidaOponente < media * (12/10):
        nomePlaneta= "Sakaar"
    elif vidaOponente <= media * (15/10):
        nomePlaneta = "Vormir"
    else:
        nomePlaneta = "Ego"

    danoTotal = 0

    for c in range(0, numAtaques):
        dano = int(input(""))
        danoTotal += dano 

    if danoTotal >= vidaOponente:
        print(f"{nomeOponente} do planeta {nomePlaneta} foi derrotado!")

    else:
        print(f"{nomeOponente}, do planeta {nomePlaneta}, conseguiu escapar.")
        oponentesVivos += 1

if oponentesVivos == 0:
    print("Conseguimos deixar a galaxia segura.")
else:
    print("Alguns oponentes ainda estao a espreita...")
