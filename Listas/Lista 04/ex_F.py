board = [
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-', '-']
        ]

px = py = cx = cy = ax = ay = bx = by = 0

def initBoard(): #void
    px = int(input()); py = int(input()); board[px][py] = 'P'
    cx = int(input()); cy = int(input()); board[cx][cy] = 'C'
    ax = int(input()); ay = int(input()); board[ax][ay] = 'A'
    bx = int(input()); by = int(input()); board[bx][by] = 'B'

def printBoard(): #void
    for i in range(8):
        for j in range(7):
            print(board[i][j], end = ' ')
        print(board[i][7])
    print()

def moveC(): #void
    if (cy > py): cy -= 1
    elif (cy < py): cy += 1
    elif (cx > px): cx -= 1
    elif (cx < px): cx += 1

def moveP(move): #void    
    if move == "cima": px -= 1
    elif move == "baixo": px += 1
    elif move == "esquerda": py -= 1
    elif move == "direita": py += 1 

def waterC():
    if (cx == ax) and (cy == ay):
        void = input() #discarted percy's move
        return True 
    return False

def waterP():
    if (px == ax) and (py == ay):
        return True
    return False

def control():
    flag = False

    while(1):
        moveC()
        if waterC():
            return 'P'
        pMove = input()
        moveP(pMove)
        if waterP():
            moveP(pMove)
            print("Sinto o poder de Poseidon em minhas veias!")
        else:
            if flag:
                print("Agora eu só preciso meter o pé daqui!")
            else:
                print("Preciso pegar aquela maldita bandeira vermelha.")


def main():

    initBoard()


    return 1

main()
