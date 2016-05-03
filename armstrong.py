from constraint import *

def main():
    problem = Problem()
	#za potpuno ilustrovanje bi protrebno da promenljive, x y z, imaju mogucnost da uzmu vrednost 0
	#ali to nije moguce zbog deljenja nulom, python prevodilac ne dozvoljava da postoji mogucnost deljenja nulom
	#iako se obezbedimo da se taj slucaj nikad nece desiti
    problem.addVariables("xyz", range(1,10)) 
	#primer dodavanja ogranicenja na algoritam
	#problem.addConstraint(lambda x,y,z: a!=1)
    problem.getSolutions()
    for solution in problem.getSolutions():
        x = solution["x"]
        y = solution["y"]
        z = solution["z"]
		#XYZ = X^3+Y^3+Z^3
        value = (100*x+10*y+z)*1.0/(x**3+y**3+z**3)*1.0
        if value == 1.0:
            print solution 

if __name__ == "__main__":
    main()
