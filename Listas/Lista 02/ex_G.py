len = int(input())
platscore = 0

for c in range(len):
    text_plat = input()
    plat = str()

    for char in text_plat:
        plat += (char.upper())

    if c == 0:
        print("Cause, baby, now we've got")
        if plat == "BAD BLOOD":
            print(plat)
            platscore += 1
    
    elif c == 1:
        print("You know it used to be")
        if plat == "MAD LOVE":
            print(plat)
            platscore += 1
    
    elif c == 2:
        print("So take a look what")
        if plat == "YOU'VE DONE":
            print(plat)
            platscore += 1

    elif c == 3:
        print("Cause, baby, now we've got")
        if plat == "BAD BLOOD, HEY":
            print(plat)
            platscore += 1

if platscore == len:
    print("A plateia deu um show! Acertou tudo!")
elif platscore >= float(len/2):
    print("A plateia acertou a maior parte da música")
else:
    print("Foi um dia atípico e a plateia se esqueceu de grande da música")
