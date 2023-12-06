valid = ["Foice de Hades", "Talismã de Ícaro", "Elmo da Invisibilidade", "Cinto de Hermes", "Espada Anaklusmos", "Escudo Aegis", "Adaga Katoptris"]

list = input().split("-")

while (list != ["Parar"]):
    
    
    cpy = valid.copy();
    for c in list:
        if c in cpy: cpy.remove(c)
    
    if len(cpy) == 0:
        print(f"{list[0]} irá batalhar na base do murro!")
        list = input().split("-")
        continue

    if len(cpy) == 1: 
        print(f"{list[0]} irá rumo a batalha com o equipamento: {cpy[0]}!")
        list = input().split("-")
        continue
    
    print(f"{list[0]} irá rumo a batalha com os seguintes equipamentos: ", end="")
    
    for c in range(len(cpy)-2): 
        print(cpy[c], end=", ")
    
    print(f"{cpy[-2]} e {cpy[-1]}!");

    list = input().split("-")
