import sys
import bisect

# junk = """
# 5
# 0 24
# 100 35
# 150 50
# 200 75
# 250 150
# 5
# 107
# 143
# 152
# 170
# 150
# """.split('\n')[1:-1]

# input_iter = iter(junk)

def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    # n = int(next(input_iter))
    n = int(input())

    power_levels = []
    power_taxes = dict()

    for i in range(n):
        # power, tax = [int(x) for x in next(input_iter).split()]
        power, tax = [int(x) for x in sys.stdin.readline().split()]
        
        power_levels.append(power)
        power_taxes[power] = tax

    # m = int(next(input_iter))
    m = int(input())

    for i in range(m):
        # car_power = int(next(input_iter))
        car_power = int(input())

        answer = 0

        binary_searched_index = bisect.bisect_left(power_levels, car_power)
        if binary_searched_index == 0:
            raise Exception('expected car_power >= 1')
        elif binary_searched_index >= len(power_levels):
            answer = car_power * power_taxes[power_levels[-1]]
        else:
            answer = car_power * power_taxes[power_levels[binary_searched_index-1]]
        
        print(answer)


if __name__ == '__main__':
    main()
