localTeste = input("")
deslocamento = 0

if localTeste == "Salão":
    print("Em direção ao salão!")
    deslocamento = 2
elif localTeste == "Praça":
    print("Para a praça eu vou!")
    deslocamento = 2
elif localTeste == "Centro da cidade":
    print("Faz tempo que não visito o centro, mal posso esperar!")
    deslocamento = 1

horaTeste = int(input(""))

print(f"Pra chegar na hora, vou ter que sair de {horaTeste - deslocamento} horas.")

respostaMae = input("")

if respostaMae == "Sim, Pearl! Siga seus sonhos!":
    print("Obrigada mãe! Eu vou ser uma estrela e o mundo todo saberá meu nome!")
else:
    print("Você não vai me deixar aqui! EU NÃO VOU FICAR NESSA FAZENDA!")
