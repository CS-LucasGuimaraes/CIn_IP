import math

x_atual = int(input(""))
z_atual = int(input(""))

Dist_Hogsmeade = float(math.sqrt((x_atual-34)**2+(z_atual-220)**2))
Dist_Kakariko = float(math.sqrt((x_atual)**2+(z_atual)**2))
Dist_Solitude = float(math.sqrt((x_atual-140)**2+(z_atual-456)**2))

print(f"Distancia para Hogsmeade: {Dist_Hogsmeade:.2f}")
print(f"Distancia para Kakariko: {Dist_Kakariko:.2f}")
print(f"Distancia para Solitude: {Dist_Solitude:.2f}")
