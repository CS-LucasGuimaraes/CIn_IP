a = int(input("Digite o menor valor: "))
b = int(input("Digite o maior valor: "))

range_ab = b-a

for c in range(0, range_ab):
    b += (a+c)

print(b)