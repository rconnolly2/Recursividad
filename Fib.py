def fibonacci(numero: int):
    if numero == 0 or numero == 1:
        return numero #basecase

    return fibonacci(numero-1)+fibonacci(numero-2) #https://es.wikipedia.org/wiki/Sucesi%C3%B3n_de_Fibonacci#Definici%C3%B3n_recurrente


print(fibonacci(3))