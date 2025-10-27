import sys


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n = int(input())
    #dynamic = dict()

    if n < 3:
        print(1)
        return
    
    cubes_required_per_stage = []
    i = 1
    increment = 2
    while i <= n:
        #print(i)
        cubes_required_per_stage.append(i)
        i += increment
        increment += 1
        #possible_stages += 1

    #print(cubes_required_per_stage)

    variants_per_n = {
        '1': 1,
        '2': 1,
        '3': 2
    }

    def recursive(cubes, lower_width):
        case_hash = f'{cubes}_{lower_width}'
        if case_hash in variants_per_n.keys():
            return variants_per_n[case_hash]

        current_width = lower_width - 1

        if current_width < 1:
            raise Exception('min width must be 1')
        
        if current_width - 1 < len(cubes_required_per_stage):
            if cubes > cubes_required_per_stage[current_width - 1]:
                #print(f'cubes {cubes} lower_width {lower_width} returned {0}')
                variants_per_n[case_hash] = 0
                return 0

        # print(f'cubes {cubes}')
        # print(f'cubes_required_per_stage {cubes_required_per_stage[current_width - 2]}')

        variants_from_top = 0
        result = 0 

        #if str(cubes) in variants_per_n.keys() and cubes <= current_width:
            #print(f'cubes {cubes} lower_width {lower_width} returned {variants_per_n[str(cubes)]}')
            #return variants_per_n[str(cubes)]
        if cubes <= 3 and cubes <= current_width:
            result = variants_per_n.get(str(cubes), 1)
            variants_per_n[case_hash] = result
            return result
        
        
        
        if cubes <= current_width:
            result += 1 # самый плоский вариант

        first_cubes_contribution = max(cubes - current_width, 1)

        for i in range(first_cubes_contribution, cubes - 1):
            actual_width = min(current_width, cubes - i)
            variants_from_top += recursive(i, actual_width)

        result += variants_from_top
        # if cubes <= current_width:
        #     variants_per_n[str(cubes)] = result
        variants_per_n[case_hash] = result
        #print(f'cubes {cubes} lower_width {lower_width} returned {result}')
        return result


    answer = recursive(n, n+1)
    print(answer)


if __name__ == '__main__':
    main()
