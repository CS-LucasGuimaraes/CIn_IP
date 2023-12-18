# 
def suitcases(): #return list[ordered suitcases]
    weights = input().split(', ')

    weights.sort()

    weights[0], weights[-1] = weights[-1], weights[0]
    weights[1], weights[-2] = weights[-2], weights[1]

    return weights;

#
def parameters(): #return list[speed, load, people]
    read = input().split(', ')
    
    coal = int(read[0])
    weight = int(read[1])
    passenger = int(read[2])

    speed = int((coal + 200)/2)
    load = int((weight + 4000)/1000)
    people = passenger + 40

    return [speed, load, people]

#
def shift(): # return string
    employees = input().split(", ")
    time = input().split(":")
    path = input(); path = int(path[-1])

    chosen_emplyees = ""

    if (7 < int(time[0]) < 21):
        if (path == 1):
            chosen_emplyees += employees[0] + ", " + employees[1]
        else:
            chosen_emplyees +=  employees[0] + ", " + employees[-1]
    else:
        if (path == 1):
            chosen_emplyees += employees[2]
        else:
            chosen_emplyees += "Nenhum!" + ' ' + "O turno da Madrugada vai ser tranquilo para todos"
    
    return chosen_emplyees

#
def control(): #int main()
    print("A nova organização das malas é a seguinte: ", end='')
    ordered_suitcases = suitcases()
    for s in range(len(ordered_suitcases)-1):
        print(ordered_suitcases[s], end=', ')
    print(ordered_suitcases[-1])

    parameters_list = parameters()
    print(f"A velocidade que o trem partirá é de: {parameters_list[0]}Km/H")
    print(f"A carga do Trem em Toneladas é: {parameters_list[1]} Ton.")
    print(f"A quantidade de passageiros é de {parameters_list[2]}")

    print(f"Os funcionários convocados são: {shift()}")

    return 0

control()
