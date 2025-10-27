import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    a,b,c,v0,v1,v2 = [float(x) for x in input().split()]
    # на ум приходят 5 возможных вариантов, посчитаем лучший
    results = []
    results.append(a/v0 + a/v1 + b/v0 + b/v1)
    results.append(a/v0 + c/v1 + b/v2)
    results.append(b/v0 + c/v1 + a/v2)
    results.append(a/v0 + c/v1 + c/v2 + a/v2)
    results.append(b/v0 + c/v1 + c/v2 + b/v2)

    #тест 4 не прошел
    results.append(a/v0 + a/v1 + a/v0 + c/v0 + c/v1 + a/v1)
    results.append(b/v0 + b/v1 + b/v0 + c/v0 + c/v1 + b/v1)
    results.append(a/v0 + c/v0 + c/v1 + a/v2)
    results.append(b/v0 + c/v0 + c/v1 + b/v2)

    best_result = min(results)
    print(best_result)


if __name__ == '__main__':
    main()
