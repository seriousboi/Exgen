from random import randrange,randint,seed



def isIrreducible(firstInteger,secondInteger):
    #faire un parcour sur les nombres premiers pour gagner en efficacité
    for factor in range(2,min(firstInteger,secondInteger)+1):
        if firstInteger%factor == 0 and secondInteger%factor == 0:
            return False
    return True



def generateEX(type):
    associatedFunction = [None,generateEX1,generateEX2,generateEX3,generateEX4]
    return associatedFunction[type]()



#exercice type 4, somme de deux fractions quelquonques puis simplification
def generateEX4():
    commonFactors = [2,3,4,5,6,7,8,9]
    primes = [2,3,5]

    leftDen = randomPick(commonFactors)

    for factor in commonFactors:
        if (factor**2)%leftDen == 0:
            commonFactors.remove(factor)
            if factor in primes:
                primes.remove(factor)
    rightDen = randomPick(commonFactors)

    rightDenSize = randomPick(["small","big"])
    if rightDenSize == "big":
        rightDenFac1 =  rightDen
        rightDenFac2 =  randomPick(primes)
        rightDen = rightDenFac1*rightDenFac2
    elif rightDenSize == "small":
        rightDenFac1 = rightDen
        rightDenFac2 = 1

    radius = 13
    leftNum = randomPick(list(range(-radius,-1))+list(range(1,radius+1))*2)

    if rightDenSize == "small":
        rightNum = randomPick(list(range(-radius,-1))+list(range(1,radius+1))*2)
    elif rightDenSize == "big":
        rightNumFac = randomPick(list(range(-radius//2,-1))+list(range(1,(radius+1)//2))*2)
        rightNum = rightDenFac1*rightNumFac

    type = 4
    problem = (type,leftNum,leftDen,rightNum,rightDen,rightDenSize,rightDenFac1,rightDenFac2)
    return problem


#exercice type 3,réécriture pour ensuite sommer deux fracrions puis simplifier la somme
def generateEX3():
    problem = generateEX1()
    type,factor,numerator,denominator = problem

    numSum = numerator*factor
    denSum = denominator*factor
    rightDen = denSum

    commonFactors = [2,3,4,5,6,7,8,9]
    simplifiers = []
    for potentialFactor in commonFactors:
        if denSum%potentialFactor == 0:
            simplifiers += [potentialFactor]

    simplifier = randomPick(simplifiers)
    leftDen = denSum//simplifier

    radius = 15 #négativé maximale (>= max(commonFactors)/2)
    potentialNums = []
    for potentialNum in range(-radius,numSum+radius):
        if potentialNum%simplifier == 0 and potentialNum!=0 and potentialNum!=numSum:
            potentialNums += [potentialNum]

    leftNumDev = randomPick(potentialNums)
    rightNum = numSum - leftNumDev
    leftNum = leftNumDev//simplifier

    type = 3
    problem = (type,leftNum,leftDen,rightNum,rightDen,simplifier,numSum,factor,numerator,denominator)
    return problem


def printEX3(problem):
    type,leftNum,leftDen,rightNum,rightDen,simplifier,numSum,factor,numerator,denominator = problem
    print(str(leftNum)+"/"+str(leftDen)+"+"+str(rightNum)+"/"+str(rightDen)+"="+str(numerator)+"/"+str(denominator))



#exercice type 2, somme de deux fracrions puis simplification
def generateEX2():
    problem = generateEX1()
    type,factor,numerator,denominator, = problem

    numSum = numerator*factor
    denSum = denominator*factor

    radius = 15 #négativé maximale
    numGap = randint(-radius,numSum+radius)
    leftNum = numGap
    rightNum = numSum - leftNum

    type = 2
    problem = (type,leftNum,rightNum,denSum,factor,numerator,denominator)
    return problem



def printEX2(problem):
    type,leftNum,rightNum,denSum,factor,numerator,denominator = problem
    print(str(leftNum)+"/"+str(denSum)+"+"+str(rightNum)+"/"+str(denSum)+"="+str(numerator)+"/"+str(denominator))



#exercice type 1, simplification d'une fraction
def generateEX1():
    seed()
    primes = {2,3,5,7}
    oprimes = {1,2,3,5,7}

    facSize = randomPick(["small","big"])
    if facSize == "big":
        factor = randomPick(primes)
        factor = factor*randomPick(primes)
    elif facSize == "small":
        factor = randomPick(primes)

    numSize = randomPick(["small","big"])
    denSize = randomPick(["small","big"])
    if facSize == "big": #si on a une grosse simplification à faire le numérateur et dénominateur doivent être petits
        numSize = "small"
        denSize = "small"

    if numSize == "big":
        numeratorA = randomPick(oprimes)
        numeratorB = randomPick(oprimes)
        numerator = numeratorA*numeratorB
        oprimes.discard(numeratorA)
        oprimes.discard(numeratorB)
    elif numSize == "small":
        numerator = randomPick(oprimes)
        oprimes.discard(numerator)

    if denSize == "big":
        denominator = randomPick(oprimes)
        denominator = denominator*randomPick(oprimes)
    elif denSize == "small":
        denominator = randomPick(oprimes)

    type = 1
    problem = (type,factor,numerator,denominator)
    return problem



def printEX1(problem):
    type,factor,numerator,denominator = problem
    print(str(numerator*factor)+"/"+str(denominator*factor)+"="+str(numerator)+"/"+str(denominator))



def randomPick(listOrSet):
    myList = list(listOrSet)
    return myList[randrange(len(myList))]
