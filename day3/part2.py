
def solve_puzzle(puzzle_input):
    instructions = puzzle_input.splitlines(False)
    oxygen_generator_list = instructions.copy()
    co2_scrubber_list = instructions.copy()

    for position in range(len(instructions[0])):
        if len(oxygen_generator_list) >1:
            x = [int(row[position]) for row in oxygen_generator_list]
            if sum(x) >= len(x)-sum(x):
                oxygen_generator_list = [x for x in oxygen_generator_list if x[position] == "1"]
            else:
                oxygen_generator_list = [x for x in oxygen_generator_list if x[position] == "0"]
        
        if len(co2_scrubber_list) >1:
            x = [int(row[position]) for row in co2_scrubber_list]
            if sum(x) < len(x)-sum(x):
                co2_scrubber_list = [x for x in co2_scrubber_list if x[position] == "1"]
            else:
                co2_scrubber_list = [x for x in co2_scrubber_list if x[position] == "0"]

    return int(oxygen_generator_list[0],2)*int(co2_scrubber_list[0],2)

if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))