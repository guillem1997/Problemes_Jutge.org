def absValue(x):
    if x > 0:
        result = x
    else:
        result = -x
    return result


def power(x, p):
    result = x**p
    return result


def isPrime(x):
    is_Prime = True
    if x < 2:
        is_Prime = False
    for number in range(2, x):
        if x % number == 0:
            is_Prime = False
            break
    return is_Prime


def slowFib(n):
    if n == 0 or n == 1:
        return n
    return slowFib(n-1) + slowFib(n-2)


def quickFib(n):
    secuencia = []
    if n < 2:
        return n
    else:
        secuencia = [0, 1]
        for i in range(2, n+1):
            count = i
            secuencia.append(secuencia[i - 1] + secuencia[i - 2])
    return secuencia[count]
