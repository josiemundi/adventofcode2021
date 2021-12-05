def mark_numbers(number, bingo_sheets):
    for bingo_sheet in bingo_sheets:
        for row_number in range(5):
            for column_number in range(5):
                if bingo_sheet[row_number][column_number]==number:
                    bingo_sheet[row_number][column_number]= -1


def bingo(bingocard):
    for row in bingocard:
        if sum(row) == -5:
            return True
    for column in zip(*bingocard):
        if sum(column) == -5:
            return True
    return False

def play_bingo(numbers,bingocards):
    for number in numbers:
        mark_numbers(number, bingocards)

        for bingo_board in bingocards:
            if bingo(bingo_board):
                return number, bingo_board


def solve_puzzle(puzzle_input):
    instructions = puzzle_input.splitlines(False)

    drawn_numbers = list(map(int, instructions[0].split(",")))
    instructions = instructions[1:]

    bingo_boards = []
    while instructions:
        bingo_boards.append([list(map(int,line.split())) for line in instructions[1:6]])
        instructions = instructions[6:]
    
    
    winning_number, winning_board = play_bingo(drawn_numbers,bingo_boards)

    sumofboard= 0

    for row in winning_board:
        for number in row:
            if number != -1:
                sumofboard += number

    return winning_number*sumofboard


if __name__ == "__main__":
    import os
    import pathlib
    puzzle_path = pathlib.Path(__file__).parent.absolute()
    puzzle_input = open(os.path.join(puzzle_path,"puzzle_input")).read()
    print(solve_puzzle(puzzle_input))