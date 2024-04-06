print('''
**********
**********
''')

pReservada = "coice"

palavra = ['_','_','_','_','_']



print(palavra)

acertou =False
enforcou=False
erros=0

while not acertou and not enforcou:

    tentativa= input("sugestao: ")
    
    for i,letra in enumerate(pReservada):
        if tentativa.upper() == letra.upper():
            palavra[i] = tentativa
    erros+=1

    acertou = not "_" in palavra
    enforcou = erros==5

    print(palavra)

if acertou==True:
    print('''
=============
Voce venceu
=============
''')
else:
    print('''
    =============
    Voce perdeu
    =============
    ''')
