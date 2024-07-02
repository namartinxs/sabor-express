import os

def exibir_nome_do_programa():
 print("""𝕊𝕒𝕓𝕠𝕣 𝕖𝕩𝕡𝕣𝕖𝕤𝕤

 """)

def exibir_opcoes(): 
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    os.system('cls')
    print('Finalizando o app')

def escolher_opcao():
    opcao_escolhida = int(input('Esolha uma opção:'))
    match opcao_escolhida:
        case 1:
            print('1. Cadastrar restaurante')
        case 2:
            print('2. Listar restaurante')
        case 3:
            print('3. Ativar restaurante')#cadastrado na base mas fora de visualização
        case 4: 
            finalizar_app()
        case _:
            print('op inválida')

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()