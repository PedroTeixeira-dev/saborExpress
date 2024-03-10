import os

restaurantes = [
    {
    'nome': 'Praça',
    'categoria': 'Japonesa',
    'ativo': False
    }, 
    {
    'nome': 'Pizza Suprema',
    'categoria': 'Pizza',
    'ativo': True
    },
    {
        'nome': 'cantina',
    'categoria': 'Italiana',
    'ativo': False
    }
    ]

def exibe_nome_do_programa():
    print("""
    ｓａｂｏｒ Ｅｘｐｒｅｓｓ
    """)
     
def exibir_opcoes():
    print('1. Cadastrar restaurante\n')
    print('2. Listar restaurante\n')
    print('3. Alternar estado do restaurante\n')
    print('4. Sair\n')

def voltar_ao_menu_principal():
    input('Digite uma tecla para voltar ao menu principal  ')
    main()

def opcao_invalido():
    print('O valor digitado é inválido\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('clear')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print('\n')

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar:')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes')

    print(f'{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | Staus')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o estado do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

        
    voltar_ao_menu_principal()

def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        match opcao_escolhida:     
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alternar_estado_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalido()
    except:
        opcao_invalido()

def finalizar_app():
    exibir_subtitulo('Finalizando o App')

def main():
     os.system('clear')
     exibe_nome_do_programa()
     exibir_opcoes()
     escolher_opcoes()

if __name__ == '__main__':
        main()