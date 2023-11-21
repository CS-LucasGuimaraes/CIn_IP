resp1 = input("")
resp2 = input("")
resp3 = input("")

flag = 0

pergunta = input("")
resposta = input("")

if resposta != resp1:
    print("A resposta está e…e…rrada hahahahaha. Essa é a parte que eu mais gosto, venha aqui no quintal, você pode dar um adeus!")
    flag = 1
else:
    print("Muito bem! Olha como a primeira foi fácil, seu amigo talvez sobreviva. Falta só mais duas para acabar com isso!")


if flag != 1:
    pergunta = input("")
    resposta = input("")
    if resposta != resp2:
        print("A resposta está e…e…rrada hahahahaha. Essa é a parte que eu mais gosto, venha aqui no quintal, você pode dar um adeus!")
        flag = 1
        
    else:
        print("A resposta está e…exata! Você é mais inteligente do que eu pensei, já posso caprichar nesta última, vamos ver se você realmente conhece filmes de terror!")
    if flag != 1:
        pergunta = input("")
        resposta = input("")    

        if resposta != resp3:
            print("A resposta está e…e…rrada hahahahaha. Essa é a parte que eu mais gosto, venha aqui no quintal, você pode dar um adeus!")
        else:
            print("Droga, não vai ser hoje que vou ver sangue, que pena! Mas não se esqueça de mim, quem sabe um dia algum dos seus amigos não queiram brincar para lhe salvar!")
