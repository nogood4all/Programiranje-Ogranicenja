from constraint import *

def main():
    problem = Problem()
    problem.addVariables("abc", range(1,10))
    problem.addConstraint(lambda a,b,c: a!=b)
    problem.addConstraint(lambda a,b,c: a>c)
    problem.addConstraint(lambda a,b,c: c!=b)
    problem.getSolutions()
    minvalue = 999/(9*3)
    minsolution = {}
    for solution in problem.getSolutions():
        a = solution["a"]
        b = solution["b"]
        c = solution["c"]
        value = (a*100+b*10+c)*1.0/(a+b+c)*1.0
	value2 = (a*100+b*10+c)/(a+b+c)
        if value < minvalue and value - value2 == 0 :
            minsolution = solution
	    minvalue = value2
    print minvalue
    print minsolution

if __name__ == "__main__":
    main()
