wheel = input().split(" - ")
index = int(len(wheel)/2)
bag = []

tc = int(input())

for c in range(tc):
    movement = input()
    for k in range(int(movement[0:len(movement)-1])):
        if (movement[-1] == '>'): index += 1;
        elif (movement[-1] == '<'): index -= 1;
        if (index == len(wheel)): index-=len(wheel);
        elif (index == -1): index+=len(wheel);

    action = input()
    if action == "Adicionar":
        if (wheel[index] not in bag): 
            bag.append(wheel[index])
            print(f"{wheel[index]} adicionado a mochila!")
        else:
            print(f"{wheel[index]} já está na mochila. Não seja gananciosa, ou acabará como Midas!")
    else:
        if (wheel[index] in bag):
            print(f"{wheel[index]} já está na mochila. Não seja gananciosa, ou acabará como Midas!")
        else:
            print(f"{wheel[index]} não vai ser tão útil assim!")

if (len(bag) == 0): print("Não achei nada útil no arsenal. Acho que vamos precisar ser menos violentos dessa vez…")

else:
    print("Com ",end='')
    for o in bag: print(o,end=', ')
    print("seremos imbatíveis na caça à bandeira!")
