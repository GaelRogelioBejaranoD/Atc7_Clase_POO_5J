print("Programación POO")
# Definicion de clases
class Perro:
    # Funciones dentro de la clase
    def morder(self):
        print("El perro me mordió")
    def Datos_Perro(self,nombre,edad):
        print(f" Nombre : {nombre} \n Edad : {edad}")

# Zona de creacion de objetos
pitbull=Perro()

# Zona de uso de objetos 

pitbull.Datos_Perro("Boby",4)
pitbull.morder()



