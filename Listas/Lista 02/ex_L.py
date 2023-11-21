nome = input()

while nome != "vou dormir":
    pp = input()
    pt = input()

    impossible = False
    for char in pt:
        if impossible == False:
            if char in pp:
                pp = pp.replace(char, "", 1)
            else:
                impossible = True
    if impossible:
        print("perdeu covarde!")
    else:
        print(f"você acertou, estreou na lista! {nome}")

    nome = input()
