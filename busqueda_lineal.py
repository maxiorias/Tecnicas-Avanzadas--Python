lista = [1,2,4,5,7,8];
n = len(lista);
print(lista);
objetivo = 5
for i in range(n-1):
    if lista[i] == objetivo:
        print(f"El elemento {objetivo} se encuentra en la posición {i}"); 
        break;

