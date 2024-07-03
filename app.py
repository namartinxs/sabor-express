import os

restaurantes = ['Capitão Xis', 'Açai do Careca'] #global 

def exibir_nome_do_programa():
 print("""𝕊𝕒𝕓𝕠𝕣 𝕖𝕩𝕡𝕣𝕖𝕤𝕤

 """)

def exibir_opcoes(): 
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando o app...')


def voltar_menu_principal():
    input('\n Digite uma tecla para voltar ao menu principal. ')
    main()

def exibir_subtitulo(msg):
    os.system('cls')
    print(msg)
    print()

def opcao_invalida():
    print('Opcao Inválida')
    voltar_menu_principal()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'{nome_do_restaurante} cadastrado com sucesso.')
    voltar_menu_principal()
    

def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes...')

    for restaurante in restaurantes:
        print (f'- {restaurante}')

    voltar_menu_principal()

def escolher_opcao():
    try:
        
        opcao_escolhida = int(input('Esolha uma opção:'))
        if opcao_escolhida == 1:
           cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('3. Ativar restaurante')
        elif opcao_escolhida == 4 :
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()



def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()