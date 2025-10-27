import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    x0, y0 = [int(x) for x in input().split()]
    x1, y1 = [int(x) for x in input().split()]

    if x0 in [x1-1,x1,x1+1] and y0 in [y1-1,y1,y1+1]:
        if x0 == x1 or y0 == y1:
            print(0)
            return
        else:
            print(1)
            return

    is_turn_needed = (x0 != x1) and (y0 != y1)

    distances = sorted([abs(x0-x1), abs(y0-y1)])[::-1]

    answer = 0

    d0 = (distances[0] - 1) * 3
    d1 = max((distances[1] - 1) * 3, 0)

    answer = d0 + d1
    if is_turn_needed:
        answer += 1
    
    print(answer)
    
    


if __name__ == '__main__':
    main()
