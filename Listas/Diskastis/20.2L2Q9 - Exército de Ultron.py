num = int(input(""))

for c in range(0, num):
    mensagem = input("")
    for i in range(0, int((len(mensagem))/2)):
        print(f"{chr(int(mensagem[i]+mensagem[-(1+i)]))}",end="")
    print("")
