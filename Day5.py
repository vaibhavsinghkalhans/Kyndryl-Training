# Score classifier using if/else and a for loop
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    return "F"


scores = [95, 82, 67, 45]

for score in scores:
    print(f"Score: {score}, Grade: {get_grade(score)}")