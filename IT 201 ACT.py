#1. Read the student name, attendance grade, and 3 quizzes, activities, assignment, and major exam. Compute the final grade
#Determine student remark if PASSED OR FAILED. 
#The program will display all input the computed grade per term, the final grade and the remarks. finals grade = average(prelim, midterm, pre-final, finals)
#for each term compute grade = 10% x attendance + activities x 20% + assignment x 10% + average of quizzes x 10% + major exam x 50%


def calculate_final_grade(attendance, activities, assignment, quizzes, major_exam):
    prelim_weight = 0.10
    midterm_weight = 0.20
    pre_final_weight = 0.20
    finals_weight = 0.50

    # Calculate the average of quizzes
    quizzes_average = sum(quizzes) / len(quizzes)

    # Calculate the final grade
    final_grade = (
        attendance * prelim_weight +
        activities * midterm_weight +
        assignment * pre_final_weight +
        quizzes_average * pre_final_weight +
        major_exam * finals_weight
    )

    return final_grade

# determine the student's remark
def determine_remark(final_grade):
    passing_score = 75 

    if final_grade >= passing_score:
        return "PASSED"
    else:
        return "FAILED"

# Input student information
student_name = input("Enter student name: ")
attendance_grade = float(input("Enter attendance grade(out of 100): "))
activities_grade = float(input("Enter activities grade(out of 100): "))
assignment_grade = float(input("Enter assignment grade(out of 100): "))
quizzes = [float(input(f"Enter quiz {i+1} grade(out of 50): ")) for i in range(3)]
major_exam_grade = float(input("Enter major exam grade(out of 75): "))

# Calculate the final grade
final_grade = calculate_final_grade(attendance_grade, activities_grade, assignment_grade, quizzes, major_exam_grade)

# Determine the student's remark
remark = determine_remark(final_grade)

# Display the results
print("Student Information:")
print("Name:", student_name)
print("Attendance Grade:", attendance_grade)
print("Activities Grade:", activities_grade)
print("Assignment Grade:", assignment_grade)
print("Quiz Grades:", quizzes)
print("Major Exam Grade:", major_exam_grade)
print("Calculated Final Grade:", final_grade)
print("Remark:", remark)




#2. Read input name, date of birth (MM-DD-YY) and determine the zodiac sign and chinese zodiac(year)
#Display name, birthdate, zodoac sign and chinese zodiac sign(year)


# Function to determine the Chinese zodiac year based on the year of birth
def determine_chinese_zodiac_year(year):
    zodiac_animals = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]
    return zodiac_animals[(year - 1900) % 12]


def determine_zodiac_sign(month, day):
    zodiac_signs = [
        ("Capricorn", (1, 20), (2, 16)),
        ("Aquarius", (2, 16), (3, 11)),
        ("Pisces", (3, 11), (4, 18)),
        ("Aries", (4, 18), (5, 13)),
        ("Taurus", (5, 13), (6, 21)),
        ("Gemini", (6, 21), (7, 20)),
        ("Cancer", (7, 20), (8, 10)),
        ("Leo", (8, 10), (9, 16)),
        ("Virgo", (9, 16), (10, 30)),
        ("Libra", (10, 30), (11, 23)),
        ("Scorpio", (11, 23), (11, 29)),
        ("Sagittarius", (12, 17), (1, 20))
    ]
    
    for sign, (start_month, start_day), (end_month, end_day) in zodiac_signs:
        if (month == start_month and day >= start_day) or (month == end_month and day <= end_day):
            return sign

    return "Invalid Date"


# Input from the user
name = input("Enter your name: ")
dob = input("Enter your date of birth (MM-DD-YYY): ")

# Extract month, day, and year from the input
month, day, year = map(int, dob.split('-'))


# Determine the zodiac sign and Chinese zodiac year
zodiac_sign = determine_zodiac_sign(month, day)
chinese_zodiac_year = determine_chinese_zodiac_year(year)

# Display the results
print("Name:", name)
print("Birthdate:", dob)
print("Zodiac Sign:", zodiac_sign)
print("Chinese Zodiac Year:", chinese_zodiac_year)




#3. Reada positive number and print
try:
    number = int(input("Enter a positive number: "))
    
    if number <= 0:
        print("Please enter a positive number.")
    else:
        for i in range(number, 0, -1):
            for j in range(number, i - 1, -1):
                print(j, end='')
            print() 
except ValueError:
    print("Invalid input. Please enter a valid positive integer.")

