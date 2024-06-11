# Importando um módulo
import math

# Usando listas para armazenar as médias
medias = []

# Função para calcular a média das notas
def calcular_media(notas):
   return sum(notas) / len(notas) if notas else 0

# Dicionário para armazenar as notas dos alunos
notas_dos_alunos = {}

# Usando input e while loop para coletar as notas dos alunos
quantidade_de_alunos = int(input("Digite a quantidade de alunos: "))
i = 0
while i < quantidade_de_alunos:
   nome = input("Digite o nome do aluno: ")
   notas = []
   nota = input("Digite uma nota do aluno (ou 'sair' para finalizar): ")

# Usando for loop e if/else/elif para processar as notas
   while nota.lower() != 'sair':
       if nota:
           try:
               nota_float = float(nota)
               if 0 <= nota_float <= 10:
                   notas.append(nota_float)
               else:
                   print("Nota deve ser entre 0 e 10.")
           except ValueError:
               print("Por favor, digite um número válido.")
       nota = input("Digite a próxima nota (ou 'sair' para finalizar): ")
   notas_dos_alunos[nome] = notas
   i += 1

# Usando for loop para calcular a média das notas
for aluno, notas in notas_dos_alunos.items():
   media = calcular_media(notas)
   medias.append(media)
   print(f"A média do(a) aluno(a) {aluno} é: {media:.2f}")

# Usando funções do módulo math
print(f"A média geral da turma é: {calcular_media(medias):.2f}")
print(f"A maior média é: {max(medias):.2f}")
print(f"A menor média é: {min(medias):.2f}")