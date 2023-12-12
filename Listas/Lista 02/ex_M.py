comp = int(input())
dinh = int(input())
temp_min = int(input())*60

melhorpos = 1000000000000
cont_ing = 0
comput = 0

cont = 0

for c in range(comp):
    nome = input()
    if nome == "end":
        break
    if nome != "laura" and nome != "carlos" and nome != "roberto":
        cont += 1

if cont == 0:
    print("Ah não! João não conseguiu nenhum amigo que o ajudasse. Agora ele vai ter que contar com a sorte para pegar um bom lugar na fila, usando apenas seu computador.")

else:
    print(f"Bom começo! Consegui {cont} amigos que podem me ajudar a comprar o ingresso")

    for c in range(cont):
        

        loc = ''
        while loc != "end":
            val = int(input())
            loc = input()

            if loc == "rio de janeiro" or loc == "são paulo" or loc == "buenos aires": 
                print("Consegui um ingresso em um local que João possa ir! Agora temos que ver o preço")
                if val <= dinh:
                    print("Consegui o dinheiro! Agora só falta ver a minha colocação na fila dos ingressos...")
                    pos = int(input())
                    if pos / 16 * 10 <= temp_min:
                        print("ISSOOO, conseguimos um ingresso!!!")
                        cont_ing += 1
                        if melhorpos > pos:
                            melhorpos = pos
                            comput = c+1
                    else:
                        print(f"Caramba, essa foi quase! Mas infelizmente não consegui um bom lugar na fila dos ingressos no computador de número {c+1}")
                else:
                    print("Caramba! Só tinha ingresso para a pista vip, que está bem acima do meu orçamento.")
                break

    if cont_ing != 0:
        print(f"Consegui o ingresso! Com {int((cont_ing/cont)*100)}% de aproveitamento da ajuda dos meus amigos. E a fila escolhida para comprar o ingresso foi do computador número {comput}. Rumo ao show da Taylor!!!")

    elif cont > comp/2:
        print("Não acredito que tive amigos para ocuparem mais da metade dos computadores, e ainda assim não consegui um ingresso...")

    else:
        print("Poxa, não acredito que não consegui o ingresso, acho que eu devia ter chamado mais amigos para ajudar.")
