def combinacion_congruencial(n, a, m, seeds):
    """
    Genera una secuencia de números aleatorios utilizando el método del generador de congruencia lineal combinada.
    """
    k = len(seeds)
    numbers = [0] * n
    numbers[:k] = seeds

    for i in range(k, n):
        xi = 0
        for j in range(k):
            xi += a[j] * numbers[i - j - 1]
        numbers[i] = xi % m

    return numbers

# Generar 10 números aleatorios con semillas 123, 456 y 789
seeds = [123, 456, 789]
a = [13, 23, 29]
m = 1000
numbers = combinacion_congruencial(n=10, a=a, m=m, seeds=seeds)

print(numbers)