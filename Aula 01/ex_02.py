a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))

if a > b:
    aux = a
    a = b
    b = aux

print(a)
print(b)