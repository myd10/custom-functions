# custom-functions/my_functions.py

# TODO: define temperature conversion function here

# TODO: define gradebook function here


def celsius_to_fahrenheit(c):
    f = (9/5) * c + 32
    return f



def numeric_to_letter_grade(score):
    if score < 0: 
     grade = "Error, please input a grade between 0 and 100"
    elif score < 60: 
        grade = "F"
    elif score < 63:
        grade = "D-"
    elif score < 67:
        grade = "D"
    elif score < 70:
        grade = "D+"
    elif score < 73:
        grade = "C-"
    elif score < 77:
        grade = "C"
    elif score < 80:
        grade = "C+"
    elif score < 83:
        grade = "B-"
    elif score < 87:
        grade = "B"
    elif score < 90:
        grade = "B+"
    elif score < 93:
        grade = "A-"
    elif score <= 100:
        grade = "A"
    elif score > 100:
        grade = "Error, please input a grade between 0 and 100."
    return grade    

#if __name__ == "__main__":


print("--------------------")
print("CUSTOM FUNCTIONS EXERCISE...")


print("--------------------")
c = float((input("what is the temperature in celsius? ")))
print("THE CELSIUS TEMP IS:", c, "DEGREES")
f = round(celsius_to_fahrenheit(c), 2)
print("THE FAHRENHEIT EQUIVALENT IS:", f, "DEGREES")

print("--------------------")
score = float((input("What numeric score did the student earn? ")))
print("THE NUMERIC SCORE IS:", score)
grade = numeric_to_letter_grade(score)
print("THE LETTER-GRADE EQUIVALENT IS:", grade)