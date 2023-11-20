pont = 0
music = 0
while pont >= 0:
    string = input("")
    if string == "os fãs estão formando uma ciranda":
        pont -= 3
    elif string == "os fãs estão ligando os flashes e atrapalhando a visão" or string == "os fãs estão dançando na frente da tela" or string == "os fãs estão gritando o nome da Taylor e atrapalhando a música":
        pont -= 2
    elif string == "os fãs estão cantando as músicas em coro" or string == "houve um pedido de casamento na sessão":
        pont += 2
    elif string == "long live":
        print(f"A Taylor conseguiu concluir o show sem muitas interrupções e cantou {music+1} músicas.")
        break
    else:
        pont += 1
        music += 1
if pont < 0:
    print(f"A Taylor só conseguiu cantar {music} músicas e a sessão foi interrompida.")
