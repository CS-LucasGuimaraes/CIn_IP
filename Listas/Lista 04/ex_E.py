INF = 999
alphabet = "abcdefghijklmnopqrstuvwxyz"
vowels = 'aeiou'
ascci_A = 97

def pangram(string):
    for i in alphabet:
        if i not in string.lower():
            return False

    return True


store_fib = [-1 for k in range(INF)]
def fib(n): #DP for efficiency #MaratonaCIn
    if store_fib[n] != -1: return store_fib[n]

    if n == 0: return 0
    if n == 1: return 1

    store_fib[n] = fib(n-1) + fib(n-2)
    return store_fib[n]


def hasVowel(string):
    for i in vowels:
        if i in string.lower():
            return True
    return False 


def countLetter(string):
    lettermap = [0 for _ in range(26)]
    for c in string:
        if (c == ' '): continue
        lettermap[ord(c.lower())-ascci_A] += 1
    return lettermap


def minmap(lettermap):
    lettermap.sort()
    a = 0
    while lettermap[a] == 0:
        a += 1
    return lettermap[a]


def challengeX():
    string = input()

    if pangram(string):
        x = max(countLetter(string))
    else:
        x = minmap(countLetter(string))

    return x


def challengeY():
    string = input()

    sz = len(string)
    
    return fib(sz)*4 if hasVowel(string) else fib(sz)*2

def challengeZ():
    word = input().strip()
    string = input()

    upper_word = 0
    lower_word = 0

    for c in word:
        if c in alphabet: lower_word += 1
        else: upper_word += 1

    upper_string = 0
    lower_string = 0

    for c in string:
        if c in alphabet: lower_string += 1 
        elif c != ' ': upper_string += 1

    return int((lower_string-upper_string)**(lower_word-upper_word))


def main():
    x = challengeX()
    y = challengeY()
    z = challengeZ()

    i = int(input())
    j = int(input())
    k = int(input())

    dist = ( (x - i)**2 + (y - j)**2 + (z - k)**2 )**(1/2)

    print(f"A 1ª coordenada do Papai Noel é: {x}")
    print(f"A 2ª coordenada do Papai Noel é: {y}")
    print(f"A 3ª coordenada do Papai Noel é: {z}")
    print(f"A distância entre Jack Esqueleto e Papai Noel é: {dist:.2f}")

    return 1

main()
