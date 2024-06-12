#Classe base
class Veiculo:
   def __init__(self, marca, modelo):
       self.marca = marca
       self.modelo = modelo
   def acelerar(self):
       return "Vrumm!"
# Subclasse que herda de Veiculo
class Carro(Veiculo):
   def __init__(self, marca, modelo, portas):
       super().__init__(marca, modelo)
       self.portas = portas  # Atributo específico da subclasse
   # Polimorfismo: Sobrescrevendo o método acelerar
   def acelerar(self):
       return super().acelerar() + " Vrumm Vrumm!"
# Encapsulamento: Atributos privados com métodos públicos para acessá-los
class Moto(Veiculo):
   def __init__(self, marca, modelo, cilindradas):
       super().__init__(marca, modelo)
       self.__cilindradas = cilindradas  # Atributo privado
   def getCilindradas(self):
       return self.__cilindradas
# Instanciando objetos
carro = Carro("Toyota", "Corolla", 4)
moto = Moto("Honda", "CB500", 500)
# Usando métodos
print(carro.acelerar())  # Saída: Vrumm Vrumm!
print(moto.getCilindradas())  # Saída: 500