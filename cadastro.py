import os
alunos = []

# Função para cadastra aluno
def cadastra_novo_aluno():
    os.system('cls')
    print('Cadastra novo aluno\n')
    nome_aluno = input('Digite o nome do aluno: ')
    idade_do_aluno = input('Digite a idade do aluno: ')
    nota_do_aluno = input('Digite a nota do alunno: ')
    cadastra_novo_aluno = {'nome': nome_aluno, 'idade do aluno': idade_do_aluno, 'nota do aluno': nota_do_aluno}
    alunos.append(cadastra_novo_aluno)

# Função para exibir alunos
def exibir_alunos():
    os.system('cls')
    print('''
█▀▀ ▄▀█ █▀▄ ▄▀█ █▀ ▀█▀ █▀█ █▀█   █▀▄ █▀▀   ▄▀█ █░░ █░█ █▄░█ █▀█ █▀
█▄▄ █▀█ █▄▀ █▀█ ▄█ ░█░ █▀▄ █▄█   █▄▀ ██▄   █▀█ █▄▄ █▄█ █░▀█ █▄█ ▄█\n''')
    for aluno in alunos:
        nome_do_aluno = aluno['nome']
        idade_do_aluno = aluno['idade do aluno']
        nota_do_aluno = aluno['nota do aluno']
        print(f'nome do aluno: {nome_do_aluno} | idade do aluno: {idade_do_aluno} | nota do aluno: {nota_do_aluno}')

# Função para exibir alunos para usuarios
def main():
    while True:
        opcao = input('Você quer cadastrar um aluno?\n Diite s para SIM e n para NÃO: ')
        if opcao == 's':
            cadastra_novo_aluno()
        elif opcao == 'n':
            exibir_alunos()
            break
            
# Função de iniciação do programa 
if __name__ == '__main__':
    main()