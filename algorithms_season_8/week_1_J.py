import sys
from ctypes import c_uint32

# junk = """
# 13
# List x = new List(1,2,5,14,42)
# List y = x.subList(1,4)
# List z = y.subList(2,4)
# y.set(1,7)
# x.get(1)
# z.get(1)
# z.set(2,100)
# x.get(3)
# y.get(3)
# x.add(132)
# x.set(5,43)
# x.get(5)
# y.get(4)
# """.split('\n')[1:-1]

# input_iter = iter(junk)

def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """

    lists_dict = dict()

    n = int(input())
    # n = int(next(input_iter))

    class List_Window:
        __slots__ = ('parent_list', 'start', 'end')
        def __init__(self, letter_parent_list, start, end):
            parent_list = lists_dict[letter_parent_list]
            while isinstance(parent_list, List_Window):
                start += lists_dict[letter_parent_list].start
                end += lists_dict[letter_parent_list].start
                letter_parent_list = parent_list.parent_list
                parent_list = lists_dict[letter_parent_list]
            self.parent_list = letter_parent_list
            self.start = start
            self.end = end
        
        # def __getitem__(self, index):
        #     return self.parent_list[self.start + index]
    
        # def __setitem__(self, index, value):
        #     self.parent_list[self.start + index].value = value
        
        # def __len__(self):
        #     return self.end - self.start

    for i in range(n):

        cmd = input()
        # cmd = next(input_iter)

        if 'new List' in cmd:
            splitted_cmd = cmd.split()
            list_name = splitted_cmd[1]
            list_values = [c_uint32(int(x)) for x in splitted_cmd[4].strip('List(').strip(')').split(',')]
            lists_dict[list_name] = list_values
        elif '.subList' in cmd:
            splitted_cmd = cmd.split()
            list_name = splitted_cmd[1]
            source_list_name = splitted_cmd[3].split('.')[0]
            list_indexes = [int(x) for x in splitted_cmd[3].split('(')[1].strip(')').split(',')]
            start_index = list_indexes[0] - 1
            end_index = list_indexes[1]
            #list_values = tuple(lists_dict[source_list_name][start_index:end_index])
            list_values = List_Window(source_list_name, start_index, end_index)
            lists_dict[list_name] = list_values
        else:
            cmd_dot_split = cmd.split('.')
            if '.set' in cmd:
                list_name = cmd_dot_split[0]
                args = [int(x) for x in cmd_dot_split[1].strip('set(').strip(')').split(',')]
                set_index = args[0] - 1
                set_value = args[1]
                if isinstance(lists_dict[list_name], list):
                    lists_dict[list_name][set_index].value = set_value
                else:
                    letter_list_name = lists_dict[list_name].parent_list
                    set_index += lists_dict[list_name].start
                    lists_dict[letter_list_name][set_index].value = set_value

            elif '.add' in cmd:
                list_name = cmd_dot_split[0]
                add_value = c_uint32(int(cmd_dot_split[1].strip('add(').strip(')')))
                lists_dict[list_name].append(add_value)
            elif '.get' in cmd:
                list_name = cmd_dot_split[0]
                value_index = int(cmd_dot_split[1].strip('get(').strip(')')) - 1
                if isinstance(lists_dict[list_name], list):
                    print(lists_dict[list_name][value_index].value)
                else:
                    letter_list_name = lists_dict[list_name].parent_list
                    value_index += lists_dict[list_name].start
                    print(lists_dict[letter_list_name][value_index].value)
            else:
                raise Exception('unknown cmd')


if __name__ == '__main__':
    main()
