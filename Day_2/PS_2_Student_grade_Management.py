# Student Grade Management System in which displayed the grades, highest grade, lowest grades and average grades

grades = []
for i in range(1, 6):
    g = int(input("Enter the grades : "))
    grades.append(g)
print(grades)

grades.sort()
print("\nHighest grade =", grades[4], "\nlowest grade =", grades[0])
print("\nAverage of grades =", sum(grades)/len(grades))
