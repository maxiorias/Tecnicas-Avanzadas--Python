import time
import matplotlib.pyplot as plt

## Fibonacci iterativo
def fibo_iterativo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b

## Fibonacci recursivo
def fibo_recursivo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibo_recursivo(n - 1) + fibo_recursivo(n - 2)

## Fibonacci memoización
def fibo_memo(n, memo={}):
    if n in memo:
        return memo[n]
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    memo[n] = fibo_memo(n - 1, memo) + fibo_memo(n - 2, memo)
    return memo[n]

### Fibonacci tabulación
def fibo_tabulacion(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    fib_valores = [0, 1] + [0] * (n + 1)
    for i in range(2, n + 1):
        fib_valores[i] = fib_valores[i - 1] + fib_valores[i - 2]
    return fib_valores[n]