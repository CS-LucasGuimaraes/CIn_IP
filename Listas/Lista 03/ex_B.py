respostas = [['Zeus', 'deus', 'trovão'], ['Afrodite', 'amor', 'deusa'], ['Poseidon', 'deus', 'oceanos'], ['Hércules', 'força', 'semideus'], ['Aquiles', 'resistência', 'semideus'], ['Orfeu', 'música', 'semideus']]

perguntas = int(input())
corretas = 0

if perguntas == 0:
    print("Infelizmente, Percy Jackson, chegou atrasado para a exame...")

else:
    for c in range(perguntas):
        lista = input().split(', ')
        lista.sort()
        if lista in respostas:
            print(f"A resposta da {c+1}ª questão está... CORRETA!")
            corretas += 1
        else:
            print(f"A resposta da {c+1}ª questão está... ERRADA!")

    porcentagem = int((corretas / perguntas) * 100)

    print(f"Percy Jackson, sua taxa de acerto no EDEM é de aproximadamente... {porcentagem}%")

    if porcentagem < 20:
        print("Bem... te vejo ano que vem")
    elif porcentagem < 60:
        print("Você pode melhorar um pouco mais!")
    elif porcentagem < 100:
        print("Muito bem, você quase pode começar a desfilar entre os semideuses!")
    elif porcentagem == 100:
        print("UAU, você gabaritou! Você é praticamente um deus do Olimpo!")

