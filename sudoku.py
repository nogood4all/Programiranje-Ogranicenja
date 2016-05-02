from constraint import *

size = 3

sudoku = [
    [ 7, 6, 0,   4, 0, 0,   0, 0, 8, ],
    [ 0, 0, 0,   5, 0, 0,   0, 1, 0, ],
    [ 0, 0, 5,   0, 7, 0,   0, 9, 0, ],
    
    [ 3, 0, 0,   7, 0, 0,   0, 0, 0, ],
    [ 0, 4, 0,   0, 0, 0,   0, 8, 0, ],
    [ 0, 0, 0,   0, 0, 5,   0, 0, 9, ],
    
    [ 0, 3, 0,   0, 9, 0,   4, 0, 0, ],
    [ 0, 8, 0,   0, 0, 6,   0, 0, 0, ],
    [ 4, 0, 0,   0, 0, 7,   0, 6, 1, ],
]

problem = Problem()

for i in range(size ** 2):
    for j in range(size ** 2):
        if sudoku[i][j] == 0:
            problem.addVariable((i, j), range(1, size ** 2 + 1))
        else:
            problem.addVariable((i, j), [sudoku[i][j]])

for i in range(0, size ** 2):
    vertical = []
    horizontal = []
    for j in range(0, size ** 2):
        vertical.append((i, j))
        horizontal.append((j, i))
    problem.addConstraint(AllDifferentConstraint(), vertical)
    problem.addConstraint(AllDifferentConstraint(), horizontal)

for i in range(0, size):
    for j in range(0, size):
        square = []
        for k in range(0, size):
            for l in range(0, size):
                square.append((size * i + k, size * j + l))
        problem.addConstraint(AllDifferentConstraint(), square)


for solution in problem.getSolutions():
    solved = dict()
    for key, value in solution.iteritems():
        try:
            solved[key[0]][key[1]] = value
        except:
            solved[key[0]] = dict()
        solved[key[0]][key[1]] = value
        
    for i, value1 in solved.iteritems():
        for j, value2 in value1.iteritems():
            print str(value2) + " ",
            if (j + 1) % size == 0:
                print " ",
        print ""
        if (i + 1) % size == 0:
            print ""
    print ""
