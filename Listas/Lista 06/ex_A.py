def main():
    """
    Get the score for each Samba School. Check if the School is in the list of Rio de Janeiro's Sambas Schools. If it is, update its score. At the end, print the scoreboard sorted from the greatest to the lowest and show the winner and the last place.
    """
    # Tuple with every Samba School from Rio de Janeiro
    samba_schools = ("Porto da Pedra", "Beija-flor", "Salgueiro", "Grande Rio", "Unidos da Tijuca", "Imperatriz", "Mocidade", "Portela", "Vila Isabel", "Mangueira", "Paraíso do Tuiuti", "Viradouro") 
    
    # The dict where all the scores are going to be stored
    dict = {}

    score = input().split(": ");
    while score != ['Fim']:                     # Gets the score until the end... 
        if score[0] not in samba_schools:       # Checks if the school is not from Rio de Janeiro
            print("Epa, o que essa escola está fazendo aqui?!");

        else:                                   # If it is from Rio:
            if score[0] not in dict:            # Check if it's the first appear
                dict[score[0]] = score[1]       # Create the key for the school with the value
                print(f"{score[0]} teve sua nota apurada!")

            else :                              # If it has appeared before
                dict[score[0]] = score[1]       # Update the value
                print(f"{score[0]} teve sua nota atualizada!")

        score = input().split(": ")             # Gets the next input

    # List which will receive the tuples in the dict in reversed order (value, key)
    sorted_dict = []

    for element in dict:                        # Iterates over the dict, getting it's key and val
        key = element
        val = dict[element]

        sorted_dict.append((val,key))           # Push the values reversed to the list

    sorted_dict.sort(reverse=True)              # Sort the list by the ponctuation
    

    print("\nCLASSIFICAÇÃO DO CARNAVAL 2024:")

    counter = 0;
    for e in sorted_dict:                       # Iterates over the sorted list to print the scoreboard
        counter += 1;
        print(f"{counter}. {e[1]}: {e[0]}")

    # Prints the best school
    print(f'\nÉ CAMPEÃ! A ESCOLA {sorted_dict[0][1]} É A GRANDE VENCEDORA DO CARNAVAL DE 2024, FAZENDO {sorted_dict[0][0]} PONTOS!!')
    
    # Prints the worst school
    print(f"Infelizmente, a escola {sorted_dict[-1][1]} não alcançou as expectativas, fazendo apenas {sorted_dict[-1][0]} pontos, e foi rebaixada.")

    return 1


main()  # Start the program execution
