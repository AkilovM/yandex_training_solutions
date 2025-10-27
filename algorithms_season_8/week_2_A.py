import sys

# junk = """
# 5
# """.split('\n')[1:-1]

# input_iter = iter(junk)

def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n = int(input())
    # n = int(next(input_iter))
    fibonacci_but_trio = [1]
    for i in range(n):
        start_index = max(0,i-2)
        end_index = i + 1
        fibonacci_but_trio.append(sum(fibonacci_but_trio[start_index:end_index]))
    print(fibonacci_but_trio[-1])
    #print(fibonacci_but_trio)


if __name__ == '__main__':
    main()
