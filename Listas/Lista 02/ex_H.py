len = int(input())

kanye_west = False
gerard_pique = False
chris_martin = False
taylor_switft = False
Katy_Perry = False
Arina_grande = False
Beyonce = False
Shakira = False

for c in range(len):
    celebridade = input()
    print(f"Apresentador: Contamos com a ilustre presença de {celebridade}, uma salva de palmas!")
    if celebridade == "Kanye West":
        kanye_west = True
    elif celebridade == "Gerard Piqué":
        gerard_pique = True
    elif celebridade == "Chris Martin":
        chris_martin = True 

cand = input() 
while cand != "Início da Premiação":
    if cand == "Taylor Swift":
        taylor_switft = True
    elif cand == "Katy Perry":
        Katy_Perry = True
    elif cand == "Ariana Grande":
        Arina_grande = True
    elif cand == "Beyoncé":
        Beyonce = True
    elif cand == "Shakira":
        Shakira = True
    cand = input()

print("Apresentador: Vamos deixar de enrolação e ir para a premiação!")
print("Apresentador: E a artista do ano do MTV Video Music Awards 2023 é...")

if taylor_switft:
    print("Taylor Swift".upper())
    if kanye_west:
        print("Kanye West: Eu vou te deixar terminar. Estou feliz por você, mas Beyoncé fez um dos melhores vídeos de todos os tempos.")
elif Katy_Perry:
    print("Katy Perry".upper())
elif Arina_grande:
    print("Ariana Grande".upper())
elif Beyonce:
    print("Beyoncé".upper())
    if chris_martin:
        print("Chris Martin: Minha heroína, minha irmã, meu tudo. Você merece!")
elif Shakira:
    print("Shakira".upper())
    if gerard_pique:
        print("Gerard Piqué: Meu amor me perdoa, volta pra mim...")

