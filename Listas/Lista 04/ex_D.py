cities= [] #[ [dist, name, word, pos, dir, x, y] ]

def cesar(word, positions, direction):
    dir = 1
    decodified = ''
    if direction == 'L': dir = -1
    
    for c in word:
        x = ord(c)
        x += ((positions%26)*dir)

        if (x > 90): x -= 26
        elif (x < 65): x += 26

        decodified += chr(x)

    return decodified

def main():
    cities_count = int(input())

    for c in range(cities_count):
        city = input().split(', ')
        name  = city[0]
        x = float(city[1]); y = float(city[2])
        word = city[3]; pos = int(city[4]); dir = city [5]

        dist = (((x-0)**2)+((y-0)**2))**(1/2)

        cities.append([dist, name, word, pos, dir, x, y])

    cities.sort(reverse=True)

    while(len(cities)!=0):
        city = cities[-1]; cities.pop()
        decodified = cesar (city[2], city[3], city[4])

        print(f"A senha da cidade {city[1]} é: {decodified}")

        for c in cities:
            c[0] = (((c[5]-city[5])**2)+((c[6]-city[6])**2))**(1/2)
        
        cities.sort(reverse=True)

    return 1

main()