import sys

num_col = 8
num_row = 5
HOW_MANY = 4

EMPTY = '.'
WHITE = 'X'
BLACK = 'O'


def horizontal(grid, is_first):
    if is_first:
        for row in range(num_row):
            for i in range(5):
                if grid[row][i] == grid[row][i+1] == grid[row][i+2] == grid[row][i+3] == "O":
                    print("Game finished.")
                    return True
    else:
        for row in range(num_row):
            for i in range(5):
                if grid[row][i] == grid[row][i+1] == grid[row][i+2] == grid[row][i+3] == "X":
                    print("Game finished.")
                    return True
    return False


def vertical(grid, is_first):
    for row in range(0, 2):
        for i in range(0, 8):
            if (grid[row][i] == grid[row+1][i] == grid[row+2][i] == grid[row+3][i] == "O") or (grid[row][i] == grid[row+1][i] == grid[row+2][i] == grid[row+3][i] == "X"):
                print("Game finished.")
                return True
    return False


def diagonal(grid, is_first):
    if is_first:
        for row in range(0, 2):
            for i in range(3, 8):
                if grid[row][i] == grid[row+1][i-1] == grid[row+2][i-2] == grid[row+3][i-3] == "O":
                    print("Game finished.")
                    return True
        for row in range(0, 2):
            for i in range(0, 5):
                if grid[row][i] == grid[row+1][i + 1] == grid[row+2][i + 2] == grid[row+3][i + 3] == "O":
                    print("Game finished.")
                    return True
    elif not is_first:
        for row in range(0, 2):
            for i in range(3, 8):
                if grid[row][i] == grid[row+1][i-1] == grid[row+2][i-2] == grid[row+3][i-3] == "X":
                    print("Game finished.")
                    return True
        for row in range(0, 2):
            for i in range(0, 5):
                if grid[row][i] == grid[row+1][i + 1] == grid[row+2][i + 2] == grid[row+3][i + 3] == "X":
                    print("Game finished.")
                    return True
    return False


def number_in_list(text):
    counter = 0
    for item in text.split():
        counter += 1
    return counter


def player_wins(grid, is_first):
    if horizontal(grid, is_first) or vertical(grid, is_first) or diagonal(grid, is_first):
        return True
    return False


def load_grid():
    row = []
    grid = []
    for r in range(5):
        for column in range(8):
            row.append('.')
        grid.append(row)
        row = []
    return grid


def end_of_game(grid, is_first):
    if player_wins(grid, is_first):
        return True
    return False


def display_grid(rer):
    print("\n01234567")
    for r in rer:
        print("".join(r))
    print("01234567")


def find_row(column, grid):
    for i in range(num_row):
        if grid[i][int(column)] != ".":
            return i - 1
    return num_row - 1


def new_grid(row, column, grid, is_first):
    if is_first:
        grid[row][int(column[0])] = 'X'
    else:
        grid[row][int(column[0])] = 'O'
    return grid
    pass


def is_full(grid):
    counter = 0
    for row in grid:
        for col in row:
            if col != ".":
                counter += 1
    if counter == 40:
        return True


def connect():
    rer = load_grid()
    display_grid(rer)
    current_grid = load_grid()
    is_first = True
    counter = 0
    while True:
        if is_first:
            if counter == 0:
                print("X's turn")
            counter += 1
            response = input("Enter a column: ")
            if response.isdigit():
                if number_in_list(response) == 1:
                    if int(response) <= 7 and int(response) >= 0:
                        row2 = find_row(response, current_grid)
                        current_grid = new_grid(row2, response, current_grid, is_first)
                        display_grid(current_grid)
                        is_first = not is_first
                        counter = 0
                        if is_full(current_grid) is True:
                            print("Game finished.")
                            break
                        if end_of_game(current_grid, is_first):
                            break
                    else:
                        print("Invalid move. Enter a column number (0-7).")
                else:
                    print("Invalid move. Enter a column number (0-7).")
            else:
                print("Invalid move. Enter a column number (0-7).")
        elif not is_first:
            if counter == 0:
                print("O's turn")
            counter += 1
            response = input("Enter a column: ")
            if response.isdigit():
                if number_in_list(response) == 1:
                    if int(response) <= 7 and int(response) >= 0:
                        row2 = find_row(response, current_grid)
                        current_grid = new_grid(row2, response, current_grid, is_first)
                        display_grid(current_grid)
                        is_first = not is_first
                        counter = 0
                        if is_full(current_grid) is True:
                            print("Game finished.")
                            break
                        if end_of_game(current_grid, is_first):
                            break
                    else:
                        print("Invalid move. Enter a column number (0-7).")
                else:
                    print("Invalid move. Enter a column number (0-7).")
            else:
                print("Invalid move. Enter a column number (0-7).")


if __name__ == '__main__':
    connect()
# :)


