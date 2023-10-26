# 3 horas por dia
# Dia completo tem 24000 ticks. Um dia vai de 0 à 12000 e uma noite de 12001 a 24000.
# 24000 ticks = 20 minutos -> 20 ticks/segundo
# 1 hora => 72000

dias_reais = int(input(""))
qntd_casas = int(input(""))

ticks_por_casa = (dias_reais * 3 * 72000 / 2)/qntd_casas

print(int(ticks_por_casa))
