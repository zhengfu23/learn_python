import random
import re
import time
from string import ascii_lowercase


def setup_grid(grid_size, start, num_of_mines):
    empty_grid = [['0' for _ in range(grid_size)] for _ in range(grid_size)]

    mines = get_mines(empty_grid, start, num_of_mines)

    for i, j in mines:
        empty_grid[i][j] = 'X'

    grid = get_numbers(empty_grid)

    return grid, mines


def show_grid(grid):
    grid_size = len(grid)

    horizontal = '   ' + (4 * grid_size * '-') + '-'

    # Print top column letters
    top_label = '     '

    for i in ascii_lowercase[:grid_size]:
        top_label = top_label + i + '   '

    print(top_label + '\n' + horizontal)

    # Print left row numbers
    for idx, i in enumerate(grid):
        row = f'{(idx+1):2}'

        for j in i:
            row = row + ' ' + j + ' |'

        print(row + '\n' + horizontal)

    print('')


def get_random_cell(grid):
    grid_size = len(grid)

    a = random.randint(0, grid_size - 1)
    b = random.randint(0, grid_size - 1)

    return a, b


def get_neighbors(grid, row, col):
    grid_size = len(grid)
    neighbors = []

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            elif -1 < (row + i) < grid_size and -1 < (col + j) < grid_size:
                neighbors.append((row + i, col + j))

    return neighbors


def get_mines(grid, start, num_of_mines):
    mines = []
    start_neighbors = get_neighbors(grid, *start)

    for i in range(num_of_mines):
        cell = get_random_cell(grid)
        while cell == start or cell in mines or cell in start_neighbors:
            cell = get_random_cell(grid)
        mines.append(cell)
    return mines


def get_numbers(grid):
    for row_i, row in enumerate(grid):
        for col_j, cell in enumerate(row):
            if cell != 'X':
                # If this is not a mine, get the values of the neighbors
                values = [grid[r][c] for r, c in get_neighbors(grid, row_i, col_j)]

                grid[row_i][col_j] = str(values.count('X'))

    return grid


def show_cells(grid, cur_grid, row_i, col_j):
    # Exit if the cell has already been shown
    if cur_grid[row_i][col_j] != ' ':
        return

    # Show current cell
    cur_grid[row_i][col_j] = grid[row_i][col_j]

    # Get the neighbors if the cell is empty
    if grid[row_i][col_j] == '0':
        for r, c in get_neighbors(grid, row_i, col_j):
            # Repeat function for each neighbor that doesn't have a flag
            if cur_grid[r][c] != 'F':
                show_cells(grid, cur_grid, r, c)


def play_again():
    choice = input('Play again? (y/n): ')

    return choice.lower() == 'y'


def parse_input(input_str, grid_size, help_msg):
    cell = ()
    flag = False
    msg = "Invalid cell. " + help_msg

    pattern = r'([a-{}])([0-9]+)(f?)'.format(ascii_lowercase[grid_size - 1])
    valid_input = re.match(pattern, input_str)

    if input_str == 'help':
        msg = help_msg
    elif valid_input:
        row_i = int(valid_input.group(2)) - 1
        col_j = ascii_lowercase.index(valid_input.group(1))
        flag = bool(valid_input.group(3))

        if -1 < row_i < grid_size:
            cell = (row_i, col_j)
            msg = ''

    return {'cell': cell, 'flag': flag, 'message': msg}


def play_game():
    grid_size = 9
    num_of_mines = 10

    cur_grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]

    grid = []
    flags = []
    start_time = 0

    help_msg = ("Type the column_letter followed by the row_number with no space. (ex: a5). "
                "To put or remove a flag, add 'f' after the cell. (ex: a5f).")

    show_grid(cur_grid)
    print(help_msg + " Type 'help' to show this message again.\n")

    while True:
        mines_remaining = num_of_mines - len(flags)
        prompt = input(f'Enter cell ({mines_remaining} mines remaining): ')
        result = parse_input(prompt, grid_size, help_msg + '\n')

        msg = result['message']
        cell = result['cell']

        if cell:
            print('\n\n')
            row_i, col_j = cell
            cur_cell = cur_grid[row_i][col_j]
            flag = result['flag']

            if not grid:
                # if grid is empty, set up the grid to start new game.
                grid, mines = setup_grid(grid_size, cell, num_of_mines)
            if not start_time:
                # if start_time is 0, start the timer by recording the current time.
                start_time = time.time()

            if flag:
                # Add a flag if the cell is empty
                if cur_cell == ' ':
                    cur_grid[row_i][col_j] = 'F'
                    flags.append(cell)
                elif cur_cell == 'F':
                    cur_grid[row_i][col_j] = ' '
                    flags.remove(cell)
                else:
                    msg = 'Cannot put a flag there'
            elif cell in flags:
                msg = 'There is a flag there'

            elif grid[row_i][col_j] == 'X':
                print('Game Over\n')
                show_grid(grid)
                if play_again():
                    play_game()
                return
            elif cur_cell == ' ':
                show_cells(grid, cur_grid, row_i, col_j)
            else:
                msg = 'That cell has already been shown'

            if set(flags) == set(mines):
                minutes, seconds = divmod(int(time.time() - start_time), 60)
                print(
                    'You won! '
                    f"It took you {minutes} minutes and {seconds} seconds.\n"
                )
                show_grid(grid)
                if play_again():
                    play_game()
                return

        show_grid(cur_grid)
        print(msg)


if __name__ == '__main__':
    play_game()
