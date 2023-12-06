inp = input()

inp.split()

informacoes_deuses = [
    ['Zeus', 'Poseidon', 'Atenas', 'Ares', 'Afrodite'],
    [100, 90, 80, 70, 60],
    ['Raio', 'Tridente', 'Égide', 'Lança', 'Cinto Mágico']
    ]

for c in range(len(inp)):
    i = int(inp[c])
    if i == 2 or i == 4:
        print(f"Deusa:{informacoes_deuses[0][i]}")
    else:
        print(f"Deus:{informacoes_deuses[0][i]}")
    print(f"Poder:{informacoes_deuses[1][i]}")
    print(f"Artefato:{informacoes_deuses[2][i]}")

    if c != len(inp)-1:
        print("")
