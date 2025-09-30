#enunciado:
#Una persona tiene un nombre, dos apellidos, una fecha de nacimiento, un sexo y un número de identificación.
#Define las clases y los atributos correspondientes

class Persona:
    def __init__(self,nombre, apellido1, apellido2, fecha_nacimiento, sexo, num_id):
        self.__nombre = nombre
        self.__apellido1 = apellido1
        self.__apellido2 = apellido2
        self.__fecha_nacimiento = fecha_nacimiento
        self.__sexo = sexo
        self.__num_id = num_id

    #GETTERS
    def get_nombre(self):   
            return self.__nombre
    def get_apellido1(self):
            return self.__apellido1
    def get_apellido2(self):
            return self.__apellido2
    def get_fecha_nacimiento(self):
            return self.__fecha_nacimiento
    def get_sexo(self):
            return self.__sexo
    def get_num_id(self):
            return self.__num_id
        
    #SETTERS
    def set_nombre(self,nombre):
            self.__nombre = nombre
    def set_apellido1(self,apellido1):
            self.__apellido1 = apellido1
    def set_apellido2(self,apellido2):
            self.__apellido2 = apellido2
    def set_fecha_nacimiento(self,fecha_nacimiento):
            self.__fecha_nacimiento = fecha_nacimiento
    def set_sexo(self,sexo):
            self.__sexo = sexo
    def set_num_id(self,num_id):
            self.__num_id = num_id


    #comportamientos o metodos (funciones)
    def saludar(self):
        return f"Hola, me llamo {self.__nombre} {self.__apellido1} {self.__apellido2}, encantado."
    def despedirse(self,otra_persona):
        return f"Adiós {otra_persona}, ha sido un placer conocerte."
    def cumpleaños(self):
        return f"Feliz cumpleaños {self.__nombre} {self.__apellido1} {self.__apellido2}!"
           


    #representacion en cadena
    def __str__(self):
        return f"{self.__nombre} se apellida {self.__apellido1} {self.__apellido2}, su fecha de nacimiento es: {self.__fecha_nacimiento}, Sexo: {self.__sexo}, ID: {self.__num_id}"

     