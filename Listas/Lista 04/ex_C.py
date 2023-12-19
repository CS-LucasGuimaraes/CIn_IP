def asciiSum(ascii_list):
    sum = 0
    for i in ascii_list:
      sum += int(i)

    return sum

def gift():
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
    gift_list = [[],[]]
    excluded_gifts = []
    accepted_gifts = []

    for tc in range(n): 
        item = gift()
        
        if (item[0] == ''): continue

        if (item[0] not in gift_list[0]):
            print(f"{item[0]} foi adicionado a lista ultrassecreta de presentes da Anya!!")
            gift_list[0].append(item[0])
            gift_list[1].append(item[1])
        else:
            print(f"{item[0]} já está na lista de presentes da Anya!!")
        
    for e in range(len(gift_list[0])):
        if gift_list[1][e]:
            accepted_gifts.append(gift_list[0][e])
        else:
            excluded_gifts.append(gift_list[0][e])

    if len(excluded_gifts) > 0:
        print(f"Infelizmente o Twilight é mão de vaca e os seguintes itens precisaram ser excluídos da lista de presentes ultrassecretos da Anya: {', '.join(excluded_gifts)}.")
    elif len(accepted_gifts) != 0:
        print("Parece que o Dia das Crianças desse ano será especial!!!! Anya ganhará todos os presentes planejados, mesmo que ela não seja tão exemplar como deveria…")

    if len(accepted_gifts) == 0:
        print("O quê? Nenhum presente? Isso é um absurdo! Vamos corrigir essa injustiça e garantir que Anya tenha um Dia das Crianças inesquecível!")
    else:
        print(f"Lista final dos melhores presentes da Anya: {', '.join(accepted_gifts)}.")

    return 1

main()
