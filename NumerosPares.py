

#Dime los numeros pares inferiores a 8

def NumerosPares(numero: int):
    print(numero)

    if not (numero/2) == int(numero/2) or numero == 0:
        return "Numero no es par!"
        

    if (numero == 2):
        return numero # final de recursion
    else:
        return NumerosPares(numero-2)

print(NumerosPares(5))

