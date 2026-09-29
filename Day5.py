# Score classifier using if/else and a for loop

scores = [95, 78, 62, 45, 88]

for score in scores:
    if score >= 90:
        grade = "A"
    elif score >= 75:
        grade = "B"
    elif score >= 60:
        grade = "C"
    else:
        grade = "F"

    print(f"Score: {score}, Grade: {grade}")