# GLOBAL VARIABLES:
cities = [] # [ [dist, name, word, pos, dir, x, y] ]
Ascii_A = 65

# ---===---===---=*=---===---===--- #

def caeser(word, positions, direction): #string
    decodified = ''
    if direction == 'L': positions *= -1
    
    for c in word:
        x = (ord(c)-Ascii_A + (positions%26)) % 26

        decodified += chr(x+Ascii_A)

    return decodified


# Read each city, make some calculus and store it on a more convenient order (for sort)
def read_cities(cities_count): #void
    for c in range(cities_count):
        city = input().split(', ')
        name  = city[0]
        x = float(city[1]); y = float(city[2])
        word = city[3]; pos = int(city[4]); dir = city [5]

        dist = (((x-0)**2)+((y-0)**2))**(1/2)

        cities.append([dist, name, word, pos, dir, x, y])

    cities.sort(reverse=True)


# Quick flush of cities distance to match the distance for the actual city
def flushDistancies(actual_city): #void
    for c in cities:
        c[0] = (((c[5]-actual_city[5])**2)+((c[6]-actual_city[6])**2))**(1/2)
        
    cities.sort(reverse=True)


def main():
    cities_count = int(input())

    read_cities(cities_count)    

    # For each city: decodify the password, then, flush the distances.
    while(len(cities)!=0):
        actual_city = cities[-1]; cities.pop()
        decodified = caeser(actual_city[2], actual_city[3], actual_city[4])

        print(f"A senha da cidade {actual_city[1]} é: {decodified}")

        flushDistancies(actual_city)
        
    return 1


main()
