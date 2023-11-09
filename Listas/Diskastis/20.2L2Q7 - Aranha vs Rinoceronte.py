rodadas = int(input(""))

pontosAranha = 0
pontosRino = 0 
aranhaPodeAtacar = False
rinoPodeAtacar = False

for c in range(0, rodadas):

    acaoAranha = input("")
    acaoRino = input("")

    if acaoAranha == "É apenas uma grande massa de musculos":
        aranhaPodeAtacar = True
        
    if acaoRino == "Agora voce vai ver!":
        rinoPodeAtacar = True

    if acaoAranha == "Vai teia!":
        if acaoRino != "Meus musculos sao macicos!" and aranhaPodeAtacar:
            pontosAranha += 1
            print("Maldito inseto!")
        aranhaPodeAtacar = False

    if acaoRino == "Toma essa":
        if acaoAranha != "Camada de teias" and rinoPodeAtacar:
            pontosRino += 1
            print("Droga, me descuidei")
        rinoPodeAtacar = False

if pontosAranha > pontosRino:
    print("Perdeu grandao!")

elif pontosRino > pontosAranha:
    print("Aiai apenas mais um dia comum")
else:
    print("Isso nao esta dando certo")
