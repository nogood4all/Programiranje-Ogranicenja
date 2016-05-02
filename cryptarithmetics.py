from constraint import *


# Funkcija za generisanje izraza
# Primer:
# Broj sa ciframa ABC se prevodi kao 100 * A + 10 * B + C
# Ovi izrazi se evaluiraju u toku izvrsavanja

def genExp(word):
    exp = ""
    for i in range(0, len(word) - 1):
        exp += str(10 ** i) + "*" + word[i] + "+"
    exp += str(10 ** (len(word) - 1)) + "*" + word[-1]
    return exp


# Unose se reci, svaka u novom redu
word1 = raw_input().lower()[::-1]
word2 = raw_input().lower()[::-1]
word3 = raw_input().lower()[::-1]


# Promenljive u resavacu se nazivaju po slovima unutar reci
variables = set(word1 + word2 + word3)


# Izraz koji se evaluira u tacno ili netacno
exp = genExp(word1) + "+" + genExp(word2) + "==" + genExp(word3)


# Vodece nule su prihvatljive

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


#
problem.addConstraint(eval(func), eval(arguments))
for key, value in problem.getSolution().iteritems():
    print key, "=", value
    
# Vodece nule nisu prihvatljive

problem.reset()


# Potrebno je razdvojiti pocetna slova reci od ostalih slova jer ne smeju da budu nule
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
