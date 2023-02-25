
class persona:
    def __init__(self, nombre, edad, dni):
        self.nombre =nombre
        self.edad =edad
        self.dni = dni
    def mayor_edad(self):
        if self.edad <= 18 :
            return False
        else :
            return True
miguel = persona("miguel",20,13754850)
es_mayor = miguel.mayor_edad()
print(es_mayor) 
#  nombre, apellido, edad, salario
class empledo:
    def __init__(self, nombre, apellido, edad, salario):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.salario= salario
    def nombre_completo(self):
       lista_nombres = self.nombre.split(" ")
       
       return lista_nombres
