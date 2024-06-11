import os

jogos = [{'nome':'Csgo','categoria':'Plataforma', 'ativo': False},
         {'nome':'Mario','categoria':'Plataforma', 'ativo': True},
          {'nome':'lol','categoria':'RPG', 'ativo': False}]

def exibir_nome_do_programa():    
    print("""

░█████╗░░█████╗░██╗░░░░░███████╗░█████╗░░█████╗░░█████╗░  ██████╗░███████╗
██╔══██╗██╔══██╗██║░░░░░██╔════╝██╔══██╗██╔══██╗██╔══██╗  ██╔══██╗██╔════╝
██║░░╚═╝██║░░██║██║░░░░░█████╗░░██║░░╚═╝███████║██║░░██║  ██║░░██║█████╗░░
██║░░██╗██║░░██║██║░░░░░██╔══╝░░██║░░██╗██╔══██║██║░░██║  ██║░░██║██╔══╝░░
╚█████╔╝╚█████╔╝███████╗███████╗╚█████╔╝██║░░██║╚█████╔╝  ██████╔╝███████╗
░╚════╝░░╚════╝░╚══════╝╚══════╝░╚════╝░╚═╝░░╚═╝░╚════╝░  ╚═════╝░╚══════╝

░░░░░██╗░█████╗░░██████╗░░█████╗░░██████╗
░░░░░██║██╔══██╗██╔════╝░██╔══██╗██╔════╝
░░░░░██║██║░░██║██║░░██╗░██║░░██║╚█████╗░
██╗░░██║██║░░██║██║░░╚██╗██║░░██║░╚═══██╗
╚█████╔╝╚█████╔╝╚██████╔╝╚█████╔╝██████╔╝
░╚════╝░░╚════╝░░╚═════╝░░╚════╝░╚═════╝░
""")

def exibrit_opcoes():
    print('''1. Cadastra jogo ❣ (ɔ◔‿◔)ɔ ♥\n''')
    print('''2. Listar jogos ❣ (>‿◠)✌ ❣ \n''')
    print('''3. Aivar jogos ❣ (っ＾▿＾)💨 ❣ \n''')
    print('''4. Sair 👋≧◉ᴥ◉≦ \n''')

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def finalizar_app():
    os.system('cls')
    print('''Encerrando o progrma ❣ ( 👁️ ͜ʖ 👁️ )👎\n''')

def opcao_invalida():
    exibir_subtitulo('Opção inválida')
    input('Digite uma tecla para reiniciar: ')
    main()

def cadastra_novo_jogo():
    os.system('cls')
    exibir_subtitulo('Cadastro de jogo')
    nome_jogo = input('Digite o nome do jogo: ')
    categoria = input('Digite a categoria: ')
    dados_do_jogo = {'nome':nome_jogo, 'categoria':categoria, 'ativo':False}
    jogos.append(dados_do_jogo)
    input('Digite uma tecla para reiniciar: ')
    main()

def listar_jogos():
    os.system('cls')
    exibir_subtitulo('Listando os Jogos')
    for jogo in jogos:
        nome_do_jogo = jogo['nome']
        categoria_do_jogo = jogo['categoria']
        ativo_jogo = jogo['ativo']
        print(f' - {nome_do_jogo} | {categoria_do_jogo} | {ativo_jogo}')

    input('Digite uma tecla para reiniciar: ')
    main()

def alternar_estado_jogo():
    exibir_subtitulo('Modificar estado do jogo')
    nome_jogo = input('Digite o nome do jogo: ')
    for jogo in jogos:
        if nome_jogo == jogo['nome']:
            jogo['ativo'] = not jogo['ativo']
            if jogo['ativo']:
               print(f'O jogo {nome_jogo} está ativado')
            else:
                print(f'O jogo {nome_jogo} está desativado')  
    main()

def escolher_opcoes():
    try:
        opcao_escolhida = int(input('''Escolha uma opção ¯\_( ͡❛ ͜ʖ ͡❛)_/¯: '''))
        print(f'''Você escolheu a opção( ͡❛ ͜ʖ ͡❛)👌: {opcao_escolhida}''')

        if opcao_escolhida == 1:
            cadastra_novo_jogo()
        elif opcao_escolhida == 2:
            listar_jogos()
        elif opcao_escolhida == 3:
            print('''Ativar jogos ( 👁️ ͜ʖ 👁️ )\n''')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    exibir_nome_do_programa()
    exibrit_opcoes()
    escolher_opcoes()


if __name__ == '__main__':
    main()