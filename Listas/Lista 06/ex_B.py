def main():
    notes = {}
    times = {}

    name = input()
    while (name != "Não há mais escolas"):
        theme = input()
        duration = int(input())

        times[name] = duration;
        notes[name] = 0

        name = input()


    print("Desfile de samba do Rio de janeiro 2024")

    evaluation_question = input()
    reps = 0
    while evaluation_question != "Não há mais quesitos":
        print(f"Vamos às notas para o quesito {evaluation_question}:")
        for _ in range(len(notes)):
            note = input().split(" - ")
            notes[note[0]] += float(note[1])
            print(f"{note[0]}: {note[1]}")

        evaluation_question = input()
        reps += 1
    
    for key in notes:
        notes[key] /= reps;
        notes[key] = round(notes[key], 2)
    
    for key in times:
        reduction = 0

        if times[key] < 65:
            reduction = 0.1 * (65 - times[key])
        if times[key] > 75:
            reduction = 0.1 * (times[key] - 75)
        
        notes[key] -= reduction

    print("E o vencedor do desfile de escola de samba do Rio de Janeiro de 2024 é:")

    sorted_dict = []

    for element in notes:                       # Iterates over the dict, getting it's key and val
        key = element
        val = notes[element]

        sorted_dict.append((val,key))           # Push the values reversed to the list

    sorted_dict.sort(reverse=True)              # Sort the list by the ponctuation

    print(f"{sorted_dict[0][1]} com uma nota final de {sorted_dict[0][0]}!")

    return 1


main()  # Start the program execution
