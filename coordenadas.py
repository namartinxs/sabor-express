x = float(input('Digite a cordena x:'))

y = float(input('Digite a cordena y:'))


if x > 0 and y > 0:
    print("O ponto pertence ao primeiro quadrante.")
elif x < 0 and y > 0:
    print("O ponto pertence ao segundo quadrante.")
elif x < 0 and y < 0:
    print("O ponto pertence ao terceiro quadrante.")
elif x > 0 and y < 0:
    print("O ponto pertence ao quarto quadrante.")
else:
    print("O ponto está sobre um eixo ou na origem.")
