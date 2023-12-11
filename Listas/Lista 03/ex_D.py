books = input()
n = int(input())

total_books = ['O Ladrão de Raios', 'O Mar de Monstros', 'A Maldição do Titã', 'A Batalha do Labirinto', 'O Último Olimpiano']

if n == 0:
  print ('Caramba, você não tem nenhum livro. Compre todos imediatamente.')

else:  
  list = books.split(', ')
 
  same = []
  other = []
  missing = []
 
  for book in list:
    if book in total_books:
      same.append(book)
    else:
      other.append(book)
 
  for book in total_books:
    if book not in list:
      missing.append(book)
 
  if len(same) == len(total_books):
    print('Sua coleção está completa! Você pode ler à vontade.')
   
  elif len(same) == 0:
    print ('Caramba, você não tem nenhum livro. Compre todos imediatamente.')
 
  elif len(same) > 0 and len(same) < len(total_books):
    l = ', '.join(missing)
    print(f'Infelizmente, sua coleção está incompleta. Falta(m) esse(s) livro(s): {l}.')
 
  if len(other) > 0:
    j = ', '.join(other)
    print(f'Cuidado, Sérgio! Você está organizando seus livros de uma forma errada, o(s) livro(s): {j}, não faz(em) parte da saga "Percy Jackson e os Olimpianos".')