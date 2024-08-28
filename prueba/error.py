miLista = [1, 2, 3, 4, 5]

def lista():
    try:
        return miLista[7] 
    except IndexError:
        return "El índice no está en la lista"

print(lista())
