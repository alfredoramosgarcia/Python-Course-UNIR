import math

def perimetro(lado, num_lados):
    return num_lados * lado

def area(lado, num_lados):
    apotema = lado / (2 * math.tan(math.pi / num_lados))
    perimetro = perimetro(lado, num_lados)
    return (perimetro * apotema) / 2