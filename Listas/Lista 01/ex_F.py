sua_vida = int(input(""))
poder_sua_arma = int(input(""))
sua_habilidade_luta = int(input(""))
seu_poder_surpresa = int(input(""))
poder_arma_mascarado = int(input(""))
habilidade_luta_mascarado = int(input(""))
poder_surpresa_mascarado = int(input(""))
defesa_mascarado = int(input(""))

if poder_sua_arma > poder_arma_mascarado and sua_habilidade_luta > habilidade_luta_mascarado and seu_poder_surpresa > poder_surpresa_mascarado:
    print("Ainda bem que deu tudo certo, está quase em casa")
else:
    sua_vida -= defesa_mascarado
    if sua_vida > 0:
        print("Rápido, corra antes que ele vá atrás de você!")
        seu_poder_surpresa *= 105/100
        sua_habilidade_luta *= 95/100
        poder_sua_arma *= 95/100
    else:
        print("Oh, no! Acabou pra mim")
        exit()

poder_arma_novo_mascarado = int(input(""))
habilidade_luta_novo_mascarado = int(input(""))
poder_surpresa_novo_mascarado = int(input(""))

if poder_sua_arma >= poder_arma_novo_mascarado or sua_habilidade_luta >= habilidade_luta_novo_mascarado or seu_poder_surpresa >= poder_surpresa_novo_mascarado:
    print("Casa, aqui vou eu")
else:
    print("Oh, no! Acabou pra mim")
