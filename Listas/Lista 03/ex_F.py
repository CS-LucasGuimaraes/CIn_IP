row = input()
row_n = 0

flag = False

while row != "Fim do labirinto":
    row = row.split(" ")
    for i in range(len(row)):
        elemento = row[i]
        if elemento == "1" and flag == False:
            print("Relíquias encontradas nos seguintes locais:")
            print(f"linha: {row_n}, coluna: {i}")
            flag = True
        elif elemento == "1":
            print(f"linha: {row_n}, coluna: {i}")
    row_n += 1
    row = input()

if flag == False:
    print("Nenhuma relíquia encontrada no labirinto.")
