"""
GLOBAL VARIABLES
"""

remaining_requiriments = []
board = []
r = c = 0

# -------------- #

def read_board():
    global r, c, board

    row = input()
    while(row != "finalizar"): 
        row = [c for c in row]
        
        board.append(row)

        row = input()
    
    r = len(board); c = len(board[0])

    return board


def print_board():
    global r, c, board

    for i in range(r):
        for j in range(c):
            print(board[i][j], end='')
        print()

    return 1


def read_itens(required_equipments):
    item = input()
    while (item != "finalizar programa"):
        item = item.split('-')

        name = item[0]
        size = item[1].split('x')
        x = int(size[1])
        y = int(size[0])
        category = item[2]

        check_inventory(name, category, x, y)

        item = input()

    return 1


def check_inventory(name, category, x, y):
    global board, remaining_requiriments

    if category not in remaining_requiriments:
        print(f"Não precisamos de {name}")
        return 0 

    for i in range(r):
        for j in range(c):
            if board[i][j] == 'O':
                if check_pos(i, j, x,y):
                    remaining_requiriments.remove(category)
                    print(f"Item adicionado: {name}")
                    fill_pos(i,j, x,y,  category)
                    return 1

    print(f"Não há espaço para {name}")        
    return 0


def check_pos(i,j, x,y):
    global r, c

    if (i + x > r or j + y > c): return 0
    
    for k in range(x):
        for l in range(y):
            if board[i+k][j+l] != 'O':
                return 0
    return 1


def fill_pos(i,j, x,y, category):
    category = category.split(' ')
    char = category[-1][0].upper()
    
    for k in range(x):
        for l in range(y):
            board[i+k][j+l] = char

    return 1


def main():
    global remaining_requiriments

    board = read_board()

    required_equipments = input().split(", ")
    remaining_requiriments = required_equipments.copy()

    read_itens(required_equipments)

    print_board()

    if len(remaining_requiriments) != 0:
        print(f"Faltou: {', '.join(remaining_requiriments)}") 

    return 1

main()  # Start the program eitemecution
