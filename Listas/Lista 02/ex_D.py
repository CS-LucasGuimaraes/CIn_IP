len = int(input())

pont_taylor = 0;
pont_beyonce = 0;

print("Vai começar! Vamos ver quem é a verdadeira diva!")

for c in range (len):
    if pont_taylor < 3 and pont_beyonce < 3:
        print(f"Vai começar a {c+1}º rodada!")

        nota_coreo_tay = int(input())
        nota_figurino_tay = int(input())
        nota_coreo_bey = int(input())
        nota_figurino_bey = int(input())

        nota_total_tay = nota_coreo_tay*4 + nota_figurino_tay*3
        nota_total_bey = nota_coreo_bey*4 + nota_figurino_bey*3

        if nota_total_tay > nota_total_bey:
            pont_taylor += 1
            print(f"Fim da apresentação! O placar da rodada {c+1} foi {nota_total_tay}x{nota_total_bey} para os representantes da Tay.")
        elif nota_total_bey > nota_total_tay:
            pont_beyonce += 1
            print(f"Fim da apresentação! O placar da rodada {c+1} foi {nota_total_bey}x{nota_total_tay} para os representantes da Bey.")

        if abs(nota_total_tay-nota_total_bey) > 20:
            print(f"A diferença na pontuação foi de {abs(nota_total_tay-nota_total_bey)} pontos.")
        else:
            print(f"A diferença de pontos foi de apenas {abs(nota_total_tay-nota_total_bey)}.")

if pont_taylor > pont_beyonce:
    print(f"Uuuh! Por um placar de {pont_taylor} a {pont_beyonce}, a equipe da Taylor Swift venceu a competição e mostrou que ela é a verdadeira diva do pop!")
else:
    print(f"Minha nossa! A equipe da Beyoncé chocou o mundo e venceu a equipe da Taylor Swift por um placar de {pont_beyonce} a {pont_taylor}. A Bey é a verdadeira rainha do pop!")
