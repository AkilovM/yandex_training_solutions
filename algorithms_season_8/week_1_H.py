import sys

# junk = """
# 12 3
# cabacaqwerty
# erty
# caba
# caqw
# """.split('\n')[1:-1]

# junk = """
# 16 4
# cabacaqwertycaqw
# erty
# caba
# caqw
# caqw
# """.split('\n')[1:-1]

# input_iter = iter(junk)

def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n, m = [int(x) for x in input().split()]
    # n, m = [int(x) for x in next(input_iter).split()]

    full_str = input()
    # full_str = next(input_iter)
    cut_len = int(n // m)

    cut_index_dict = dict()

    for i in range(m):
        cut = input()
        # cut = next(input_iter)
        #cut_index_dict[cut] = i+1

        if cut not in cut_index_dict.keys():
            cut_index_dict[cut] = set()
        #cut_index_dict[cut] = cut_index_dict.get(cut, set()).add(i+1)
        cut_index_dict[cut].add(i+1)
    
    answer = []

    for i in range(m):
        cut = full_str[i*cut_len:(i+1)*cut_len]
        #answer.append(str(cut_index_dict[cut]))
        answer.append(str(cut_index_dict[cut].pop()))

    print(' '.join(answer))


if __name__ == '__main__':
    main()
