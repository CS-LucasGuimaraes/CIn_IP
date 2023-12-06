columna = 0

linea = input()
numero_linea = 0

flag = False

while linea != "Fim do labirinto":
    linea = linea.split(" ")
    numero_linea += 1
    for i in range(len(linea)):
        elemento = linea[i]
        if elemento == "1" and flag:
            print("Relíquias encontradas nos seguintes locais:")
            print(f"linha: {numero_linea}, coluna: {i} ")
            flag = True
        elif elemento == "1":
            print(f"linha: {numero_linea}, coluna: {i} ")
    linea = input()

if flag == False:
    print("Nenhuma relíquia encontrada no labirinto.")