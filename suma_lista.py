
def sumatorio_lista(lista: list):
    n = 0
    r = 0
    items_in_list = len(lista)
    return sumatorio_lista2(lista, n, items_in_list, r)


def sumatorio_lista2(lista, n:int, items_in_list, r):
        if n == items_in_list:
            return r #basecase
        
        if isinstance(lista[n], list):
            for i in range(len(lista[n])):
                r = r + i
            return sumatorio_lista2(lista, n+1, items_in_list, r)

        else:
            r = lista[n] + r
            return sumatorio_lista2(lista, n+1, items_in_list, r)


lista_numeros = [2, 3, 4, [2, 3]]
print(sumatorio_lista(lista_numeros))