class Banco:
    def __init__(self, nombre, id):
        self.nombre= nombre
        self.id= id
        self.__saldo= 0
    
    def depositar(self, cantidad):
        self.__saldo+= cantidad
    
    def canjear(self, cantidad):
        if cantidad < self.__saldo:
            self.__saldo-= cantidad
        else:
            print("No hay saldo suficiente")
            print(f"Tu saldo es de: {self.__saldo}")

    def status(self):
        print(">>###########<<")
        print("Mostrando Cuenta y sus datos:")
        print("------------------------")
        print(f"Nombre: {self.nombre}")
        print("------------------------")
        print(f"ID: {self.id}")
        print("------------------------")
        print(f"Saldo: {self.__saldo}")
        

user_1= Banco("Pepe", 1)
user_2= Banco("Alejandro", 2)

user_1.depositar(100)
user_2.depositar(500)

user_1.status()
user_2.status()

user_1.canjear(120)
user_2.canjear(120)

user_1.status()
user_2.status()
