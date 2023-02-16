import random

t_grid = [
    [7,0,0,  0,0,9,  0,0,0],
    [0,0,0,  6,0,0,  0,4,0],
    [0,0,2,  0,0,0,  0,0,0],

    [0,0,0,  0,0,0,  4,0,0],
    [0,5,0,  0,4,6,  0,0,0],
    [0,0,0,  0,0,0,  0,0,0],

    [0,0,6,  0,0,0,  0,0,5],
    [2,0,0,  5,0,0,  0,0,0],
    [0,0,0,  0,0,0,  0,3,0]
]

def sudoku_solver(grid):
    print('-------new--------')
    new_grid = [[]]*9

    count = 0
    while count < 9:
        print(f'um>>>>>>> new while loop - count is {count}')
        new_line = []
        #new_row: not_nulls > negative_list > removing nn >                   append them
        n_nulls = [x for x in grid[count] if x != 0]
        compl = list(range(1,10))
        for nn in n_nulls:
            compl.remove(nn)
        for x in grid[count]:
            if x != 0:
                new_line.append(x)
            else:
                z = random.choice(compl)
                new_line.append(z)
                compl.remove(z)

        new_grid[count] = new_line
        print(f'new_grid now: {new_grid}')

        #create collumns:
        all_9 = 0     #counter to check if through all 9
        for col in range(9):

            col_li = []
            for row in range(count+1):
                col_li.append(new_grid[row][col])

            print(f'created collumn_nr.{col}: {col_li}')

            #check collumns one after another:
            check_li = list(range(1,10))
            for n in col_li:
                if n in check_li:
                    check_li.remove(n)
                    all_9 += 1
                    print(f'{n}: unique in col_nr.{col} count on {all_9}')

        if all_9 == (count+1)*9:
            count +=1
        else:
            count -= 1

    return new_grid

# collum_check works!!! probably the same with the box_check
# problem: the random fill-up-way will never lead to solution. computes for ever
# idea: checking the nums of other collumns before, too avoid them
#       >> very complicated.
# better idea: dont refill every time the complete row
#       >> just replace the double part




if __name__ == '__main__':
    print(sudoku_solver(t_grid))
