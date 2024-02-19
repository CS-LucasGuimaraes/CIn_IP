prices = {
    "tomate": 3, "cebola": 2, "coentro": 1, "manteiga": 5.5, "macaxeira": 3,
    "alho": 1.5, "pimentao": 2, "azeite": 15, "camarao": 30, "carne de sol": 30, 
    "queijo coalho": 15, "massa de tapioca": 10, "moranga": 10 , "dende": 15,
    "creme de leite": 4, "leite de coco": 5, "bobo de camarao": 58,
    "tapioca de carne de sol": 60, "carne de sol com macaxeira": 38.5,
    "camarao na moranga": 68.5
}

ingredients = {
    "tomate": 5, "cebola": 5, "coentro": 5, "manteiga": 5, "macaxeira": 5,
    "alho": 5, "pimentao": 5, "azeite": 5, "camarao": 5, "carne de sol": 5, 
    "queijo coalho": 5, "massa de tapioca": 5, "moranga": 5, "dende": 5,
    "creme de leite": 5, "leite de coco": 5, "bobo de camarao": 5,
    "tapioca de carne de sol": 5, "carne de sol com macaxeira": 5,
    "camarao na moranga": 5
}

recipes = {
    "bobo de camarao": ("camarao", "macaxeira", "leite de coco", 
                        "dende", "tomate", "cebola"),
    
    "tapioca de carne de sol": ("massa de tapioca", "carne de sol",
                                 "queijo coalho", "tomate", "cebola"),
    
    "carne de sol com macaxeira": ("carne de sol", "macaxeira", "manteiga"),
    
    "camarao na moranga": ("moranga", "camarao", "cebola", "alho", "tomate", 
                           "pimentao", "creme de leite", "azeite", "coentro")
}

input_list = []

requested = {}

orders = {}

money = 30
index = 0


def read_untill_EOF():
    input_list = []
     
    while True:
        try:
            x = input()
            input_list.append(x)
        except EOFError:
            break
          
    return input_list


def newrecipe(order):
    global input_list, index

    if requested.get(order, 0) >= 2:
        recipe = []
        price = 5
        for _ in range(9):
            index += 1
            ingredient = input_list[index]
            recipe.append(ingredient)
            price += prices[ingredient]
        recipes[order] = tuple(recipe)
        prices[order] = price

        print(f"Atendendo demandas, {order} é a mais nova adição ao cardápio do Sabores de Recife.")
    else:
        requested[order] = requested.get(order, 0) + 1
        print(f"{order} ainda não é uma opção disponível.")


def check_ingredients(order):
    global money

    if order not in recipes:
        newrecipe(order)
    else:
        for ingredient in recipes[order]:
            if ingredients[ingredient] >= 1:
                ingredients[ingredient] -= 1
            else:
                ingredients[ingredient] = 3
                money -= prices[ingredient]

        money += prices[order]
        print(f"{order} saindo...")
        
        orders[order] = orders.get(order, 0) + 1 

def main():
    global money, index, input_list

    input_list = read_untill_EOF()


    while index != len(input_list):
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
