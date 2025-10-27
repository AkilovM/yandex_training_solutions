import sys

# junk = """
# 5
# 1 2
# 1 3
# 2 4
# 2 5
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
    if n == 2:
        print(1)
        return
    elif n == 3:
        print(2)
        return
    
    neighbours = dict()

    # first_row = [int(x) for x in next(input_iter).split()]
    first_row = [int(x) for x in input().split()]
    neighbours[first_row[0]] = {first_row[1]}
    neighbours[first_row[1]] = {first_row[0]}

    #nodes_1_step_to_deadend = set()
    deadends = set()
    deadends.add(first_row[0])
    deadends.add(first_row[1])

    visited_nodes = set()


    for i in range(n-2):
        # row = [int(x) for x in next(input_iter).split()]
        row = [int(x) for x in input().split()]
        a, b = row
        # if b in neighbours.keys():
        #     a,b = b,a
        # neighbours[a].add(b)
        # neighbours[b] = {a}
        # deadends.discard(a)
        # deadends.add(b)

        for element in [a,b]:
            other_element = a if element == b else b
            if element not in neighbours.keys():
                neighbours[element] = {other_element}
                deadends.add(element)
            else:
                neighbours[element].add(other_element)
                deadends.discard(element)

    # print(f'deadends {deadends}')

    answer = 1
    while(True):
        new_deadends = set()
        for end in deadends:
            for neighbour in neighbours[end]:
                if neighbour not in visited_nodes:
                    if neighbour in deadends:
                        print((answer-1)*2 + 1)
                        return
                    if neighbour not in new_deadends:
                        new_deadends.add(neighbour)
                    else:
                        print(answer * 2)
                        return
            visited_nodes.add(end)
        deadends = new_deadends
        answer += 1
    print(answer)


if __name__ == '__main__':
    main()
