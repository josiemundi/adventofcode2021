def new_spawn(fish_age):
    ages = fish_age[1:]+[fish_age[0]]
    ages[6] += fish_age[0]
    return ages
    
    
def solve_puzzle(puzzle_input):
    instructions = puzzle_input


    fishes = list(map(int, instructions.split(",")))

    #create a list of fish ages
    fish_age = []

    for position in range(9):
        fish_age.append(len([x for x in fishes if x==position]))

    for day in range(80):
        print(fish_age)
        fish_age = new_spawn(fish_age)
    
    return sum(fish_age)


if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))