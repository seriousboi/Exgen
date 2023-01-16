


def outputTexExercices(filename,exerciceslines):
    startLines = [r"\documentclass{article}","\n",
    r"\usepackage[utf8]{inputenc}","\n",
    r"\usepackage[a4paper, total={7.5in, 11in}]{geometry}","\n",
    r"\setlength{\parindent}{0pt}","\n",
    r"\begin{document}","\n",
    r"\huge","\n",
    "\n",]
    endLines = [r"\end{document}""\n",]

    lines = startLines + exerciceslines + endLines

    file= open(filename,"w")
    file.writelines(lines)
    file.close()



def writeExPack(problems,type,title):
    examples = [None,(1, 5, 3, 5),(2, -2, 16, 147, 7, 2, 21),(3, -5, 3, 25, 6, 2, 15, 3, 5, 2),
    (4,2,7,3,6,"big",3,2)]
    orders = [None,r"Simplifier pour obtenir une fraction irréductible.\\"+"\n",
    r"Sommer puis simplifier pour obtenir une fraction irréductible.\\"+"\n",
    r"Mettre au même dénominateur pour sommer puis simplifier pour obtenir une fraction irréductible.\\"+"\n",
    r"Développer chaque fraction pour obtenir un dénominateur commun puis sommer, puis simplifier si possible.\\"+"\n"]

    lines = []
    if title != None:
        lines += [r"\subsection*{"+title+"}"+"\n"]
    if type != None:
        lines += [orders[type]]
        lines += writeExSolution(examples[type],"exemple")
        lines += ["\n"]
    for index in range(len(problems)):
        problem = problems[index]
        lines += writeEx(problem,letter(index))
    return lines



def writeSolutionPack(problems,title):
    lines = []
    if title != None:
        lines += [r"\subsection*{"+title+"}"+"\n"]
    for index in range(len(problems)):
        problem = problems[index]
        lines += writeExSolution(problem,letter(index))
    return lines



def writeEx(problem,title):
    associatedFunction = [None,writeExType1,writeExType2,writeExType3,writeExType4]
    type = problem[0]
    return associatedFunction[type](problem,title)



def writeExSolution(problem,title):
    associatedFunction = [None,writeExType1solution,writeExType2solution,writeExType3solution,writeExType4solution]
    type = problem[0]
    return associatedFunction[type](problem,title)



def writeExType4(problem,title):
    type,leftNum,leftDen,rightNum,rightDen,rightDenSize,rightDenFac1,rightDenFac2 = problem
    lines = []
    if title != None:
        lines += [title+") "]
    lines += ["$"]
    lines += [writeFraction(leftNum,leftDen)+"+"+writeFraction(rightNum,rightDen)]
    lines += ["=$"]
    lines += endl()
    return lines



