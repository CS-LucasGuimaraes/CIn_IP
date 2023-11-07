numero = int(input(""))

local1 = input("")
local2 = input("")
local3 = input("")

maior = str()
menor = str()
sucesso = False
   
if numero == 1:
        
    if len(local1) > len(local2) and len(local1) > len(local3):
        print(local1)
        sucesso = True

    elif len(local2) > len(local1) and len(local2) > len(local3):
        print(local2)
        sucesso = True
    
    elif len(local3) > len(local1) and len(local3) > len(local2):
        print(local3)
        sucesso = True

    else:
        print("(Droga! Ainda não consegui descobrir o local que possui mais sinais desconhecidos! Vou ter que ficar mais um tempo nessa Mansão Mal-Assombrada...)")
        if local1 > local2 > local3 or local1 > local3 > local2:
            print(local1)  
            sucesso = True

        elif local2 > local1 > local3 or local2 > local3 > local1:
            print(local2)
            sucesso = True

        elif local3 > local1 > local2 or local3 > local2 > local1:
            print(local3)
            sucesso = True

        else: 
            print("\"AAAAAA! Um fantasma me assustou!\"\n(Uma mensagem apareceu no monitor que você estava usando. \"Agente, um erro inesperado aconteceu. A EPF contactará você novamente quando tudo estiver funcionando da forma correta. Nosso sistema foi invadido por alguém que se identifica como Hubert P.Enguin\")")

elif numero == 2:
        
    if len(local1) < len(local2) and len(local1) < len(local3):
        print(local1)
        sucesso = True

    elif len(local2) < len(local1) and len(local2) < len(local3):
        print(local2)
        sucesso = True
    
    elif len(local3) < len(local1) and len(local3) < len(local2):
        print(local3)
        sucesso = True

    else:
        print("(Droga! Ainda não consegui descobrir o local que possui mais sinais desconhecidos! Vou ter que ficar mais um tempo nessa Mansão Mal-Assombrada...)")
        if local1 > local2 > local3 or local1 > local3 > local2:
            print(local1)  
            sucesso = True

        elif local2 > local1 > local3 or local2 > local3 > local1:
            print(local2)
            sucesso = True

        elif local3 > local1 > local2 or local3 > local2 > local1:
            print(local3)
            sucesso = True

        else: 
            print("\"AAAAAA! Um fantasma me assustou!\"\n(Uma mensagem apareceu no monitor que você estava usando. \"Agente, um erro inesperado aconteceu. A EPF contactará você novamente quando tudo estiver funcionando da forma correta. Nosso sistema foi invadido por alguém que se identifica como Hubert P.Enguin\")")


if sucesso == True:
    print("(Ao terminar sua tarefa, uma mensagem apareceu no monitor que você estava usando. \"Muito bem agente. A EPF agradece os seus esforços\")")

print("(Depois de ler a mensagem, você dormiu. Ao acordar, você não estava mais no CIn de outubro de 2012, mas no CIn de 2023, sem acreditar na situação que vivenciou)")
