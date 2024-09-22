# Medir tiempo de ejecución
def medir_tiempo(funcion, n, repeticiones=10):
    tiempos = []
    for _ in range(repeticiones):
        inicio = time.time()
        funcion(n)
        fin = time.time()
        tiempos.append((fin - inicio) * 1000)  # Convertir a milisegundos
    return sum(tiempos) / len(tiempos)

# Medir precisión
def verificar_precision(funciones, n):
    resultado_base = funciones[0](n)  # Tomamos como referencia la primera función
    for funcion in funciones[1:]:
        if funcion(n) != resultado_base:
            return False
    return True

# Definir los valores de n para la prueba
n_values = [10, 20, 30]

# Definir funciones a probar
funciones = [fibo_iterativo, fibo_recursivo, fibo_memo, fibo_tabulacion]
nombres_funciones = ["Iterativo", "Recursivo", "Memoización", "Tabulación"]

# Pruebas de precisión
print("Pruebas de Precisión:")
for n in n_values:
    if verificar_precision(funciones, n):
        print(f"Todas las implementaciones devuelven el mismo resultado para n = {n}.")
    else:
        print(f"¡Error! Diferentes resultados para n = {n}.")

# Pruebas de rendimiento
resultados_iterativo = []
resultados_recursivo = []
resultados_memoizacion = []
resultados_tabulacion = []

# Valores de n más grandes para rendimiento
n_rendimiento = [10, 20, 30]  # Puedes incluir valores más grandes como 100 si el rendimiento lo permite

print("\nPruebas de Rendimiento (tiempo en milisegundos):")
for n in n_rendimiento:
    tiempo_iterativo = medir_tiempo(fibo_iterativo, n)
    tiempo_recursivo = medir_tiempo(fibo_recursivo, n)
    tiempo_memoizacion = medir_tiempo(fibo_memo, n)
    tiempo_tabulacion = medir_tiempo(fibo_tabulacion, n)
    
    resultados_iterativo.append(tiempo_iterativo)
    resultados_recursivo.append(tiempo_recursivo)
    resultados_memoizacion.append(tiempo_memoizacion)
    resultados_tabulacion.append(tiempo_tabulacion)

    print(f"\nPara n = {n}:")
    print(f"Tiempo de Fibonacci Iterativo: {tiempo_iterativo:.4f} ms")
    print(f"Tiempo de Fibonacci Recursivo: {tiempo_recursivo:.4f} ms")
    print(f"Tiempo de Fibonacci Memoización: {tiempo_memoizacion:.4f} ms")
    print(f"Tiempo de Fibonacci Tabulación: {tiempo_tabulacion:.4f} ms")

# Gráficos de tiempo por cada función
plt.figure(figsize=(10, 12))

# Gráfico para Fibonacci Iterativo
plt.subplot(2, 2, 1)
plt.plot(n_rendimiento, resultados_iterativo, label='Iterativo', marker='o')
plt.xlabel('n')
plt.ylabel('Tiempo (ms)')
plt.title('Fibonacci Iterativo')
plt.grid()

# Gráfico para Fibonacci Recursivo
plt.subplot(2, 2, 2)
plt.plot(n_rendimiento, resultados_recursivo, label='Recursivo', marker='o', color='orange')
plt.xlabel('n')
plt.ylabel('Tiempo (ms)')
plt.title('Fibonacci Recursivo')
plt.grid()

# Gráfico para Fibonacci Memoización
plt.subplot(2, 2, 3)
plt.plot(n_rendimiento, resultados_memoizacion, label='Memoización', marker='o', color='green')
plt.xlabel('n')
plt.ylabel('Tiempo (ms)')
plt.title('Fibonacci Memoización')
plt.grid()

# Gráfico para Fibonacci Tabulación
plt.subplot(2, 2, 4)
plt.plot(n_rendimiento, resultados_tabulacion, label='Tabulación', marker='o', color='red')
plt.xlabel('n')
plt.ylabel('Tiempo (ms)')
plt.title('Fibonacci Tabulación')
plt.grid()

plt.tight_layout()
plt.show()
