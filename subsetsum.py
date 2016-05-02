from constraint import *

target = 5213096522073683233230240000
A = [2316931787588303659213440000,
     1303274130518420808307560000,
     834095443531789317316838400,
     579232946897075914803360000,
     425558899761116998631040000,
     325818532629605202076890000,
     257436865287589295468160000,
     208523860882947329329209600,
     172333769324749858949760000,
     144808236724268978700840000,
     123386899930738064691840000,
     106389724940279249657760000,
     92677271503532146368537600,
     81454633157401300519222500,
     72153585080604612224640000,
     64359216321897323867040000,
     57762842349846905631360000,
     52130965220736832332302400,
     47284322195679666514560000,
     43083442331187464737440000,
     39418499221729173786240000,
     36202059181067244675210000,
     33363817741271572692673536,
     30846724982684516172960000,
     28604096143065477274240000,
     26597431235069812414440000,
     24794751591313594450560000,
     23169317875883036592134400,
     21698632766175580575360000,
     20363658289350325129805625,
     19148196591638873216640000,
     18038396270151153056160000,
     17022355990444679945241600]



#numbers = [int(it) for it in raw_input().split(" ")]

numbers = [ num - target for num in A]

problem = Problem()
func = "lambda "
variables = "("
for i in range(0, len(numbers) - 1):
    problem.addVariable(i, [0, numbers[i]])
    func += "a" + str(i) + ", "
    variables += str(i) + ", "
problem.addVariable(len(numbers) - 1, [0, numbers[-1]])
func += "a" + str(len(numbers) - 1) + ": 0 == "
variables += str(len(numbers) - 1) + ")"
for i in range(0, len(numbers) - 1):
    func  += "a" + str(i) + " + "
func += "a" + str(len(numbers) - 1)
#print func
#print variables

problem.addConstraint(SomeNotInSetConstraint([0]))
problem.addConstraint(eval(func), eval(variables))


#for solution in problem.getSolutions():
    #for key, val in solution.iteritems():
        #if val != 0:
            #print str(val) + " ",
    #print ""

for key, val in problem.getSolution().iteritems():
    if val != 0:
        print str(val) + " ",
print ""
