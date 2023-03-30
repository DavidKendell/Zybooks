currentGrade = float(input())
currentPoints = currentGrade * 0.6
remainingPoints = 90 - currentPoints
#finalGrade * 0.4 = remaingingPoints
finalGrade = (remainingPoints * 10) / 4
print("{finalGrade:.1f}".format(finalGrade = finalGrade), "%", sep="")