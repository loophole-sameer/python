lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# Add your function below!
def average(numbers):
    total = sum(numbers)
    total = float(total)
    return total / len(numbers)
    
def get_average(student):
    homework = average(student['homework'])
    quizzes = average(student['quizzes'])
    tests = average(student['tests'])
    return ((homework * 0.1) + (quizzes * 0.3) + (tests * 0.6))
    
#print get_average(lloyd)
#print get_average(alice)
#print get_average(tyler)

def get_letter_grade(score):
    if (score == 90 or score > 90):
        return "A"
    elif (score == 80 or score > 80):
        return "B"
    elif (score == 70 or score > 70):
        return "C"
    elif (score == 60 or score > 60):
        return "D"
    else:
        return "F"
        
#print get_letter_grade(get_average(lloyd))
#print get_letter_grade(get_average(alice))
#print get_letter_grade(get_average(tyler))

def get_class_average(students = [lloyd, alice, tyler]):
    results = []
    for student in students:
        results.append(get_average(student))
    return average(results)
print get_class_average()
print get_letter_grade(get_class_average())