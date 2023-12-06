colection = input().strip(", ")
editions = int(input())

book_count = 0
missing = 0

list = ["O Ladrão de Raios","O Mar de Monstros","A Maldição do Titã","A Batalha do Labirinto","O Último Olimpiano"]
missing_books = []

for book in colection:
    if book in list:
    
        book_count += 1

for book in list:
    if book not in colection:
        missing += 1
        missing_books.append(book)

if book_count == 5:
    print("Sua coleção está completa! Você pode ler à vontade.")
elif book_count == 0:
    print("Caramba, você não tem nenhum livro. Compre todos imediatamente.")
else:
    print("Infelizmente, sua coleção está incompleta. Falta(row) esse(s) livro(s): .",end="")
    for book in range(len(missing_books)):
        if book != len(missing_books):
            print(missing_books[book],end=", ")
        else:
            print(missing_books[book])

# if editions > book_count:
