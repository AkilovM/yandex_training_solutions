import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n, k = [int(x) for x in input().split()]
    unique_themes = set()
    tasks = input().split()
    answer = list()

    if k == n:
        print(' '.join(tasks))
        return

    if k == 1:
        print(tasks[0])
        return

    for i in range(n):
        task = tasks[i]
        tasks_we_need_to_take = k - len(answer)
        tasks_left = n - i
        if tasks_we_need_to_take == tasks_left:
            answer.append(task)
        elif task not in unique_themes:
            unique_themes.add(task)
            answer.append(task)
        if len(answer) == k:
            break
    print(' '.join(answer))




if __name__ == '__main__':
    main()
