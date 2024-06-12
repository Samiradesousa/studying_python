class Animal:
   def __init__(self, nome):
       self.nome = nome  # Atributo
   def falar(self):  # Método
       pass
class Cachorro(Animal):  # Herança
   def falar(self):  # Polimorfismo
       return "Au Au!"
# Encapsulamento: nome é um atributo privado, não acessível diretamente
class Gato(Animal):
   def __init__(self, nome):
       self.__nome = nome
   def falar(self):
       return "Miau!"
# Criando objetos
dog = Cachorro("Rex")
cat = Gato("Mingau")
# Usando métodos
print(dog.falar())  # Saída: Au Au!
print(cat.falar())  # Saída: Miau!