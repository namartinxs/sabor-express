idade = int(input('Insira sua idade'))

if idade <=12:
    print('Pertence a categoria: criança.')
elif idade == 13 or idade<=18:
    print('Pertence a categoria: adolescente.')
else: 
    print('Pertence a categoria: adulto')