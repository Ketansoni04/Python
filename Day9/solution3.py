score = 185

if score > 100 :
    print("Enter a valid score")
    exit()
    

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "D"


print(grade)