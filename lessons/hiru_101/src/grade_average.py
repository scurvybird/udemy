def grade_request():
    grade_list = []
    grade_request = True
    while grade_request:
        grade = float(input("Next grade: "))
        if grade == -1:
            grade_request = False
        else:
            if grade >= 0 and grade <= 10:
                grade_list.append(grade)
            else:
                print("Grades provided must be between 0 and 10 (-1 to stop)")
    return grade_list

def min_grade(num_list):
    min = num_list[0]
    for num in num_list:
        if num < min:
            min = num
    return min

def max_grade(num_list):
    max = num_list[0]
    for num in num_list:
        if num > max:
            max = num
    return max

def avg_grade(num_list):
    sum = 0
    for num in num_list:
        sum += num
    avg = sum / len(num_list)
    return avg

grade_list = grade_request()

if len(grade_list) == 0:
    print("No grades have been submitted")
    exit()

print(grade_list)
print("Grades submitted: " + str(len(grade_list)))

min = min_grade(grade_list)
max = max_grade(grade_list)
avg = avg_grade(grade_list)

print("Min: " + str(min) + " Max: " + str(max) + " Average: " + str(avg))
