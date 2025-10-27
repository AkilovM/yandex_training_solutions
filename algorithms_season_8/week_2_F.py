import sys

# junk = """
# 30
# .C.
# .W.
# WW.
# WWC
# .WC
# WW.
# ...
# .WC
# .WC
# CW.
# CWW
# CWC
# .WC
# CW.
# .WC
# .WC
# .WC
# WWC
# .WC
# .WC
# C.C
# CWC
# .WC
# CWC
# WW.
# C..
# CWC
# CWC
# CCW
# CWC
# """.split('\n')[1:-1]

# input_iter = iter(junk)

def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n = int(input())
    # n = int(next(input_iter))

    # agent_0 = 0
    # agent_1 = 0
    # agent_2 = 0
    agents = [0,0,0]

    remember_max_value = 0

    previous_row = '...'
    valid_cells = [True, True, True]

    for i in range(n):
        row = input()
        # row = next(input_iter)

        if row == 'WWW' and i == 0:
            break
        # print(row)
        # print(f'agents before {agents}')

        next_valid_cells = [False, False, False]

        can_we_go_further = False
        for idx in range(3):
            if previous_row[idx] != 'W':
                start_index = max(0, idx - 1)
                end_index = min(3, idx + 2)
                is_valid_cell = any(valid_cells[start_index:end_index])
                next_valid_cells[idx] = is_valid_cell
                if is_valid_cell:
                    if '.' in row[start_index:end_index] or 'C' in row[start_index:end_index]:
                        can_we_go_further = True
        
        if not can_we_go_further:
            break

        updated_agents = [0,0,0]

        for idx in range(3):
            if row[idx] == 'W':
                updated_agents[idx] = 0
            else:
                result = 0
                if row[idx] == 'C':
                    result += 1
                
                start_index = max(0, idx - 1)
                end_index = min(3, idx + 2)

                variants = [agents[x] for x in range(start_index, end_index) 
                            if previous_row[x] != 'W']
                # print(f'variants {variants}')
                variants.append(0)
                result += max(variants)
                updated_agents[idx] = result
        
        remember_max_value = max(remember_max_value, max(updated_agents))
        agents = updated_agents
        previous_row = row
        valid_cells = next_valid_cells

        # print(f'agents after {agents}')


    
    #print(max(agents))
    print(remember_max_value)



if __name__ == '__main__':
    main()
