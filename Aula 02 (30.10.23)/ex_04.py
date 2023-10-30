a = int(input("Digite o menor valor: "))
b = int(input("Digite o maior valor: "))

range_ab = b-a
resultado = 0

for c in range(0, range_ab+1):
    resultado += (a+c)

print(resultado)
