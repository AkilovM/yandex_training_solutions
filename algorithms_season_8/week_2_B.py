import sys

# junk = """
# RRRRRRLLBLRRBRLLLL
# """.split('\n')[1:-1]

# input_iter = iter(junk)

def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    rivers = input()
    # rivers = next(input_iter)
    
    answer = 0
    origin_len = len(rivers)
    rivers = rivers.replace('B', '')
    answer += origin_len - len(rivers)
    rivers = rivers.lstrip('R')
    rivers = rivers.rstrip('L')

    left_agent = 0
    right_agent = 1
    
    for char in rivers:
        if char == 'L':
            left_agent = min(left_agent + 1, right_agent + 1)
            right_agent = min(right_agent, left_agent + 1)
        elif char == 'R':
            right_agent = min(right_agent + 1, left_agent + 1)
            left_agent = min(left_agent, right_agent + 1)
        else:
            raise Exception('Wrong char!')
    answer += right_agent
    print(answer)


if __name__ == '__main__':
    main()
