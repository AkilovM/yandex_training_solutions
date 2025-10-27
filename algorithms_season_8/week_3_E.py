import sys

# junk = """
# 10
# 2
# 8
# 9
# 8
# 0
# 0
# 0
# 0
# 0
# 59516 36853 41730 12040 8620 -1298 -66743 -56458 -12264 86726
# """.split('\n')[1:-1]

# input_iter = iter(junk)

class Node:
    def __init__(self, index, value, parent_link, depth):
        self.index = index
        self.value = value
        self.parent = parent_link
        self.affected = 0
        self.depth = depth
    
    def get_depth(self):
        if self.depth == -1:
            parent_depth = self.parent.get_depth()
            self.depth = parent_depth + 1
        return self.depth


def main():
    """
    Пример ввода и вывода числа n, где -10^9 < n < 10^9:
    n = int(input())
    print(n)
    """
    # n = int(next(input_iter))
    n = int(input())

    nodes = []
    nodes.append(Node(0, 0, -1, 0))
    leafs_indexes = set()
    leafs_indexes.add(0)
    leafs_discarded = set()

    nodes += [Node(x,0,-1,-1) for x in range(1,n)]

    for i in range(n-1):
        # ith_nodes_parent = int(next(input_iter))
        ith_nodes_parent = int(input())

        ith_nodes_index = i+1
        parent_obj = nodes[ith_nodes_parent]
        #nodes.append(Node(ith_nodes_index, 0, parent_obj, parent_obj.depth + 1))
        nodes[ith_nodes_index].parent = parent_obj

        if ith_nodes_index not in leafs_discarded:
            leafs_indexes.add(ith_nodes_index)
        leafs_indexes.discard(parent_obj.index)
        leafs_discarded.add(parent_obj.index)
    
    for i in range(n-1):
        #DEPTH
        if nodes[i+1].depth == -1:
            nodes[i+1].depth = nodes[i+1].get_depth()

    # nodes_values = [int(x) for x in next(input_iter).split()]
    nodes_values = [int(x) for x in sys.stdin.readline().split()]

    for i in range(n):
        nodes[i].value = nodes_values[i]
    
    answer = 0
    max_depth = max([nodes[x].depth for x in leafs_indexes])
    nodes_with_max_depth = [nodes[x] for x in leafs_indexes if nodes[x].depth == max_depth]

    while len(nodes_with_max_depth) > 0:
        #new_nodes_with_max_depth = list()
        for node in nodes_with_max_depth:
            actual_value = node.value + node.affected
            affect = - actual_value
            #affect = - (node.value + node.affected)
            answer += abs(affect)
            parent_obj = node.parent
            if parent_obj == -1:
                print(answer)
                return
            else:
                leafs_indexes.add(parent_obj.index)
            parent_obj.affected += node.affected + affect
            # if parent_obj not in new_nodes_with_max_depth:
            #     new_nodes_with_max_depth.append(parent_obj)
            leafs_indexes.discard(node.index)
            #del node
        
        max_depth -= 1

        #nodes_with_max_depth = new_nodes_with_max_depth
        #nodes_with_max_depth = [nodes[x] for x in leafs_indexes if nodes[x].depth == max_depth]
        nodes_with_max_depth = [node for node in nodes if node.depth == max_depth]
    return


if __name__ == '__main__':
    main()
