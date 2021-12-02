
def solve_puzzle(puzzle_input):
    instructions = puzzle_input.splitlines(False)
    h=0
    d=0
    a=0
    for i in instructions:
        if i[0] == "f":
            h+= int(i.split(" ")[1])
            d+= int(i.split(" ")[1])*a
        elif i[0] == "d":
            a+= int(i.split(" ")[1])
        elif i[0] == "u":
            a-= int(i.split(" ")[1])

   
    return h*d


if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))