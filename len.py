def largo(lista: list):
    n = 0
    return largo2(lista, n)

def largo2(lista, n):

    if len(lista) == 0: #basecase
        return n

    lista.pop()
    return largo2(lista, n+1)

lista = ["A", "B"]
print(largo(lista))

print(type([]))
