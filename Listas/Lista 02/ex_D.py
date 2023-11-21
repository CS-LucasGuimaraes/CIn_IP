len = int(input())

pontt = 0;
pontb = 0;

print("Vai começar! Vamos ver quem é a verdadeira diva!")

for c in range (len):
    if pontt < 3 and pontb < 3:
        print(f"Vai começar a {c+1}º rodada!")

        nct = int(input())
        nft = int(input())
        ncb = int(input())
        nfb = int(input())

        ntt = nct*4 + nft*3
        ntb = ncb*4 + nfb*3

        if ntt > ntb:
            pontt += 1
            print(f"Fim da apresentação! O placar da rodada {c+1} foi {ntt}x{ntb} para os representantes da Tay.")
        elif ntb > ntt:
            pontb += 1
            print(f"Fim da apresentação! O placar da rodada {c+1} foi {ntb}x{ntt} para os representantes da Bey.")

        if abs(ntt-ntb) > 20:
            print(f"A diferença na pontuação foi de {abs(ntt-ntb)} pontos.")
        else:
            print(f"A diferença de pontos foi de apenas {abs(ntt-ntb)}.")

if pontt > pontb:
    print(f"Uuuh! Por um placar de {pontt} a {pontb}, a equipe da Taylor Swift venceu a competição e mostrou que ela é a verdadeira diva do pop!")
else:
    print(f"Minha nossa! A equipe da Beyoncé chocou o mundo e venceu a equipe da Taylor Swift por um placar de {pontb} a {pontt}. A Bey é a verdadeira rainha do pop!")
