from fracGen import *
from write import *



def commonFractionSumSheet(questionsAmount):
    exs = []
    for index in range(questionsAmount):
        exs += [generateEX(4)]

    lines = []
    lines += [r"\section*{Sommes de fractions quelquonques}"+"\n"]
    lines += writeExPack(exs,4,None)
    lines += [r"\section*{Corrections}"+"\n"]
    lines += writeSolutionPack(exs,None)

    outputTexExercices("sheets/sum.tex",lines)




def simplificationSheet(questionsAmount):
    exs = []
    for index in range(questionsAmount):
        exs += [generateEX(1)]

    lines = []
    lines += [r"\section*{Simplifications}"+"\n"]
    lines += writeExPack(exs,1,"")
    lines += [r"\section*{Corrections}"+"\n"]
    lines += writeSolutionPack(exs,"")

    outputTexExercices("sheets/simp.tex",lines)



#feuille d'exercices pour la maniuplation basique de fractions
def sheet1(questionsAmount):
    exs1 = []
    exs2 = []
    exs3 = []
    for index in range(questionsAmount):
        exs1 += [generateEX(1)]
        exs2 += [generateEX(2)]
        exs3 += [generateEX(3)]

    lines = []
    lines += [r"\section*{Manipulation des fractions}"+"\n"]
    lines += writeExPack(exs1,1,"Exercice 1")
    lines += [r"\newpage"+"\n"]
    lines += writeExPack(exs2,2,"Exercice 2")
    lines += [r"\newpage"+"\n"]
    lines += writeExPack(exs3,3,"Exercice 3")
    lines += [r"\newpage"+"\n"]
    lines += [r"\section*{Corrections}"+"\n"]
    lines += writeSolutionPack(exs1,"Exercice 1 corrigé")
    lines += [r"\newpage"+"\n"]
    lines += writeSolutionPack(exs2,"Exercice 2 corrigé")
    lines += [r"\newpage"+"\n"]
    lines += writeSolutionPack(exs3,"Exercice 3 corrigé")
    lines += [r"\newpage"+"\n"]

    outputTexExercices("sheets/sheet1.tex",lines)
