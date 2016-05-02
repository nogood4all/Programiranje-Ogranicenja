from constraint import *

problem = Problem()

problem.addVariable((0, 1), range(11))
problem.addVariable((0, 2), range(13))
problem.addVariable((1, 3), range(6))
problem.addVariable((1, 4), range(5))
problem.addVariable((2, 4), range(4))
problem.addVariable((2, 5), range(9))
problem.addVariable((3, 6), range(5))
problem.addVariable((3, 7), range(4))
problem.addVariable((4, 7), range(9))
problem.addVariable((5, 8), range(6))
problem.addVariable((5, 4), range(2))
problem.addVariable((6, 7), range(3))
problem.addVariable((7, 8), range(5))

problem.addConstraint(lambda in1, out1, out2: out1 + out2 == in1, ((0, 1), (1, 3), (1, 4))) # node 1
problem.addConstraint(lambda in1, out1, out2: out1 + out2 == in1, ((0, 2), (2, 4), (2, 5))) # node 2
problem.addConstraint(lambda in1, out1, out2: out1 + out2 == in1, ((1, 3), (3, 6), (3, 7))) # node 3
problem.addConstraint(lambda in1, in2, in3, out1: out1 == in1 + in2 + in3, ((1, 4), (2, 4), (5, 4), (4, 7))) # node 4
problem.addConstraint(lambda in1, out1, out2: out1 + out2 == in1, ((2, 5), (5, 4), (5, 8))) # node 5
problem.addConstraint(lambda in1, out1: out1 == in1, ((3, 6), (6, 7))) # node 6
problem.addConstraint(lambda in1, in2, in3, out1: out1 == in1 + in2 + in3, ((3, 7), (4, 7), (6, 7), (7, 8))) # node 7

#problem.addConstraint(lambda in1, in2, out1, out2, out3, out4: out1 + out2 + out3 + out4 == in1 + in2, ((0, 1), (0, 2), (1, 3), (1, 4), (2, 4), (2, 5)))

solutions = problem.getSolutions()

print(len(solutions))

#for solution in solutions:
    #flow = solution[(7, 8)] + solution[(5, 8)]
    #if flow == 9:
        #print solution
