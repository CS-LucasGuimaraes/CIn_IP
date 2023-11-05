nomeVitima = input("")
nomeVilao = input("")
armadilha = input("")
tempo = int(input(""))

if nomeVilao == "John Kramer":
    if armadilha == "Armadilha de urso reversa":
        if tempo >= 5*60:
            print(f"Com tempo de sobra, {nomeVitima} consegue retirar a armadilha de sua cabeça, sobrevivendo com sucesso ao jogo de Jigsaw.")
        elif 2.5*60 <= tempo < 5*50:
            print(f"À beira de perder a cabeça, e desafiando as expectativas de seu algoz, {nomeVitima} remove a armadilha de urso e por pouco escapa de um destino cruel.")
        else:
            print("Game Over...")

    elif armadilha == "Tanque de agua":
        if tempo >= 4*60:
            print(f"{nomeVitima} usa suas práticas de respiração na natação a seu favor, vencendo o jogo de Jigsaw sem perder muito fôlego.")
        elif 2*60 <= tempo < 4*60:
            print(f"{nomeVitima} passa por maus bocados, mas vira o jogo e consegue evitar, no limite, seu afogamento dentro da armadilha.")
        else:
            print("Game Over...")
elif nomeVilao == "Amanda Young":
    if armadilha == "Caixa de laminas":
        if tempo >= 10*60:
            print(f"Apenas com ferimentos leves, {nomeVitima} se liberta rapidamente das perigosas lâminas da armadilha montada pela discípula de Jigsaw.")
        elif 6*60 <= tempo < 10*60:
            print(f"Por um triz, {nomeVitima} sobrevive ao jogo de Amanda, mas com lesões profundas em suas mãos e braços.")
        else:
            print("Game Over...")

    elif armadilha == "Asas de anjo":
        if tempo >= 3*60:
            print(f"Com surpreendente facilidade, {nomeVitima} alcança a chave da armadilha e vence o desafio da aprendiz de Jigsaw.")
        elif 1.5*60 <= tempo < 3*60:
            print(f"{nomeVitima} desafia as possibilidades e o cruel anseio de sua algoz, escapando da armadilha com poucas queimaduras e arranhões.")
        else:
            print("Game Over...")
            