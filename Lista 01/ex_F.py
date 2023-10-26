nome = str(input("")) 
sobrenome = str(input(""))

nickname = nome+sobrenome

nickname_list = nickname.split()

for c in range(0, len(nickname_list)):
    if nickname_list[c] == ' ':
        nickname_list[c] = '_'

nickname = ''.join(nickname_list)

if len(nickname) < 3:
    print(nickname + ((3 - len(nickname)) * '_'))
else:
    print(nickname[0:16])
