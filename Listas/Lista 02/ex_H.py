len = int(input())

kw = False
gp = False
cm = False
ts = False
kp = False
ag = False
b = False
s = False


for c in range(len):
    cel = input()
    print(f"Apresentador: Contamos com a ilustre presença de {cel}, uma salva de palmas!")
    if cel == "Kanye West":
        kw = True
    elif cel == "Gerard Piqué":
        gp = True
    elif cel == "Chris Martin":
        cm = True 

cand = input() 
while cand != "Início da Premiação":
    if cand == "Taylor Swift":
        ts = True
    elif cand == "Katy Perry":
        kp = True
    elif cand == "Ariana Grande":
        ag = True
    elif cand == "Beyoncé":
        b = True
    elif cand == "Shakira":
        s = True
    cand = input()

print("Apresentador: Vamos deixar de enrolação e ir para a premiação!")
print("Apresentador: E a artista do ano do MTV Video Music Awards 2023 é...")

if ts:
    print("Taylor Swift".upper())
    if kw:
        print("Kanye West: Eu vou te deixar terminar. Estou feliz por você, mas Beyoncé fez um dos melhores vídeos de todos os tempos.")
elif kp:
    print("Katy Perry".upper())
elif ag:
    print("Ariana Grande".upper())
elif b:
    print("Beyoncé".upper())
    if cm:
        print("Chris Martin: Minha heroína, minha irmã, meu tudo. Você merece!")
elif s:
    print("Shakira".upper())
    if gp:
        print("Gerard Piqué: Meu amor me perdoa, volta pra mim...")

