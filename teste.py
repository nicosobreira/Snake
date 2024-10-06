def printLista(lista):
    for i in lista:
        print(i, end="")
    print()

lista = [1, 2, 3, 4, 5]
printLista(lista)
lista.insert(0, 0)
printLista(lista)
