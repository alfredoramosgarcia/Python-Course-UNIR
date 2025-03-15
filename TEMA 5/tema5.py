# TEMA 5 ORGANIZACION DEL CODIGO

'''
Organizacion del codigo
-----------------------

    - Modulos: Cada uno de los ficheros .py de nuestro proyecto
    - Paquetes: 
'''


'''
Programacion orientada a objetos
--------------------------------


'''
# Clases

class Libro:
   
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def imprime(self):
        print(self.titulo + ' ' + self.autor)
        
    
    
libro2 = Libro('napoleaon', 'idk')
libro2.imprime()

# Herencia

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def cambiarNombre(self, nombre):
        self.nombre = nombre
    def imprime(self):
        print(self.nombre + ' ' + self.edad)
    
class Alumno(Persona):
    def __init__(self, nombre, edad, asignatura):
        Persona.__init__(self, nombre, edad)
        
        # Nuevos atributos
        
        self.asignatura = asignatura
        self.nota = None
        
    def calificar(self, calificacion):
        self.nota = calificacion
        
    def imprime(self):
        print(self.nombre + ' ', self.edad, ' ' + self.asignatura, self.nota)
        
alumno = Alumno('Alfredo', 25, 'Curso de python')

alumno.imprime()
alumno.calificar(10)
alumno.imprime()