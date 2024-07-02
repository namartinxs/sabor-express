senha_secreta = 525
senha_usuario = 0
while senha_secreta != senha_usuario:
    senha_usuario = int(input('Tente advinhar a minha senha, eu dúvido que você consiga.'))
    if senha_usuario == senha_secreta:
        print('Parabéns você acertou!')
        continue
    else:
        print('Você errou!')
        







