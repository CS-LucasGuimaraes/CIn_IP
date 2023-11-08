frase = input("")
verificador = 0

if frase == "Parou filhotada, assim vocês vão deixar todo mundo maluco.":
  caracteristica = input("")
  verificador = 1
  if caracteristica == "Uivar" or caracteristica == "Pelos" or caracteristica == "Caninos":
    print("Bem-vindos ao Hotel Transilvânia!")
    print("Wayne, seu cachorrão.")
    exit()

elif frase == "Veio de novo pelo correio, deixa de ser pão duro.":
  caracteristica = input("")
  verificador = 1
  if caracteristica == "Desmontável" or caracteristica == "Parafusos" or caracteristica == "Morto-vivo":
    print("Bem-vindos ao Hotel Transilvânia!")
    print("Frank, assim vai acabar perdendo a cabeça.")
    exit()

elif frase == "Quem me beliscou?":
  caracteristica = input("")
  verificador = 1
  if caracteristica == "Transparente":
    print("Bem-vindos ao Hotel Transilvânia!")
    print("Griffin, prazer em vê-lo.")
    exit()

elif frase == "Tô na área galera!":
  caracteristica = input("")
  verificador = 1
  if caracteristica == "Enfaixado" or caracteristica == "Morto-vivo":
    print("Bem-vindos ao Hotel Transilvânia!")
    print("Murray, sempre soltando areia.")
    exit()

if verificador == 0:
  caracteristica = input("")
  print("UM HUMANO! Quem é você, e como você achou esse lugar?")
elif verificador == 1:
  print("UM HUMANO! Quem é você, e como você achou esse lugar?")
