row = int(input()); col = int(input())

matrix = [[] for k in range(row)]

for i in range(row):
  for j in range(col):
    matrix[i].append(input())

sum = [0 for k in range(row)]
for i in range(row):
  for j in range(col):
    sum[i] += int(matrix[i][j])
    print(matrix[i][j], end="")
    if j != col-1: print(" ",end="")
  print("")

quantidade_campistas = sum[0]
numero_chale = 1

for i in range(len(sum)):
  if sum[i] > quantidade_campistas:
    quantidade_campistas = sum[i]
    numero_chale = i+1
 
print(f'\nO chalé {numero_chale} foi o que mais recebeu semi-deuses, tendo um acréscimo de {quantidade_campistas} novos campistas!')
