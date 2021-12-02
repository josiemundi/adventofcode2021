
def solve_puzzle(puzzle_input):
    depths = [int(x) for x in puzzle_input.splitlines(False)]
    res = []
    for i in range(1, len(depths)-2):
        if sum(depths[i:i+3]) > sum(depths[i-1:i+2]):
            res.append(True)
    return len(res)


if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))