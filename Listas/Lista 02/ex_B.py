pont = 0

while(1):
    string = input("")
    if string == "amei":
        pont += 4
    elif string == "não parei de ouvir":
        while (1):
            str = input("")
            if str == "pulei":
                break
            pont += 4
    elif string == "escutei só metade":
        pont += 2
    elif string == "parei":
        break

print(f"Você ouviu {pont} minutos hoje!!!")
