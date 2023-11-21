len = int(input())

sus = 0
camb = 0

for c in range(len):
    nomeC = input()
    cpfC = input()
    nomeId = input()
    cpfId = input()
    qtd = int(input())
    prc = float(input())
    cdg = input()

    if nomeC != nomeId:
        sus += 1
    if  cpfC != cpfId:
        sus += 1
    if  qtd > 12:
        sus += 1
    if prc > 1500:
        sus += 1
        
    impar = 0
    for k in cdg:
        if int(k) % 2 == 1:
            impar += 1
    if impar >= 7:
        sus += 1

    if sus >= 3:
        camb += 1
    sus = 0

print(f"Total de compradores analisados: {len}")
print(f"Total de suspeitas de cambistas: {camb}")
