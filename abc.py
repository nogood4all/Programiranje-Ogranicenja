from constraint import *
#Trazimo takve ABC promenljive da ABC/A+B+C da ima ostatak pri deljenju 0
def main():
    problem = Problem()
    problem.addVariables("abc", range(1,10))
	#primer dodavanja nekih ogranicenja
    problem.addConstraint(lambda a,b,c: a!=b)
    problem.addConstraint(lambda a,b,c: a>c)
    problem.addConstraint(lambda a,b,c: c!=b)
	#pronalazenje svih kombinacija koje postuju zadate uslove
    problem.getSolutions()
    minvalue = 999/(9*3)
    minsolution = {}
    for solution in problem.getSolutions():
        a = solution["a"]
        b = solution["b"]
        c = solution["c"]
		#Realno resenje
        value = (a*100+b*10+c)*1.0/(a+b+c)*1.0
		#Celobrojno resenje
		value2 = (a*100+b*10+c)/(a+b+c)
		#Provera da li je ostatak 0
        if value < minvalue and value - value2 == 0 :
            minsolution = solution
			minvalue = value2
    print minvalue
    print minsolution

if __name__ == "__main__":
    main()
