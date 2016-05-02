from constraint import *

def genExp(word):
    exp = ""
    for i in range(0, len(word) - 1):
        exp += str(10 ** i) + "*" + word[i] + "+"
    exp += str(10 ** (len(word) - 1)) + "*" + word[-1]
    return exp

word1 = raw_input().lower()[::-1]
word2 = raw_input().lower()[::-1]
word3 = raw_input().lower()[::-1]

variables = set(word1 + word2 + word3)
exp = genExp(word1) + "+" + genExp(word2) + "==" + genExp(word3)


# Leading zeroes are acceptable

problem = Problem()
problem.addVariables(variables, range(10))
problem.addConstraint(AllDifferentConstraint())


func = "lambda "
arguments = "("
for variable in variables:
    func += variable + ","
    arguments += "'" + variable + "',"
func = func[:-1] + ":" + exp
arguments = arguments[:-1] + ")"

problem.addConstraint(eval(func), eval(arguments))
for key, value in problem.getSolution().iteritems():
    print key, "=", value
    
# Leading zeroes are not acceptable



problem.reset()
firstLetters = set([word1[-1], word2[-1], word3[-1]])
variables2 = variables - firstLetters
print variables, firstLetters


problem.addVariables(variables2, range(10))
problem.addVariables(firstLetters, range(1, 10))

problem.addConstraint(AllDifferentConstraint())


func = "lambda "
arguments = "("
for variable in variables:
    func += variable + ","
    arguments += "'" + variable + "',"
func = func[:-1] + ":" + exp
arguments = arguments[:-1] + ")"

problem.addConstraint(eval(func), eval(arguments))
for key, value in problem.getSolution().iteritems():
    print key, "=", value
