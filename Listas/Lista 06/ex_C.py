# Dict with every ingredient and recipe and it's prices
prices = {
    "tomate": 3, "cebola": 2, "coentro": 1, "manteiga": 5.5, "macaxeira": 3,
    "alho": 1.5, "pimentao": 2, "azeite": 15, "camarao": 30, "carne de sol": 30, 
    "queijo coalho": 15, "massa de tapioca": 10, "moranga": 10 , "dende": 15,
    "creme de leite": 4, "leite de coco": 5, "bobo de camarao": 58,
    "tapioca de carne de sol": 60, "carne de sol com macaxeira": 38.5,
    "camarao na moranga": 68.5
}

# Dict with every ingredient and the remaining ammount of each one
ingredients = {
    "tomate": 5, "cebola": 5, "coentro": 5, "manteiga": 5, "macaxeira": 5,
    "alho": 5, "pimentao": 5, "azeite": 5, "camarao": 5, "carne de sol": 5, 
    "queijo coalho": 5, "massa de tapioca": 5, "moranga": 5, "dende": 5,
    "creme de leite": 5, "leite de coco": 5, "bobo de camarao": 5,
    "tapioca de carne de sol": 5, "carne de sol com macaxeira": 5,
    "camarao na moranga": 5
}

# Dict with every recipe and the necessary ingredients for each one
recipes = {
    "bobo de camarao": ("camarao", "macaxeira", "leite de coco", 
                        "dende", "tomate", "cebola"),
    
    "tapioca de carne de sol": ("massa de tapioca", "carne de sol",
                                 "queijo coalho", "tomate", "cebola"),
    
    "carne de sol com macaxeira": ("carne de sol", "macaxeira", "manteiga"),
    
    "camarao na moranga": ("moranga", "camarao", "cebola", "alho", "tomate", 
                           "pimentao", "creme de leite", "azeite", "coentro")
}


input_list = []                 # A list with the inputs (used because the input is processed until EOF)
index = 0                       # Current input index

# Dict with the recipes that were requested and the ammount of times that they were requested
requested = {}

# Dict with the recipes that were ordered and the ammount of times they were ordered
orders = {}

# The current balance 
money = 30


def read_untill_EOF():
    """
    Try to read an input untill recieves an EOF Error. Store every input on a list and return it.

    Returns:
        list(string): The list of every input read.
    """
    input_list = []
     
    while True:
        try:
            x = input()
            input_list.append(x)
        except EOFError:
            break
          
    return input_list


def newrecipe(order):
    """
    Checks if the recipe was requested at least 2 times before. If yes, then, create the recipe, reading its ingredients and adding it to the recipes dict and its price to the prices dict, otherwise, print a message 
    saying that its not available yet.

    Args:
        input_list (list): The list which stores the inputs.
        index (int): The actual index onf the input_list.
        order (string): The order that are being processed.
    """
    global input_list, index

    if requested.get(order, 0) >= 2:            # Checks if the recipe was requested at least twice before
        recipe = []
        price = 5                               # Starts the price in 5
        for _ in range(9):                      # Read 9 ingredients
            index += 1                          
            ingredient = input_list[index]
            recipe.append(ingredient)           # Append the ingredient on recipe
            price += prices[ingredient]         # Sum the ingredient price on the total price
        recipes[order] = tuple(recipe)          # Push the recipe to the map of recipes
        prices[order] = price                   # Push the price to the map of prices

        print(f"Atendendo demandas, {order} é a mais nova adição ao cardápio do Sabores de Recife.")
    else:                                       # If the recipe wasn't requested twice before
        requested[order] = requested.get(order, 0) + 1     # Add one to the requested counter
        print(f"{order} ainda não é uma opção disponível.")


def check_ingredients(order):
    """
    Checks if the recipe for the order are defined. If not, check the new recipe,
    otherwise, iterates over each ingredient and verify the ammount of required
    ingredients. Buy some new ingredients if necessary.

    Args:
        money (int): The current balance
        order (string): The order that are being processed.
    """
    global money

    if order not in recipes:                    # If the recipe for the order are not defined
        newrecipe(order)                        
    else:
        for ingredient in recipes[order]:       # Iterates over each ingredient on the recipe
            
            if ingredients[ingredient] >= 1:    # If still has the ingredient 
                ingredients[ingredient] -= 1    # Subtract one of the quantity

            else:                               # If there aren't enough ingredients
                ingredients[ingredient] = 3     # Buy 4 ingredients and use 1
                money -= prices[ingredient]*4   # Reduces 4 times the ingredient price

        money += prices[order]                  # Win the money of the order
        print(f"{order} saindo...")
        
        orders[order] = orders.get(order, 0) + 1 


def main():
    """
    Gets user input, handles even inputs, calls the oddFactorial function, and prints the result.
    """
    global money, index, input_list

    input_list = read_untill_EOF()              # Gets user input

    while index != len(input_list):             # Iterates over the inputs and check every order
        check_ingredients(input_list[index])
        index += 1
    
    print("##### Fim do expediente #####")      
    print(f"O lucro obtido no dia de hoje foi de R${money-30:.2f}.")

    sorted_dict = []

    for element in orders:                      # Iterates over the dict, getting it's key and val
        key = element
        val = orders[element]

        sorted_dict.append((val,key))           # Push the values reversed to the list

    sorted_dict.sort(reverse=True)              # Sort the list by the ponctuation

    if sorted_dict[0][1] == "bobo de camarao":
        print("O bom e tradicional Bobó de Camarão, líder em vendas, nunca será superado!")
    else:
        print(f"{sorted_dict[0][1].capitalize()} está fazendo sucesso entre os clientes, ultrapassando até mesmo o lendário Bobó de Camarão.")

    return 1


main()  # Start the program execution
