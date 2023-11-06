temPessimo = False

nome_filme_1 = input("")
pontuacao_global_filme_1 = int(input(""))
critica_filme_1 = input("")

if critica_filme_1 == "boa":
    pontuacao_global_filme_1 *= 1.25

elif critica_filme_1 == "ruim":
    pontuacao_global_filme_1 *= 0.75

elif critica_filme_1 == "pessima":
    pontuacao_global_filme_1 *= 0
    filmePessimo = nome_filme_1
    temPessimo = True



nome_filme_2 = input("")
pontuacao_global_filme_2 = int(input(""))
critica_filme_2 = input("")

if critica_filme_2 == "boa":
    pontuacao_global_filme_2 *= 1.25

elif critica_filme_2 == "ruim":
    pontuacao_global_filme_2 *= 0.75

elif critica_filme_2 == "pessima":
    pontuacao_global_filme_2 *= 0
    filmePessimo = nome_filme_2
    temPessimo = True



nome_filme_3 = input("")
pontuacao_global_filme_3 = int(input(""))
critica_filme_3 = input("")

if critica_filme_3 == "boa":
    pontuacao_global_filme_3 *= 1.25

elif critica_filme_3 == "ruim":
    pontuacao_global_filme_3 *= 0.75

elif critica_filme_3 == "pessima":
    pontuacao_global_filme_3 *= 0
    filmePessimo = nome_filme_3
    temPessimo = True


#
if pontuacao_global_filme_1 > pontuacao_global_filme_2 > pontuacao_global_filme_3:
    filme1 = nome_filme_1
    filme2 = nome_filme_2
    filme3 = nome_filme_3

elif pontuacao_global_filme_1 > pontuacao_global_filme_3 > pontuacao_global_filme_2:
    filme1 = nome_filme_1
    filme2 = nome_filme_3
    filme3 = nome_filme_2

elif pontuacao_global_filme_2 > pontuacao_global_filme_1 > pontuacao_global_filme_3:
    filme1 = nome_filme_2
    filme2 = nome_filme_1
    filme3 = nome_filme_3

elif pontuacao_global_filme_2 > pontuacao_global_filme_3 > pontuacao_global_filme_1:
    filme1 = nome_filme_2
    filme2 = nome_filme_3
    filme3 = nome_filme_1

elif pontuacao_global_filme_3 > pontuacao_global_filme_1 > pontuacao_global_filme_2:
    filme1 = nome_filme_3
    filme2 = nome_filme_1
    filme3 = nome_filme_2

elif pontuacao_global_filme_3 > pontuacao_global_filme_2 > pontuacao_global_filme_1:
    filme1 = nome_filme_3
    filme2 = nome_filme_2
    filme3 = nome_filme_1


#

print("**** TOP 3 FILMES ****")
print(f"{filme1} está em 1° lugar")
print(f"{filme2} está em 2° lugar")
print(f"{filme3} está em 3° lugar")

if temPessimo:
    print(f"{filmePessimo} teve uma crítica péssima")