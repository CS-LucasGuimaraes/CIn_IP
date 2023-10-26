qntd_arthur = int(input(""))
qntd_luiz = int(input(""))
qntd_pedro = int(input(""))
tempo_horas = int(input(""))

# x = (a + b + (|a - b|)) / 2

max_parcial = (( qntd_arthur + qntd_luiz + abs(qntd_arthur-qntd_luiz) ) / 2)
max = (( max_parcial + qntd_pedro + abs(max_parcial-qntd_pedro) ) /2) * tempo_horas

print(int(max))
