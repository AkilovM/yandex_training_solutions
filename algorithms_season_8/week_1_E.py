import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n, k = [int(x) for x in input().split()]

    if k == 0:
        print(n)
        return

    if n % 10 == 0:
        print(n)
        return
    
    if n % 10 == 5:
        n += 5
        print(n)
        return
    
    if n % 10 in [1,3,7,9]:
        n += n % 10
        k -= 1
    
    if k // 4 >= 1:
        how_many_times_add_twenty = k // 4 # 2+4+6+8=20
        n += 20 * how_many_times_add_twenty
        k -= 4 * how_many_times_add_twenty

    for i in range(k):
        n += n % 10
        # if n % 10 == 0:
        #     break
    print(n)


if __name__ == '__main__':
    main()
