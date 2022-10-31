from ast import Str


def TorreDeHanoi(n, principio, final, intermedio):
    if n == 1:
        print("Mueve primer disco de", principio, " a ", final) # basecase
    else:
        TorreDeHanoi(n-1, principio, intermedio, final)
        print("Moviendo disco: " + str(n) + " desde: "+ principio + " a " + final)
        TorreDeHanoi(n-1, intermedio, final, principio)




TorreDeHanoi(2, "A", "C", "B")

