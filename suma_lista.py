resultado = []
def sumatorio_lista(lista: list):
    n = 0
    items_in_list = len(lista)
    return sumatorio_lista2(lista, n, items_in_list)


def sumatorio_lista2(lista, n:int, items_in_list):
        if n == items_in_list:
            return #basecase
        
        if type(lista[n]) == "list":
            sumatorio = sum(lista[n])
            resultado.append(sumatorio)
            return sumatorio_lista2(lista, n+1, items_in_list)

        else:
            resultado.append(lista[n])
            return sumatorio_lista2(lista, n+1, items_in_list)


lista_numeros = [2, 3, 4, [2, 3]]
print(sumatorio_lista(lista_numeros), resultado)