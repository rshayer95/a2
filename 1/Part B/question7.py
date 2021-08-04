import datetime
marks = int(input("Enter your marks: "))
grades = "";

if marks >=90:
    grades = "A+"
elif marks >=80 and marks <=89:
    grades = "A"
elif marks >=70 and marks <=79:
    grades = "B"
elif marks >=60 and marks <=69:
    grades = "C"
elif marks >=50 and marks <=59:
    grades = "D"
elif marks < 50:
    grades = "F"

today = datetime.datetime.now()
print(today.strftime("%A"), ", ", today.strftime("%d"), "/", today.strftime("%B"), "/", today.year , " ", today.strftime("%H"), ":",today.strftime("%M"))
print("Grades ", grades)