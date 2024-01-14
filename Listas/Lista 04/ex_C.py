def asciiSum(ascii_list):
    sum = 0
    for i in ascii_list:
      sum += int(i)

    return sum


# read a gift in ascii and transforms it to string. Also check if it can be on the final list.
def gift(): # [ [gift_name, is_on_final_list?], [string, bool] ]
    gift_name_ascii = input().split()
    gift_name = ""
    for c in gift_name_ascii:
       gift_name += chr(int(c))

    if (asciiSum(gift_name_ascii)%2 == 0):
        return [gift_name, True]
    else:
        return [gift_name, False]

  
def main():
    
    n = int(input())
    gift_list = [[],[]]             # [ [item_list #string], [is_on_final_list? #bool] ]
    excluded_gifts = []
    accepted_gifts = []

    for tc in range(n):                     # For each gift:
        item = gift()                           # Read the current gift
        
        if (item[0] == ''): continue            # If there's no gift, continue

        if (item[0] not in gift_list[0]):       # If it wasn't on list, add it.
            print(f"{item[0]} foi adicionado a lista ultrassecreta de presentes da Anya!!")
            gift_list[0].append(item[0])                # Make a list with gifts names
            gift_list[1].append(item[1])                # Make a list with the bool representing if the present was accepted or not
        else:                                   # If it's already on list, warn.
            print(f"{item[0]} já está na lista de presentes da Anya!!")
        
    for e in range(len(gift_list[0])):      # For each gift in gift_list 
        if gift_list[1][e]:                     # If the present can be added, add its name to accepted list
            accepted_gifts.append(gift_list[0][e])
        else:                                   # If the present can't be added, add its name to excluded list
            excluded_gifts.append(gift_list[0][e])

    if len(excluded_gifts) > 0:             # If some gift was excluded
        print(f"Infelizmente o Twilight é mão de vaca e os seguintes itens precisaram ser excluídos da lista de presentes ultrassecretos da Anya: {', '.join(excluded_gifts)}.")
    elif len(accepted_gifts) != 0:          # Else if any gift was accepted 
        print("Parece que o Dia das Crianças desse ano será especial!!!! Anya ganhará todos os presentes planejados, mesmo que ela não seja tão exemplar como deveria…")

    if len(accepted_gifts) == 0:            # If any gift was accepted
        print("O quê? Nenhum presente? Isso é um absurdo! Vamos corrigir essa injustiça e garantir que Anya tenha um Dia das Crianças inesquecível!")
    else:                                   # If at least one gift was accepted
        print(f"Lista final dos melhores presentes da Anya: {', '.join(accepted_gifts)}.")

    return 1


main()
