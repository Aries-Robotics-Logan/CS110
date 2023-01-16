def new_grid(record, grid):
    for row in range(len(grid)):
        for column in range(len(grid)):
            if record[0] == str(row) and record[1] == str(column):
                grid[row][column] = 'X'
    return grid
    pass


def make_grid():
    li, gi = [], []
    for row in range(4):
        for column in range(4):
            li.append('.')
        gi.append(li)
        li = []
    return gi


def display_grid(grid):
    for row in grid:
        for column in row:
            print(column, end='')
        print()


def main():
    display_grid(make_grid())
    currentgrid = make_grid()
    while True:
        record = input('Enter a coordinate: ')
        if record.upper() == "Q":
            break
        record = record.split(',')
        display_grid(new_grid(record, currentgrid))


if __name__ == '__main__':
    main()
