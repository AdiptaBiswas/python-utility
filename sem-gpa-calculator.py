'''
  * Semester wise GPA calculator for my college subjects
  * Outputs would be rounded off in 3 nearest digits
'''

gradeMarks = {"S": 10, "A": 9, "B": 8, "C": 7, "D": 5, "U": 0, "I": 0, "W": 0}

''' 
  Grade and Credit lists to be put here. Can be altered by inputing as well
  
  ...[]
  ....
  ...[]
  ...[]
'''
    
def gradeToMarks(grdCrtList):
    gradeList, creditList = grdCrtList
    totalCredit = 0
    obtainedPoints = 0
    for g in range(len(gradeList)):
        tempPoints = gradeList[g]
        obtainedPoints += gradeMarks[tempPoints] * creditList[g]
        totalCredit += creditList[g]*10
    return obtainedPoints, totalCredit
    
def pointsToCgpa(obtPts, totCrdts):
    gpa = (obtPts/totCrdts) * 10
    return round(gpa,3)

def generate():
    passingList = [[gradeSem1, creditSem1], [gradeSem2, creditSem2], [gradeSem3,creditSem3], [gradeSem4, creditSem4], 
    [gradeSem5, creditSem5], [gradeSem6, creditSem6], [gradeSem7, creditSem7]]
    gpaList = []
    for P in passingList:
        obtPts, totCrdts = gradeToMarks(P)
        tempGpa = pointsToCgpa(obtPts, totCrdts)
        gpaList.append(tempGpa)
    for i,j in enumerate(gpaList):
        print("Semester {}: {}".format(i+1,j))
        
if __name__ == "__main__":
    generate()
