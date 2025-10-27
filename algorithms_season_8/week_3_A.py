import sys

# junk = """
# 1 1 1
# """.split('\n')[1:-1]

# input_iter = iter(junk)

def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    # a, b, s = [int(x) for x in next(input_iter).split()]
    a, b, s = [int(x) for x in input().split()]
    # L = -1

    answers = []

    ab_area = a*b
    # bot_area = ab_area / b * L
    # top_area = ab_area / a * L

    # full_area = L * L
    # unknown_area = full_area - s - ab_area
    # unknown_area = b * (L-a) + a * (L-b)
    # unknown_area = ab_area / b * L + ab_area / a * L

    # L * L = ab_area / b * L + ab_area / a * L + s + ab_area
    # L**2 + L*(-ab_area/b - ab_area/a) + (-s - ab_area) = 0

    # L**2 = L*(a+b) - a*b + s
    # L**2 + L*(-a-b) + a*b - s = 0

    #discr = (-ab_area/b - ab_area/a)**2 - 4*(-s - ab_area)
    discr = (-a-b)**2 - 4*(a*b - s)
    # print(f'discr {discr}')
    if discr < 0:
        print(-1)
        return
    elif discr == 0:
        answers.append(-(-ab_area/b - ab_area/a)/2)
    else:
        answers.append((-(-ab_area/b - ab_area/a)-discr**(1/2))/2)
        answers.append((-(-ab_area/b - ab_area/a)+discr**(1/2))/2)
    answers = sorted(answers)
    # print(f'answers {answers}')

    if answers[-1] > a and answers[-1] > b and answers[-1] % 1 == 0:
        print(int(answers[-1]))
    else:
        print(-1)
    return


if __name__ == '__main__':
    main()
