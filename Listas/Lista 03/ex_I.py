string = input()
answer = ''
flag = False

for c in string:
    if (c != ' '): c = chr(ord(c)+len(string))
    if c in "0123456789":
        print("Algo de errado não está certo. Será que estou ficando doido?")
        flag = True;
    else:
        answer += c;

if flag == False:
    if (answer.strip() == ""): print("Ué não tem nada para me decifrar aqui")
    else: print(f"Descobri o que a mensagem significa: {answer}")