def solve_puzzle(puzzle_input):
    instructions = puzzle_input


    crabs = list(map(int, instructions.split(",")))

    crab_counts = {}

    for element in crabs:
        if element in crab_counts:
            crab_counts[element] +=1
        else:
            crab_counts[element] =1
    
    min_position = min(crabs)
    max_position = max(crabs)
    sum_fuel_min = max_position*len(crab_counts)

    for final_position in range(min_position,max_position+1):
        sum_fuel = 0
        for initial_position, crab_count in crab_counts.items():
            sum_fuel += abs(final_position-initial_position)*crab_count
        print(sum_fuel)

        if sum_fuel < sum_fuel_min:
            sum_fuel_min = sum_fuel

    return sum_fuel_min


if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))