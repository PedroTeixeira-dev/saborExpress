import os

restaurantes = ['Petrus', 'QuiSabor']

def exibe_nome_do_programa():
    print("""
    ｓａｂｏｒ Ｅｘｐｒｅｓｓ
    """)
     
def exibir_opcoes():
    print('1. Cadastrar restaurante\n')
    print('2. Listar restaurante\n')
    print('3. Ativar restaurante\n')
    print('4. Sair\n')

def opcao_invalido():
    print('O valor digitado é inválido\n')
    input('Digite uma tecla para voltar ao menu principal  .')
    main()

def cadastrar_novo_restaurante():
    os.system('clear')
    print('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar:')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso\n')
    input('Digite uma tecla para voltar ao menu principal')
    main()

def listar_restaurantes():
    os.system('clear')
    print('Listando os restaurantes')

    for restaurante in restaurantes:
        print(f'- {restaurante}')
    
    input('Digite uma tecla para voltar ao menu principal')
    main()

def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        match opcao_escolhida:     
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                print('Ativar Restaurante\n')
            case 4:
                finalizar_app()
            case _:
                opcao_invalido()
    except:
        opcao_invalido()

def finalizar_app():
    os.system('clear')
    print('Finalizando o App\n')

def main():
     os.system('clear')
     exibe_nome_do_programa()
     exibir_opcoes()
     escolher_opcoes()

if __name__ == '__main__':
        main()