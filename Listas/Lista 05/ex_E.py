def read_board(already_have_categories):
    """
    Reads the board representation from user input until "finalizar" is entered.
    
    Args:
      already_have_categories (list(string)): The categories that are already in the board.
    
    """

    # Represents the board as a 2D list:
    board = []

    row = input()  # Read the first row
    while row != "finalizar":  # Continue reading rows until "finalizar" is entered
        row = [c for c in row]  # Convert the row (string) to a list(char)
        board.append(row)  # Add the row (list) to the board
        pre_check_board(row, already_have_categories)  # Check for existing equipment in the row
        row = input()  # Read the next row

    return board


def pre_check_board(row, already_have_categories):
    """
    Checks if any equipment categories are already present in the given row.
    
    Args:
      row (list(int)): the row that are going to be verified
      already_have_categories (list(string)): The categories that are already in the board.    
    """

    if 'M' in row and "municão" not in already_have_categories: 
        already_have_categories.append("munição")
    
    if 'G' in row and "granada" not in already_have_categories:
        already_have_categories.append("granada")
    
    if 'B' in row and "branca" not in already_have_categories:
        already_have_categories.append("branca")
    
    if 'S' in row and "secundaria" not in already_have_categories:
        already_have_categories.append("secundaria")
    
    if 'P' in row and "primaria" not in already_have_categories:
        already_have_categories.append("primaria")
    
    if 'A' in row and "acessorios" not in already_have_categories:
        already_have_categories.append("acessorios")

def print_board(board, r, c):
    """
    Prints the current state of the board.

    Args:
      board (list2D): matrix of the board.
      r: number of rows of the board.
      c: number of cols of the board.
    """

    for i in range(r):  # Iterate through each row
        for j in range(c):  # Iterate through each element in the row
            print(board[i][j], end='')  # Print the element without a newline
        print()  # Print a newline after each row


def read_itens(board, r, c, remaining_requiriments):
    """
    Reads items from user input until "finalizar programa" is entered.

    Args:
      board (list2D): matrix of the board.
      remaining_requiriments (list(string)): The categories that aren't already in the board. 
    """

    item = input()  # Read the first item
    while item != "finalizar programa":  # Continue reading items until "finalizar programa"
        item = item.split('-')  # Split item information by hyphens

        # Extract item details:
        name = item[0]
        size = item[1].split('x')
        x = int(size[1])  # Item width
        y = int(size[0])  # Item height
        category = item[2]

        check_inventory(name, category, x, y, r, c, board, remaining_requiriments)  # Check if the item can be placed on the board

        item = input()  # Read the next item


def check_inventory(name, category, x, y, r, c, board, remaining_requiriments):
    """
    Checks if an item can be placed on the board and updates inventory accordingly.

    Args:
      name (str): Name of the item
      category (str): Category of the item
      x (int): Width of the item
      y (int): Height of the item
      board (list2D): matrix of the board.
      remaining_requiriments (list(string)): The categories that aren't already in the board. 

    Returns:
      bool: 1 if item added, 0 otherwise
    """

    if category not in remaining_requiriments:
        print(f"Não precisamos de {name}")  # Item not required
        return 0

    if find_empty_space(x,y,0,0,category,name, r, c, board, remaining_requiriments): return 1 

    print(f"Não há espaço para {name}")  # No space for the item
    return 0


def find_empty_space(x,y,i,j,category,name, r, c, board, remaining_requiriments):
    """
    Tries to find an empty space that fits the item somwhere in the inventory.

    Args:
      x (int): Width of the item
      y (int): Height of the item
      i (int): Actual width index
      j (int): Actual height index
      category (str): Category of the item
      name (str): Name of the item
      board (list2D): matrix of the board. 
      remaining_requiriments (list(string)): The categories that aren't already in the board.

    Returns:
      bool: 1 if item fits somewhere, 0 otherwise
    """

    if board[i][j] == 'O':  # Found an empty space
        if check_pos(i, j, x, y, r, c, board):  # Check if the item fits
            remaining_requiriments.remove(category)  # Item added, remove from remaining requirements
            print(f"Item adicionado: {name}")
            board = fill_pos(i, j, x, y, category, board)  # Fill the corresponding positions on the board
            return 1
        
    # Recursive for system
    j += 1
    if j == c: 
        j = 0
        i += 1
        if i == r:
            return 0
    
    return find_empty_space(x,y,i,j,category,name,r,c,board, remaining_requiriments)


def check_pos(i, j, x, y, r, c, board):
    """
    Checks if an item of size x*y can fit on the board starting at position (i, j).

    Args:
      i (int): Starting row index
      j (int): Starting column index
      x (int): Width of the item
      y (int): Height of the item
      board (list2D): matrix of the board. 

    Returns:
      bool: 1 if item fits, 0 otherwise
    """

    if (i + x > r or j + y > c): return 0  # Check if item extends beyond board boundaries

    for k in range(x):
        for l in range(y):
            if board[i + k][j + l] != 'O':  # Check if any position is not empty
                return 0

    return 1  # Item fits


def fill_pos(i, j, x, y, category, board):
    """
    Fills the positions on the board with a character representing the item's category.

    Args:
      i (int): Starting row index
      j (int): Starting column index
      x (int): Width of the item
      y (int): Height of the item
      category (str): Category of the item
      board (list2D): matrix of the board. 
    """

    category = category.split(' ')  # Split category into words
    char = category[-1][0].upper()  # Use the first letter of the last word as the character

    for k in range(x):
        for l in range(y):
            board[i + k][j + l] = char

def remove_already_have_equipments(remaining_requiriments, already_have_categories):
    """
    Removes any equipment categories that are already present on the board from the remaining requirements.

    Args:
    already_have_categories (list(string)): The categories that are already in the board.
    remaining_requiriments (list(string)): The categories that aren't already in the board.
    """

    for c in already_have_categories:
        if c in remaining_requiriments:
            remaining_requiriments.remove(c)


def main():
    """
    Read the initial board and the required equipments. Remove the equipments 
    that are already on the initial board from the remaining requiriments list. 
    Read the input itens and tries to fit it on the board. Them, print the final
    state of the board. If any requirement was missing, print them. 
    """

    # Stores categories of equipment already present on the board:
    already_have_categories = []

    board = read_board(already_have_categories)  # Read the board representation


    # Dimensions of the board:
    r = len(board)  # Set the number of rows to the length of the board list
    c = len(board[0])  # Set the number of columns to the length of the first row

    # Stores the remaining required equipment categories:
    remaining_requiriments = input().split(", ")  # Read the list of required equipment categories
    

    remove_already_have_equipments(remaining_requiriments, already_have_categories)  # Remove categories already present on the board

    read_itens(board, r, c, remaining_requiriments)  # Read and process item inputs

    print_board(board, r, c)  # Print the final state of the board

    if len(remaining_requiriments) != 0:  # Check if any items were missing
        print(f"Faltou: {', '.join(remaining_requiriments)}")

    return 1


main()  # Start the program execution
