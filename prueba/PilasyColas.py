fila = ["jose", "maria", "raul", "paola"]

print("Antes de borrar la tercera persona:")

for i in range(len(fila)):
    print(f"{i+1}.- {fila[i]}")

fila.pop(2) 

print("\nDespués de borrar la tercera persona:")