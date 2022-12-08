import numpy as np


class Block:
    shape_name = ''
    shape_default = list('-' * 16)
    shape_matrix, shape_prntblock = [], []

    data_dict = {
    'N': [[]],
    'O': [[5, 6, 9, 10]],
    'I': [[1, 5, 9, 13], [4, 5, 6, 7]],
    'S': [[6, 5, 9, 8], [5, 9, 10, 14]],
    'Z': [[4, 5, 9, 10], [2, 5, 6, 9]],
    'L': [[1, 5, 9, 10], [2, 4, 5, 6], [1, 2, 6, 10], [4, 5, 6, 8]],
    'J': [[2, 6, 9, 10], [4, 5, 6, 10], [1, 2, 5, 9], [0, 4, 5, 6]],
    'T': [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]]}

    def __init__(self, block_name):
        self.shape_name = block_name
        self.shape_matrix = self.data_dict[block_name]

    def print_block(self, data_list):
        self.shape_prntblock = self.shape_default.copy()
        for elem in data_list:
            self.shape_prntblock[elem] = '0'
        self.shape_prntblock = np.reshape(self.shape_prntblock, (4, 4))
        for item in self.shape_prntblock:
            print(*item, sep=' ')
        print('')

    def print_all_vars(self):
        # print NONE figure
        self.print_block([])

        temp_list = []
        for n in range(5):
            temp_list.clear()
            for elem in self.shape_matrix[n % len(self.shape_matrix)]:
                temp_list.append(elem)
            self.print_block(temp_list)


my_block = Block(input())
my_block.print_all_vars()
