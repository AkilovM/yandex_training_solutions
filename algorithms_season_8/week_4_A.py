import sys
import bisect

# junk = """
# 2
# 10:10-10:11
# 10:10-10:11
# 2
# 10:11-10:12
# 10:11-10:12
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

    a_departs = []
    a_arrives = []
    b_departs = []
    b_arrives = []

    for i in range(n):
        # row = next(input_iter)
        row = input()

        a_dep, b_arr = [int(x) for x in row.replace(':', '0').split('-')]
        bisect.insort_right(a_departs, a_dep) #a_departs.append(a_dep)
        bisect.insort_right(b_arrives, b_arr)
    
    # m = int(next(input_iter))
    m = int(input())

    for i in range(m):
        # row = next(input_iter)
        row = input()

        b_dep, a_arr = [int(x) for x in row.replace(':', '0').split('-')]
        bisect.insort_right(b_departs, b_dep) #b_departs.append(b_dep)
        bisect.insort_right(a_arrives, a_arr)
    
    a_dep_idx = 0
    a_arr_idx = 0
    b_dep_idx = 0
    b_arr_idx = 0

    a_busses_ready = 0
    b_busses_ready = 0

    total_busses = 0

    while (
       a_dep_idx < len(a_departs) or a_arr_idx < len(a_arrives) 
    or b_dep_idx < len(b_departs) or b_arr_idx < len(b_arrives)
        ):

        min_values = []

        min_values.append(a_departs[a_dep_idx] if a_dep_idx < len(a_departs) else 999999)
        min_values.append(a_arrives[a_arr_idx] if a_arr_idx < len(a_arrives) else 999999)
        min_values.append(b_departs[b_dep_idx] if b_dep_idx < len(b_departs) else 999999)
        min_values.append(b_arrives[b_arr_idx] if b_arr_idx < len(b_arrives) else 999999)

        min_value = min(min_values)

        if a_arr_idx < len(a_arrives):
            if a_arrives[a_arr_idx] == min_value:
                a_busses_ready += 1
                a_arr_idx += 1

        if b_arr_idx < len(b_arrives):
            if b_arrives[b_arr_idx] == min_value:
                b_busses_ready += 1
                b_arr_idx += 1
        
        if a_dep_idx < len(a_departs):
            if a_departs[a_dep_idx] == min_value:
                if a_busses_ready == 0:
                    total_busses += 1
                    a_busses_ready += 1
                a_busses_ready -= 1
                a_dep_idx += 1
        
        if b_dep_idx < len(b_departs):
            if b_departs[b_dep_idx] == min_value:
                if b_busses_ready == 0:
                    total_busses += 1
                    b_busses_ready += 1
                b_busses_ready -= 1
                b_dep_idx += 1
    
    print(total_busses)


if __name__ == '__main__':
    main()
