totalWorkingDays = 185 #source NCTB(Bangladesh)
totalAbsentDays = int(input("Enter Student Absent Days: "))

#Percentage Formula
absentPercentage = int((totalAbsentDays/totalWorkingDays) * 100)

#Percentage Check
if absentPercentage >= 35:
    print(f"Student's Absent Percentage {absentPercentage} which is above 35%.\nHe/She is not Eligible for Final Examination.")
else:
    print(f"Student's Absent Percentage {absentPercentage} which is below or equal to 35%.\nHe/She is Eligible for Final Examination.")