import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n = int(input())
    mushrooms = input().split()
    vasya_mushrooms = [int(mushrooms[i]) for i in range(len(mushrooms)) if i % 2 == 0]
    masha_mushrooms = [int(mushrooms[i]) for i in range(len(mushrooms)) if i % 2 == 1]
    
    # тактика - подменяем худший гриб Васи на лучший гриб Маши
    worst_vasya_mushroom = min(vasya_mushrooms)
    best_masha_mushroom = max(masha_mushrooms)
    swap_gain = max([best_masha_mushroom - worst_vasya_mushroom, 0]) * 2
    vasya_hapiness = sum(vasya_mushrooms) - sum(masha_mushrooms) + swap_gain
    print(vasya_hapiness)
    return None


if __name__ == '__main__':
    main()
