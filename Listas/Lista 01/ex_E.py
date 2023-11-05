resp1 = input("")
resp2 = input("")
resp3 = input("")

cont = 0

while cont < 3:
    cont += 1

    pergunta = input("")
    resposta = input("")

    if cont == 1:
        if resposta != resp1:
            print("A resposta está e…e…rrada hahahahaha. Essa é a parte que eu mais gosto, venha aqui no quintal, você pode dar um adeus!")
            break
        else:
            print("Muito bem! Olha como a primeira foi fácil, seu amigo talvez sobreviva. Falta só mais duas para acabar com isso!")
    if cont == 2:
        if resposta != resp2:
            print("A resposta está e…e…rrada hahahahaha. Essa é a parte que eu mais gosto, venha aqui no quintal, você pode dar um adeus!")
            break
        else:
            print("A resposta está e…exata! Você é mais inteligente do que eu pensei, já posso caprichar nesta última, vamos ver se você realmente conhece filmes de terror!")
    if cont == 3:
        if resposta != resp3:
            print("A resposta está e…e…rrada hahahahaha. Essa é a parte que eu mais gosto, venha aqui no quintal, você pode dar um adeus!")
            break
        else:
            print("Droga, não vai ser hoje que vou ver sangue, que pena! Mas não se esqueça de mim, quem sabe um dia algum dos seus amigos não queiram brincar para lhe salvar!")
    