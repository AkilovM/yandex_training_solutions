import sys

# junk = """
# 4
# 1 2 3 4
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

    # tables = [int(x) for x in next(input_iter).split()]
    tables = [int(x) for x in sys.stdin.readline().split()]

    left_idx = 0
    left_eaten = tables[0]

    right_idx = n-1
    right_eaten = tables[right_idx]

    min_difference = abs(left_eaten - right_eaten)
    best_left = left_idx
    best_right = right_idx

    while (right_idx - left_idx > 1):
        if min_difference == 0:
            break
        
        left_step_diff = abs(left_eaten + tables[left_idx + 1] - right_eaten)
        right_step_diff = abs(left_eaten - tables[right_idx - 1] - right_eaten)

        if left_step_diff < right_step_diff:
            left_idx += 1
            left_eaten += tables[left_idx]
        else:
            right_idx -= 1
            right_eaten += tables[right_idx]
        
        if abs(left_eaten - right_eaten) < min_difference:
            min_difference = abs(left_eaten - right_eaten)
            best_left = left_idx
            best_right = right_idx

    
    best_left += 1
    best_right += 1
    print(min_difference, best_left, best_right)


if __name__ == '__main__':
    main()
