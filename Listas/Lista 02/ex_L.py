nome = input()

while nome != "vou dormir":
    palavra_pretendente = input()
    palavra_taylor = input()

    impossible = False
    for char in palavra_taylor:
        if impossible == False:
            if char in palavra_pretendente:
                palavra_pretendente = palavra_pretendente.replace(char, "", 1)
            else:
                impossible = True
    if impossible:
        print("perdeu covarde!")
    else:
        print(f"você acertou, estreou na lista! {nome}")

    nome = input()
