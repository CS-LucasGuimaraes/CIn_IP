nome_missao = input()
participantes = []

entrada = input()
while entrada != "Grupo formado":
    participantes.append(entrada)
    entrada = input()

print(f"O grupo formado por {len(participantes)} heróis para a missão {nome_missao} foi:")

for c in participantes:
    print(f"- {c}")