def mx(a , b):
    if (a > b): return a
    else: return b

days = int(input())
found = 0
hidden = 0

for d in range(days):
    eggs = int(input())
    hidden += int(eggs)
    horoscope = input()

    if (horoscope == "Os astros estão de bom humor hoje. Acho que você terá um pouco de sorte extra."):
        eggs *= 0.7
    elif (horoscope == "As estrelas estão neutras hoje. O dia está em suas mãos."): 
        eggs = mx(eggs* 0.7, eggs/ ((eggs%(d+1)) + 1))
    elif (horoscope == "Isso é raro. As estrelas estão absolutamente neutras hoje."):
        eggs = (eggs % (d+1)) + 1
    elif (horoscope == "Hoje, Kiq não pôde consultar as estrelas. Sem a orientação astrológica, a busca por ovos fica à mercê do destino."):
        eggs *= 0

    found += int(eggs)

    print(f"Dia {d+1}");
    print(f"Hoje Carlos encontrou {int(eggs)} ovos!!")
    
print(f"Kiq encontrou {int(found)} de um total de {int(hidden)}")

if (found == hidden):
    print("Incrível! Seu signo está em alta. Você encontrou todos os ovos!")
elif (found/hidden > (66/100)):
    print("Ótimo trabalho! Os astros estão ao seu lado. Você encontrou a maioria dos ovos!")
elif (found/hidden > (33/100)):
    print("Bom esforço! Os astros sorriem para você. Muitos ovos foram encontrados.")
elif (found/hidden > 0):
    print("Continue procurando! Seu horóscopo sugere que há mais ovos a serem encontrados.")
else:
    print("Ainda não encontrou nenhum ovo. O horóscopo aconselha persistência. Continue tentando!")
