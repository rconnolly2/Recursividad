

from array import array
from ast import Num


def ConseguirFactorial(numero):
    if numero <= 1:
        return numero # Baseline Aqui es donde devolvemos el ULTIMO return que se concatenan con los returns anteriores
    elif (numero > 1):
        return numero * ConseguirFactorial(numero-1)


def PrintNumerosPares(numero: int):
    if numero == 2:
        return numero #basecase
    if numero == 0:
        print("Numero no es par")

    if (numero/2) == int(numero/2):
        print(numero)
        return PrintNumerosPares(numero-1)
    else:
        return PrintNumerosPares(numero-1)


def ReturnNumerosPares(numero: int, lista_resutado: list):
    if numero == 0:
        print("0 no es un numero par")
    if numero == 2:
        lista_resutado.append(numero)
        return None #basecase
    if numero/2 == int(numero/2):
        # Es un numero par y recursividad concatenando returns
        lista_resutado.append(numero)
        return ReturnNumerosPares(numero-2, lista_resutado)

print(ConseguirFactorial(5))
print((8/2) == int(8/2))
print(PrintNumerosPares(8))

lista_pares = []
ReturnNumerosPares(8, lista_pares)
print(lista_pares)
