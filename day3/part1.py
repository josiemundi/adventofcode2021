
import numpy as np

def solve_puzzle(puzzle_input):
    instructions = puzzle_input.splitlines(False)
    binary_result_gamma=[]
    binary_result_epsilon=[]
    n_inst = list(map(list, zip(*instructions)))

    #convert list elements to int
    list_of_integers = [[int(float(j)) for j in i] for i in n_inst]
    
    for x in list_of_integers:
        if sum(x) > len(x)//2:
            binary_result_gamma.append("1")
            binary_result_epsilon.append("0")
            print(1)
        else:
            binary_result_gamma.append("0")
            binary_result_epsilon.append("1")
            print(0)

    
    binary_result_gamma = int(''.join(binary_result_gamma),2)
    binary_result_epsilon = int(''.join(binary_result_epsilon),2)

    return binary_result_epsilon*binary_result_gamma

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))