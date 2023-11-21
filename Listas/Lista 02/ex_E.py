place = input()

c = int(input())
vip = 0

while c != 0000:
    if c == 1000:
        vip += 1
        print("Mais um VIP! Não podemos esquecer de contabilizá-lo.")
    elif c == 1001:
        print("Ingresso Normal. Não iremos contabilizá-lo.")
    elif c == 1002:
        print("Ele ficará na frente do show, porém não é VIP! Não será contabilizado também.")
    elif c == 1003:
        print("Espera, quem é esse? Ele não pagou! Não devemos sequer analisar sua entrada.")
    elif c == 1004:
        print("Esse código não existe! O sistema quebrou...\nVamos aguardar até que o suporte nos ajude.")
        while c != "Ajudou":
            c = input()
            if c != "Ajudou":
                print("Ainda não...")
        break
    c = int(input())
print(f"O show da Taylor Swift será em {place} e contará com {vip} VIPs!")
