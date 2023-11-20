len = int(input())
pont_total = 1


for c in range(len):
    music = input("").lower()
    pont = 0
    for l in music:
        if l in "aeiou":
            pont+=1
        else:
            pont+=2
    pont_total *= pont;
 
print(f"Parabéns por adquirir o ingresso! Seu assento é o {pont_total}, estamos ansiosos para vê-lo, vai ser incrível!")