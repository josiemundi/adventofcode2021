def solve_puzzle(puzzle_input):
    instructions = puzzle_input.splitlines(False)

    #remove arrow from coordinate input
    coordinates = [x.split(" -> ") for x in instructions]

    #turn coordinate pairs into tuples
    coordinate_pairs = []
    for row in coordinates:
        pair = []
        for element in row:
            pair.append(tuple(map(int, element.split(","))))
        
        coordinate_pairs.append(pair)

    tally_chart = {}

    for pair in coordinate_pairs:
        if pair[0][0] == pair[1][0]:
            start_point = min(pair[0][1],pair[1][1])
            end_point = max(pair[0][1],pair[1][1])

            for y_coord in range(start_point,end_point+1):
                point = (pair[0][0], y_coord)

                if point in tally_chart:
                    tally_chart[point]+=1
                else:
                    tally_chart[point]=1

        elif pair[0][1] == pair[1][1]:
            start_point = min(pair[0][0],pair[1][0])
            end_point = max(pair[0][0],pair[1][0])

            for x_coord in range(start_point,end_point+1):
                point = (x_coord, pair[0][1])

                if point in tally_chart:
                    tally_chart[point]+=1
                else:
                    tally_chart[point]=1

    counter = 0
    for coord in tally_chart:
        if tally_chart[coord] > 1:
            counter +=1
            

    return counter


if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))