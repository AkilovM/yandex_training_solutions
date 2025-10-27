import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    password = list(input())
    letters_counts = dict()

    answer = 1

    for i in range(len(password)):
        letter = password[i]
        letters_encountered = i + 1
        letters_counts[letter] = letters_counts.get(letter,0) + 1
        answer += letters_encountered - letters_counts[letter]
    
    print(answer)
    #print(letters_counts)


if __name__ == '__main__':
    main()
