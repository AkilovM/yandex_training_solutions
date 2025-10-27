import sys

# junk = """
# 2 6
# XX....
# .XXXXX
# """.split('\n')[1:-1]

# input_iter = iter(junk)

def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n, k = [int(x) for x in input().split()]
    # n, k = [int(x) for x in next(input_iter).split()]

    X_horiz = 0
    O_horiz = 0

    X_vert = [0] * k
    O_vert = [0] * k

    X_right_down = [0] * (k)
    O_right_down = [0] * (k)

    X_left_down = [0] * (k)
    O_left_down = [0] * (k)

    incrementing_index = 0
    decreasing_index = 0 # k - 1 - 5

    for i in range(n):
        row = input()
        # row = next(input_iter)

        X_horiz = 0
        O_horiz = 0

        right_down_index_to_clear = 0 - (incrementing_index % k)
        X_right_down[right_down_index_to_clear] = 0
        O_right_down[right_down_index_to_clear] = 0

        left_down_index_to_clear = -1 + (incrementing_index % k)
        X_left_down[left_down_index_to_clear] = 0
        O_left_down[left_down_index_to_clear] = 0

        for char_idx in range(k):
            char = row[char_idx]
            left_shifting_index = (char_idx - (incrementing_index % k))
            right_shifting_index = (char_idx + (incrementing_index % k)) % k
            if char == '.':
                X_horiz = 0
                O_horiz = 0
                X_vert[char_idx] = 0
                O_vert[char_idx] = 0
                
                #if char_idx < k - 5:
                X_right_down[left_shifting_index] = 0
                O_right_down[left_shifting_index] = 0

                # if char_idx >= 4:
                X_left_down[right_shifting_index] = 0
                O_left_down[right_shifting_index] = 0

            elif char == 'X':
                X_horiz += 1
                O_horiz = 0
                X_vert[char_idx] += 1
                O_vert[char_idx] = 0

                # if char_idx < k - 5:
                X_right_down[left_shifting_index] += 1
                O_right_down[left_shifting_index] = 0

                # if char_idx >= 4:
                X_left_down[right_shifting_index] += 1
                O_left_down[right_shifting_index] = 0

            elif char == 'O':
                X_horiz = 0
                O_horiz += 1
                X_vert[char_idx] = 0
                O_vert[char_idx] += 1

                # if char_idx < k - 5:
                X_right_down[left_shifting_index] = 0
                O_right_down[left_shifting_index] += 1

                # if char_idx >= 4:
                X_left_down[right_shifting_index] = 0
                O_left_down[right_shifting_index] += 1
            
            if (X_horiz == 5 or O_horiz == 5):
                print('Yes')
                return

        if (   5 in X_vert
            or 5 in O_vert
            or 5 in X_right_down
            or 5 in O_right_down
            or 5 in X_left_down
            or 5 in O_left_down
            ):
            print('Yes')
            return

        incrementing_index += 1
        decreasing_index -= 1

    print('No')


if __name__ == '__main__':
    main()
