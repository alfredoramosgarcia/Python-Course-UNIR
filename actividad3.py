
# EJERCICIO 1, 2 Y 3

import roman

class Numero:
    def __init__(self, num):
        self.num = num
        self.romano = roman.toRoman(num)
    def imprime(self):
        print(self.num, ' ' + self.romano)
        
    def suma_romano(self, cadena):
        aux = roman.fromRoman(cadena)
        self.num += aux
        self.romano = roman.toRoman(self.num)
    def isRoman(self, cadena):
        try:
            roman.fromRoman(cadena)
            return True
        except roman.InvalidRomanNumeralError:
            return False
        
numero = Numero(10)
numero.imprime()
numero.suma_romano('V')
numero.imprime()

print(numero.isRoman('y'))
        
        

# EJERCICIO 4 Y 5

class MejorNumero(Numero):
    
    def __init__(self, num):
        Numero.__init__(self, num)
        
    def resta_romano(self, cadena):
        aux = roman.fromRoman(cadena)
        self.num -= aux
        self.romano = roman.toRoman(self.num)
    
    def producto_romano(self, cadena):
        aux = roman.fromRoman(cadena)
        self.num *= aux
        self.romano = roman.toRoman(self.num)
        
    def suma_lista_romano(self, lista):
        for item in lista:
            try:
                if self.isRoman(item):
                    self.suma_romano(item)
                else:
                    raise TypeError(item + ' no es un numero romano')
            except TypeError as e:
                print(e)
                
                
lista = ['V', 'Y', 'X']

mejornumero = MejorNumero(10)

mejornumero.suma_lista_romano(lista)
mejornumero.imprime()
            


