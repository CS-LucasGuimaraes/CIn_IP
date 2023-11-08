n1 = float(input(""))

if n1 >= 0:
    n2 = float(input(""))
    if n2 >= 0:
        n3 = float(input(""))
        if n3 >= 0:
            palavra = input("")
            if palavra.lower() == palavra:
                n5 = float(input(""))
            else:
                print(f"{palavra} não está gravado(a) na caixa, não adianta nem continuar que ela não vai abrir.")
                exit()
        else:
            print(f"{n3:.2f} não está gravado(a) na caixa, não adianta nem continuar que ela não vai abrir.")
            exit()
    else:
        print(f"{n2:.2f} não está gravado(a) na caixa, não adianta nem continuar que ela não vai abrir.")
        exit()
else:
    print(f"{n1:.2f} não está gravado(a) na caixa, não adianta nem continuar que ela não vai abrir.")
    exit()

if n1 % 2 == 0:
    n1 = n1 * 2
else:
    n1 = n1 * 0.5

if n2 % 2 == 0:
    n2 = n2 * 2
else:
    n2 = n2 * 0.5

if n3 % 2 == 0:
    n3 = n3 * 2
else:
    n3 = n3 * 0.5

numFinal = (n1*n2*n3*n5)**(0.5)

if numFinal >= 10:
    print(f"O número {numFinal:.2f} e a palavra {palavra} eram as respostas. A caixa foi aberta.")
else:
    print(f"A combinação era muito pequena, a caixa só vai poder ser aberta daqui a {(10 - numFinal):.2f} anos.")
