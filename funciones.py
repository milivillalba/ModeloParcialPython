#PARA DEFINIR FUNCIONES EN PYTHON SE USA "def" SEGUIDO
# DEL NOMBRE DE LA FUNION Y UN PRENTESIS DONDE SE COLOCAN LOS ARGUMENTOS SEPARADOS

def saluda (nombre):
    s= "Hola " + nombre + ", bienvenido."
    return s

print(saluda("MILI"))

#las funciones en python pueden retornar mas de un valo solo se debe sparar por coma
def calcular_suma (a , b):
    suma = a+b
    resta= a-b
    return "SUMA:",suma," Resta:", resta
print(calcular_suma(10,5))

# "*"Indica que se pasan una cantidad de parametros indefinidos.
def promedio(*numeros):
    suma= 0
    k= 0
    for n in numeros:
        suma= suma+n
        k = k+1
    return suma/k
print(promedio(2,4,6,8,10))

#CADENA DE CARACTER MULTILINEA
cadena_multilinea="""
se ven facherito
"""
type(cadena_multilinea)

#recorrer una cadena