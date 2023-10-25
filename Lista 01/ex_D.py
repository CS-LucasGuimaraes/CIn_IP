qntd_arthur = int(input("Quantos diamantes Arthur coletou por hora? "))
qntd_luiz = int(input("Quantos diamantes Luiz coletou por hora? "))
qntd_pedro = int(input("Quantos diamantes Pedro coletou por hora? "))
tempo_horas = int(input("Quantas horas durou a competição? "))

# x = (a + b + (|a - b|)) / 2

max_parcial = (( qntd_arthur + qntd_luiz + abs(qntd_arthur-qntd_luiz) ) / 2)
max = (( max_parcial + qntd_pedro + abs(max_parcial-qntd_pedro) ) /2) * tempo_horas

print(int(max))
