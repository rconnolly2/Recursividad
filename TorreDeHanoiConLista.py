principio_lista = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
medio_lista = []
final_lista = []




def Torre_De_Hanoi(principio, medio, final):
    numero_discos = len(principio)
    return Torre_De_Hanoi2(numero_discos, principio, medio, final)

def Torre_De_Hanoi2(numero_discos, principio, medio, final):
    if numero_discos == 1:
        valor = principio.pop(-1)
        final.append(valor)
    else:
        Torre_De_Hanoi2(numero_discos-1, principio, final, medio)
        valor = principio.pop(-1)
        final.append(valor)
        Torre_De_Hanoi2(numero_discos-1, medio, principio, final)


Torre_De_Hanoi(principio_lista, medio_lista, final_lista)
print(principio_lista, medio_lista, final_lista)