def writeExType4solution(problem,title):
    type,leftNum,leftDen,rightNum,rightDen,rightDenSize,rightDenFac1,rightDenFac2 = problem
    lines = []
    if title != None:
        lines += [title+") "]
    lines += ["$"]
    lines += [writeFraction(leftNum,leftDen)+"+"+writeFraction(rightNum,rightDen)]
    lines += ["="+writeFraction(str(leftNum)+r"\times"+str(rightDen),str(leftDen)+r"\times"+str(rightDen))+"+"+writeFraction(str(rightNum)+r"\times"+str(leftDen),str(rightDen)+r"\times"+str(leftDen))]
    lines += ["="+writeFraction(leftNum*rightDen,leftDen*rightDen)+"+"+writeFraction(rightNum*leftDen,leftDen*rightDen)]
    lines += ["="+writeFraction(str(leftNum*rightDen)+"+"+str(rightNum*leftDen),leftDen*rightDen)]
    numerator = leftNum*rightDen+rightNum*leftDen
    denominator = leftDen*rightDen
    lines += ["="+writeFraction(numerator,denominator)]

    if rightDenSize == "big":
        lines += ["="+writeFraction(str(numerator)+r"\div"+str(rightDenFac1),str(denominator)+r"\div"+str(rightDenFac1))]
        lines += ["="+writeFraction(numerator//rightDenFac1,denominator//rightDenFac1)]

    lines += ["$"]
    lines += endl()
    return lines



def writeExType3(problem,title):
    type,leftNum,leftDen,rightNum,rightDen,simplifier,numSum,factor,numerator,denominator = problem
    lines = []
    if title != None:
        lines += [title+") "]
    lines += ["$"]
    lines += [writeFraction(leftNum,leftDen)+"+"+writeFraction(rightNum,rightDen)]
    lines += ["=$"]
    lines += endl()
    return lines



def writeExType3solution(problem,title):
    type,leftNum,leftDen,rightNum,rightDen,simplifier,numSum,factor,numerator,denominator = problem
    lines = []
    if title != None:
        lines += [title+") "]
    lines += ["$"]
    lines += [writeFraction(leftNum,leftDen)+"+"+writeFraction(rightNum,rightDen)]
    lines += ["="+writeFraction(str(leftNum)+r"\times"+str(simplifier),str(leftDen)+r"\times"+str(simplifier))+
    "+"+writeFraction(rightNum,rightDen)]
    lines += ["="+writeFraction(leftNum*simplifier,rightDen)+"+"+writeFraction(rightNum,rightDen)]
    lines += ["="+writeFraction(numSum,rightDen)]
    lines += ["="+writeFraction(str(numSum)+r"\div"+str(factor),str(rightDen)+r"\div"+str(factor))]
    lines += ["="+writeFraction(numerator,denominator)]
    if denominator == 1:
        lines += ["="+str(numerator)]
    lines += ["$"]
    lines += endl()
    return lines



def writeExType2(problem,title):
    type,leftNum,rightNum,denSum,factor,numerator,denominator = problem
    lines = []
    if title != None:
        lines += [title+") "]
    lines += ["$"]
    lines += [writeFraction(leftNum,denSum)+"+"+writeFraction(rightNum,denSum)]
    lines += ["=$"]
    lines += endl()
    return lines



def writeExType2solution(problem,title):
    type,leftNum,rightNum,denSum,factor,numerator,denominator = problem
    lines = []
    if title != None:
        lines += [title+") "]
    lines += ["$"]
    lines += [writeFraction(leftNum,denSum)+"+"+writeFraction(rightNum,denSum)]
    lines += ["="+writeFraction(str(leftNum)+"+"+str(rightNum),denSum)]
    lines += ["="+writeFraction(numerator*factor,denSum)]
    lines += ["="+writeFraction(str(numerator*factor)+r"\div"+str(factor),str(denominator*factor)+r"\div"+str(factor))]
    lines += ["="+writeFraction(numerator,denominator)]
    if denominator == 1:
        lines += ["="+str(numerator)]
    lines += ["$"]
    lines += endl()
    return lines



def writeExType1(problem,title):
    type,factor,numerator,denominator = problem
    lines = []
    if title != None:
        lines += [title+") "]
    lines += ["$"]
    lines += [writeFraction(numerator*factor,denominator*factor)]
    lines += ["=$"]
    lines += endl()
    return lines



def writeExType1solution(problem,title):
    type,factor,numerator,denominator = problem
    lines = []
    if title != None:
        lines += [title+") "]
    lines += ["$"]
    lines += [writeFraction(numerator*factor,denominator*factor)]
    lines += ["="+writeFraction(str(numerator*factor)+r"\div"+str(factor),str(denominator*factor)+r"\div"+str(factor))]
    lines += ["="+writeFraction(numerator,denominator)]
    if denominator == 1:
        lines += ["="+str(numerator)]
    lines += ["$"]
    lines += endl()
    return lines



def writeFraction(numerator,denominator):
    fracString = r"\frac{"+str(numerator)+"}{"+str(denominator)+"}"
    return fracString



def endl():
    skipSize = 10
    return [r"\\ ","\n","\n"]



def letter(index):
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l",
    "m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    return letters[index%26]
