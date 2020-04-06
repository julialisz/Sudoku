import numpy as np
import csv
import time
from plotly import graph_objects as go
import matplotlib.pyplot as plt

def form_grid(grid, sudoku_string):
    for i in range(0, len(sudoku_string), 9):
        row = sudoku_string[i:i+9]
        temp = []
        for block in row:
            if(block=="."):
                block = 0
            temp.append(int(block))
        grid.append(temp)
    #for row in grid:
        #print(row)


def possible(grid, row, col, digit):
    for i in range(0, 9):
        if grid[row][i] == digit:  #check row
            return False
    for i in range(0, 9):
        if grid[i][col] == digit:  #check column
            return False
    square_row = (row//3)*3
    square_col = (col//3)*3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[square_row+i][square_col+j] == digit:  #check 3x3 square
                return False
    return True


def solve(grid, backtrack_steps, numbers_possible):
    global all_steps
    for row in range(0, 9):
        for col in range(0, 9):
            if grid[row][col] == 0:
                for digit in numbers_possible:
                    all_steps += 1
                    if possible(grid, row, col, digit):
                        grid[row][col] = digit
                        solve(grid, backtrack_steps, numbers_possible)
                        grid[row][col] = 0  #Backtrack step
                        backtrack_steps += 1
                return
    #print('\nThe Solution')
    #for row in grid:
        #print(row)
    #print("Backtrack steps: " + str(backtrack_steps))
    global all_back_steps
    all_back_steps += backtrack_steps



def solve_fc(grid):
    global all_steps
    for row in range(0, 9):
        for col in range(0, 9):
            if grid[row][col] == 0:
                numbers_possible = {1, 2, 3, 4, 5, 6, 7, 8, 9}
                for i in range(0,9):
                    if(grid[row][i] != 0 and grid[row][i] in numbers_possible):
                        numbers_possible.remove(grid[row][i])
                for i in range(0,9):
                    if(grid[i][col] != 0 and grid[i][col] in numbers_possible):
                        numbers_possible.remove(grid[i][col])
                square_row = (row//3)*3
                square_col = (col//3)*3
                for i in range(0,3):
                    for j in range(0,3):
                        if(grid[square_row+i][square_col+i]!=0 and grid[square_row+i][square_col+i] in numbers_possible):
                            numbers_possible.remove(grid[square_row+i][square_col+i])

                for digit in numbers_possible:
                    all_steps += 1
                    if possible(grid, row, col, digit):
                        grid[row][col] = digit
                        solve_fc(grid)
                        grid[row][col] = 0  #Backtrack step
                return
    #for row in grid:
        #print(row)


sudoku_set = []
with open("Sudoku.csv", "r") as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        if(row):
            sudoku_set.append(row[2])
sudoku_set = np.delete(sudoku_set, 0)
#print(sudoku_set[0])
numbers_possible = {1, 2, 3, 4, 5, 6, 7, 8, 9}

#0 LEVEL
all_back_steps = 0
all_steps = 0
print("\nLEVEL 0")
start_time = time.time()
backtrack_steps = 0
for i in range(0, 5):
    grid = []
    form_grid(grid, sudoku_set[i])
    solve(grid, backtrack_steps, numbers_possible)
print("Average number of backtrack steps: " + str(all_back_steps/5))
av_steps_bt_0 = all_steps/5
print("Average number of all steps (backtracking): " + str(av_steps_bt_0))
execution_time = time.time() - start_time
#print("Level 0: --- %s seconds ---" % (execution_time))
average_time_bt_0 = execution_time/5
print("Level 0 average time: " + str(average_time_bt_0))

#backtracking + forward checking
all_steps = 0
print("\nBacktracking + Forward Checking:")
start_time = time.time()
for i in range(0, 5):
    grid = []
    form_grid(grid, sudoku_set[i])
    solve_fc(grid)
av_steps_fc_0 = all_steps/5
print("Average number of all steps: " + str(av_steps_fc_0))
execution_time = time.time() - start_time
average_time_fc_0 = execution_time/5
print("Level 0 average time: " + str(average_time_fc_0))


#1 LEVEL
all_back_steps = 0
all_steps = 0
print("\nLEVEL 1")
start_time = time.time()
for i in range(5, 10):
    grid = []
    form_grid(grid, sudoku_set[i])
    solve(grid, backtrack_steps, numbers_possible)
print("Average number of backtrack steps: " + str(all_back_steps/5))
av_steps_bt_1 = all_steps/5
print("Average number of all steps: " + str(av_steps_bt_1))
execution_time = time.time() - start_time
#print("Level 1: --- %s seconds ---" % (execution_time))
average_time_bt_1 = execution_time/5
print("Level 1 average time: " + str(average_time_bt_1))

#backtracking + forward checking
all_steps = 0
print("\nBacktracking + Forward Checking:")
start_time = time.time()
for i in range(5, 10):
    grid = []
    form_grid(grid, sudoku_set[i])
    solve_fc(grid)
av_steps_fc_1 = all_steps/5
print("Average number of all steps: " + str(av_steps_fc_1))
execution_time = time.time() - start_time
average_time_fc_1 = execution_time/5
print("Level 1 average time: " + str(average_time_fc_1))


#2 LEVEL
print("\nLEVEL 2")
all_back_steps = 0
all_steps = 0
start_time = time.time()
for i in range(10, 15):
    grid = []
    form_grid(grid, sudoku_set[i])
    solve(grid, backtrack_steps, numbers_possible)
print("Average number of backtrack steps: " + str(all_back_steps/5))
av_steps_bt_2 = all_steps/5
print("Average number of all steps: " + str(av_steps_bt_2))
execution_time = time.time() - start_time
#print("Level 2: --- %s seconds ---" % (execution_time))
average_time_bt_2 = execution_time/5
print("Level 2 average time: " + str(average_time_bt_2))

#backtracking + forward checking
all_steps = 0
print("\nBacktracking + Forward Checking:")
start_time = time.time()
for i in range(10, 15):
    grid = []
    form_grid(grid, sudoku_set[i])
    solve_fc(grid)
av_steps_fc_2 = all_steps/5
print("Average number of all steps: " + str(av_steps_fc_2))
execution_time = time.time() - start_time
average_time_fc_2 = execution_time/5
print("Level 2 average time: " + str(average_time_fc_2))


#3 LEVEL
print("\nLEVEL 3")
all_back_steps = 0
all_steps = 0
start_time = time.time()
for i in range(15, 20):
    grid = []
    form_grid(grid, sudoku_set[i])
    solve(grid, backtrack_steps, numbers_possible)
print("Average number of backtrack steps: " + str(all_back_steps/5))
av_steps_bt_3 = all_steps/5
print("Average number of all steps: " + str(av_steps_bt_3))
execution_time = time.time() - start_time
#print("Level 3: --- %s seconds ---" % (execution_time))
average_time_bt_3 = execution_time/5
print("Level 3 average time: " + str(average_time_bt_3))

#backtracking + forward checking
all_steps = 0
print("\nBacktracking + Forward Checking:")
start_time = time.time()
for i in range(15, 20):
    grid = []
    form_grid(grid, sudoku_set[i])
    solve_fc(grid)
av_steps_fc_3 = all_steps/5
print("Average number of all steps: " + str(av_steps_fc_3))
execution_time = time.time() - start_time
average_time_fc_3 = execution_time/5
print("Level 3 average time: " + str(average_time_fc_3))


#4 LEVEL
print("\nLEVEL 4")
all_back_steps = 0
all_steps = 0
start_time = time.time()
for i in range(20, 25):
    grid = []
    form_grid(grid, sudoku_set[i])
    solve(grid, backtrack_steps, numbers_possible)
print("Average number of backtrack steps: " + str(all_back_steps/5))
av_steps_bt_4 = all_steps/5
print("Average number of all steps: " + str(av_steps_bt_4))
execution_time = time.time() - start_time
#print("Level 4: --- %s seconds ---" % (execution_time))
average_time_bt_4 = execution_time/5
print("Level 4 average time: " + str(average_time_bt_4))

#backtracking + forward checking
all_steps = 0
print("\nBacktracking + Forward Checking:")
start_time = time.time()
for i in range(20, 25):
    grid = []
    form_grid(grid, sudoku_set[i])
    solve_fc(grid)
av_steps_fc_4 = all_steps/5
print("Average number of all steps: " + str(av_steps_fc_4))
execution_time = time.time() - start_time
average_time_fc_4 = execution_time/5
print("Level 4 average time: " + str(average_time_fc_4))


#5 LEVEL
print("\nLEVEL 5")
all_back_steps = 0
all_steps = 0
start_time = time.time()
for i in range(25, 30):
    grid = []
    form_grid(grid, sudoku_set[i])
    solve(grid, backtrack_steps, numbers_possible)
print("Average number of backtrack steps: " + str(all_back_steps/5))
av_steps_bt_5 = all_steps/5
print("Average number of all steps: " + str(av_steps_bt_5))
execution_time = time.time() - start_time
#print("Level 5: --- %s seconds ---" % (execution_time))
average_time_bt_5 = execution_time/5
print("Level 5 average time (backtracking): " + str(average_time_bt_5))

#backtracking + forward checking
all_steps = 0
print("\nBacktracking + Forward Checking:")
start_time = time.time()
for i in range(25, 30):
    grid = []
    form_grid(grid, sudoku_set[i])
    solve_fc(grid)
av_steps_fc_5 = all_steps/5
print("Average number of all steps: " + str(av_steps_fc_5))
execution_time = time.time() - start_time
average_time_fc_5 = execution_time/5
print("Level 5 average time: " + str(average_time_fc_5))


#6 LEVEL
print("\nLEVEL 6")
all_back_steps = 0
all_steps = 0
start_time = time.time()
for i in range(30, 35):
    grid = []
    form_grid(grid, sudoku_set[i])
    solve(grid, backtrack_steps, numbers_possible)
print("Average number of backtrack steps: " + str(all_back_steps/5))
av_steps_bt_6 = all_steps/5
print("Average number of all steps: " + str(av_steps_bt_6))
execution_time = time.time() - start_time
#print("Level 6: --- %s seconds ---" % (execution_time))
average_time_bt_6 = execution_time/5
print("Level 6 average time: " + str(average_time_bt_6))

#backtracking + forward checking
all_steps = 0
print("\nBacktracking + Forward Checking:")
start_time = time.time()
for i in range(30, 35):
    grid = []
    form_grid(grid, sudoku_set[i])
    solve_fc(grid)
av_steps_fc_6 = all_steps/5
print("Average number of all steps: " + str(av_steps_fc_6))
execution_time = time.time() - start_time
average_time_fc_6 = execution_time/5
print("Level 6 average time: " + str(average_time_fc_6))


#7 LEVEL
print("\nLEVEL 7")
all_back_steps = 0
all_steps = 0
start_time = time.time()
for i in range(35, 40):
    grid = []
    form_grid(grid, sudoku_set[i])
    solve(grid, backtrack_steps, numbers_possible)
print("Average number of backtrack steps: " + str(all_back_steps/5))
av_steps_bt_7 = all_steps/5
print("Average number of all steps: " + str(av_steps_bt_7))
execution_time = time.time() - start_time
#print("Level 7: --- %s seconds ---" % (execution_time))
average_time_bt_7 = execution_time/5
print("Level 7 average time: " + str(average_time_bt_7))

#backtracking + forward checking
all_steps = 0
print("\nBacktracking + Forward Checking:")
start_time = time.time()
for i in range(35, 40):
    grid = []
    form_grid(grid, sudoku_set[i])
    solve_fc(grid)
av_steps_fc_7 = all_steps/5
print("Average number of all steps: " + str(av_steps_fc_7))
execution_time = time.time() - start_time
average_time_fc_7 = execution_time/5
print("Level 7 average time: " + str(average_time_fc_7))


#8 LEVEL
print("\nLEVEL 8")
all_back_steps = 0
all_steps = 0
start_time = time.time()
for i in range(40, 43):
    grid = []
    form_grid(grid, sudoku_set[i])
    solve(grid, backtrack_steps, numbers_possible)
print("Average number of backtrack steps: " + str(all_back_steps/3))
av_steps_bt_8 = all_steps/3
print("Average number of all steps: " + str(av_steps_bt_8))
execution_time = time.time() - start_time
#print("Level 8: --- %s seconds ---" % (execution_time))
average_time_bt_8 = execution_time/3
print("Level 8 average time: " + str(average_time_bt_8))

#backtracking + forward checking
all_steps = 0
print("\nBacktracking + Forward Checking:")
start_time = time.time()
for i in range(40, 43):
    grid = []
    form_grid(grid, sudoku_set[i])
    solve_fc(grid)
av_steps_fc_8 = all_steps/3
print("Average number of all steps: " + str(av_steps_fc_8))
execution_time = time.time() - start_time
average_time_fc_8 = execution_time/3
print("Level 8 average time: " + str(average_time_fc_8))


#9 LEVEL
print("\nLEVEL 9")
all_back_steps = 0
all_steps = 0
start_time = time.time()
for i in range(43, 46):
    grid = []
    form_grid(grid, sudoku_set[i])
    solve(grid, backtrack_steps, numbers_possible)
print("Average number of backtrack steps: " + str(all_back_steps/3))
av_steps_bt_9 = all_steps/3
print("Average number of all steps: " + str(av_steps_bt_9))
execution_time = time.time() - start_time
#print("Level 9: --- %s seconds ---" % (execution_time))
average_time_bt_9 = execution_time/3
print("Level 9 average time: " + str(average_time_bt_9))

#backtracking + forward checking
all_steps = 0
print("\nBacktracking + Forward Checking:")
start_time = time.time()
for i in range(43, 46):
    grid = []
    form_grid(grid, sudoku_set[i])
    solve_fc(grid)
av_steps_fc_9 = all_steps/3
print("Average number of all steps: " + str(av_steps_fc_9))
execution_time = time.time() - start_time
average_time_fc_9 = execution_time/3
print("Level 9 average time: " + str(average_time_fc_9))

diff_level = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
bt_steps = [av_steps_bt_0, av_steps_bt_1, av_steps_bt_2, av_steps_bt_3, av_steps_bt_4, av_steps_bt_5, av_steps_bt_6, av_steps_bt_7, av_steps_bt_8, av_steps_bt_9]
fc_steps = [av_steps_fc_0, av_steps_fc_1, av_steps_fc_2, av_steps_fc_3, av_steps_fc_4, av_steps_fc_5, av_steps_fc_6, av_steps_fc_7, av_steps_fc_8, av_steps_fc_9]
bt_time = [average_time_bt_0, average_time_bt_1, average_time_bt_2, average_time_bt_3, average_time_bt_4, average_time_bt_5, average_time_bt_6, average_time_bt_7, average_time_bt_8, average_time_bt_9]
fc_time = [average_time_fc_0, average_time_fc_1, average_time_fc_2, average_time_fc_3, average_time_fc_4, average_time_fc_5, average_time_fc_6, average_time_fc_7, average_time_fc_8, average_time_fc_9]

'''fig = go.Figure(data = [go.Table(header=dict(values=['Difficulty level', 'Backtracking steps', 'Backtracking time', 'Bt + fc steps', 'Bt + fc time']),
    cells=dict(values=[diff_level, bt_steps, bt_time, fc_steps, fc_time]))
    ])

fig.show()'''

#data = [fig]
#py.iplot(data, filename = 'sudoku_table')

#Barplot of number of steps
# The x position of bars
barWidth = 0.3
r1 = np.arange(len(bt_steps))
r2 = [x + barWidth for x in r1]

plt.bar(r1, bt_steps, width = barWidth, color = 'blue', edgecolor = 'black', label='bt')
plt.bar(r2, fc_steps, width = barWidth, color = 'green', edgecolor = 'black', label='bt+fc')

plt.title('Number of steps in backtracking and forward checking')
plt.xticks([r + barWidth for r in range(len(bt_steps))], diff_level)
plt.ylabel('Number of steps')
plt.legend()
plt.show()


#Barplot of time
# The x position of bars
barWidth = 0.3
r1 = np.arange(len(bt_time))
r2 = [x + barWidth for x in r1]

plt.bar(r1, bt_time, width = barWidth, color = 'purple', edgecolor = 'black', label='bt')
plt.bar(r2, fc_time, width = barWidth, color = 'green', edgecolor = 'black', label='bt+fc')

plt.title('Time of compilation for backtracking and forward checking')
plt.xticks([r + barWidth for r in range(len(bt_time))], diff_level)
plt.ylabel('Time')
plt.legend()
plt.show()
