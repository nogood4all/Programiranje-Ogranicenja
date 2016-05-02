from constraint import *

def main():
    problem = Problem()
    problem.addVariables("abc", range(1,10)) 
#    problem.addConstraint(lambda a,b,c: a!=1)
    problem.getSolutions()
    for solution in problem.getSolutions():
        a = solution["a"]
        b = solution["b"]
        c = solution["c"]
        value = (100*a+10*b+c)*1.0/(a**3+b**3+c**3)*1.0
        if value == 1.0:
            print solution 

if __name__ == "__main__":
    main()
