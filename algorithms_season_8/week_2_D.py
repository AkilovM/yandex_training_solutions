import sys

# junk = """
# xyzpqrstq
# 7
# p
# pqrstq
# rst
# stq
# xyz
# xyzpq
# zpq
# """.split('\n')[1:-1]

# input_iter = iter(junk)

def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    full_str = input()
    # full_str = next(input_iter)

    n = int(input())
    # n = int(next(input_iter))

    d = dict()
    unique_words = set()

    result = []

    for i in range(n):
        word = input()
        # word = next(input_iter)
        unique_words.add(word)
        first_letter = word[0]
        if first_letter not in d.keys():
            d[first_letter] = []
        d[first_letter].append(word)
    
    idx = 0
    considered_string = ''
    #guesses = []
    dynamic = {}

    def recursive(start):#, guess):
        #print(f'called recursive, start {start} guess {guess}')
        #print(f'called recursive, start {start} unique_words {unique_words}')
        if start in dynamic:
            return dynamic[start]
        if start == len(full_str):
            return []#guess

        considered_string = ''
        first_char = full_str[start]
        if first_char not in d.keys():
            dynamic[start] = None
            return

        for i in range(start, min(start + 20, len(full_str))):
            considered_string += full_str[i]
            #first_char
            #first_letter = considered_string[0]
            if considered_string in unique_words:
                next_words = recursive(i+1)
                if next_words is not None:
                    dynamic[start] = [considered_string] + next_words
                    return [considered_string] + next_words
        dynamic[start] = None
        return

    result = recursive(0)#, [])

    print(' '.join(result))


if __name__ == '__main__':
    main()
