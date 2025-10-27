import sys

# junk = """
# 2 2
# 1 2
# 7
# 3 0
# 3 1
# 2
# 3 0
# 1 3
# 3 0
# 3 1
# """.split('\n')[1:-1]

# input_iter = iter(junk)

class McDonalds_Queue:
    def __init__(self, initial_queue, hunger_treshold):
        self.all_guys_list = initial_queue
        self.first_guy = self.all_guys_list[0]
        self.last_guy = self.all_guys_list[-1]
        self.guys_served = 0
        self.REALLY_HUNGRY_guys_served = 0
        self.hunger_treshold = hunger_treshold
    
    def serve_first_guy(self):
        if self.first_guy['am_i_really_hungry']:
            self.REALLY_HUNGRY_guys_served += 1
        self.guys_served += 1
        if self.guys_served == len(self.all_guys_list):
            self.first_guy = -1
        else:
            self.first_guy = self.all_guys_list[self.guys_served]
    
    def add_last_guy(self, hunger):
        am_i_really_hungry = hunger >= self.hunger_treshold
        hungry_guys_counted = self.last_guy['really_hungry_guys_including_me']
        if am_i_really_hungry:
            hungry_guys_counted += 1
        new_guy = {
            'am_i_really_hungry': am_i_really_hungry,
            'really_hungry_guys_including_me': hungry_guys_counted
        }
        self.all_guys_list.append(new_guy)
        self.last_guy = self.all_guys_list[-1]
        if self.first_guy == -1:
            self.first_guy = self.last_guy
    
    def masha_asks(self, n_first_guys):
        if n_first_guys == 0:
            #print('masha, what the hell ??')
            print(0)
        else:
            index_of_her_last_guy = self.guys_served + n_first_guys - 1
            answer = self.all_guys_list[index_of_her_last_guy]['really_hungry_guys_including_me'] - self.REALLY_HUNGRY_guys_served
            print(answer)


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    # n = int(next(input_iter))
    # n = int(input())

    # n, hunger_treshold = [int(x) for x in next(input_iter).split()]
    n, hunger_treshold = [int(x) for x in sys.stdin.readline().split()]

    # initial_queue = [int(x) for x in next(input_iter).split()]
    initial_queue = [int(x) for x in sys.stdin.readline().split()]

    first_guy_hunger = initial_queue[0] >= hunger_treshold
    really_hungry_first_counter = 1 if first_guy_hunger else 0
    first_guy = {
        'am_i_really_hungry': first_guy_hunger,
        'really_hungry_guys_including_me': really_hungry_first_counter
    }

    one_guy_queue = [first_guy]

    mcdonals = McDonalds_Queue(one_guy_queue, hunger_treshold)

    for i in range(1, n):
        mcdonals.add_last_guy(initial_queue[i])

    # m = int(next(input_iter))
    m = int(input())

    for i in range(m):
        # row = [int(x) for x in next(input_iter).split()]
        row = [int(x) for x in sys.stdin.readline().split()]

        operation = row[0]

        if operation == 1:
            mcdonals.add_last_guy(row[1])
        elif operation == 2:
            mcdonals.serve_first_guy()
        elif operation == 3:
            mcdonals.masha_asks(row[1])

if __name__ == '__main__':
    main()
