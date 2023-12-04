desejos = input().split(", ")
encontrados = input().split(", ")
n = 0
desejos_encontrados = []

for item in desejos:
    if item in encontrados:
        desejos_encontrados.append(item)

if len(desejos_encontrados) != 0:
    print("Estes são os itens que já tenho no Acampamento Meio-Sangue:")
    for item in desejos_encontrados:
        n += 1
        print(f"{n}º item: {item}")

if n == 0:
    print(f"Hmm, preciso visitar um vendedor ambulante! Não encontrei nenhum dos {len(desejos)} itens aqui no Acampamento Meio-Sangue.")
elif n != len(desejos):
    print(f"Vou precisar adquirir {len(desejos)-n} itens antes da batalha!")
else:
    print(f"Perfeito, encontrei todos os {len(desejos)} itens aqui no Acampamento Meio-Sangue!")

print("Estou pronto para a batalha! Que comece a guerra contra os Titãs!")