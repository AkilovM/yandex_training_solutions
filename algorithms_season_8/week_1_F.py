import sys

# junk = """
# 4 3
# +-+
# ??-
# ?-?
# ++?
# """.split('\n')[1:-1]

# input_iter = iter(junk)

def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    n, m = [int(x) for x in input().split()]
    # n, m = [int(x) for x in next(input_iter).split()]

    #rows_minuses_counts = [0] * n
    columns_pluses_counts = [0] * m
    least_row_minuses_count = m + 1
    #least_column_pluses_count = n + 1
    remember_best_row = 'abra'
    map_of_questions = set()
    for i in range(n):
        row = input()
        # row = next(input_iter)
        local_row_minuses_count = 0
        local_map_of_questions = set()
        for c in range(m):
            sign = row[c]
            if sign == '+':
                columns_pluses_counts[c] += 1
            elif sign == '-':
                local_row_minuses_count += 1
            elif sign == '?':
                local_map_of_questions.add(c)
        #least_row_minuses_count = min(least_row_minuses_count, local_row_minuses_count)
        if local_row_minuses_count < least_row_minuses_count:
            least_row_minuses_count = local_row_minuses_count
            remember_best_row = row
            map_of_questions = local_map_of_questions
        elif local_row_minuses_count == least_row_minuses_count:
            for c in list(map_of_questions):
                sign = row[c]
                if sign != '?':
                    map_of_questions.discard(c)
    
    max_row_sum = m - least_row_minuses_count - least_row_minuses_count
    least_column_pluses_count = min(columns_pluses_counts)
    #idx_best_column = columns_pluses_counts.index(least_column_pluses_count)
    indexes_of_best_columns = set([i for i, v in enumerate(columns_pluses_counts) if v == least_column_pluses_count])
    min_column_sum = least_column_pluses_count - (n - least_column_pluses_count)

    #sign_question_mark_on_intersection = remember_best_row[idx_best_column] == '?'
    sign_question_mark_on_intersection = len(indexes_of_best_columns - map_of_questions) == 0
    answer = max_row_sum - min_column_sum
    if sign_question_mark_on_intersection:
        answer -= 2
    print(answer)
    
    # print(f'answer {answer}')
    # print(f'remember_best_row {remember_best_row}')
    # print(f'least_column_pluses_count {least_column_pluses_count}')
    # print(f'idx_best_column {idx_best_column}')
    # print(f'sign_question_mark_on_intersection {sign_question_mark_on_intersection}')



if __name__ == '__main__':
    main()
