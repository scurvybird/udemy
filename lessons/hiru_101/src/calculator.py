def print_instr():
    print("Please provide two numbers and an operation to execute between them")

def add_nums(num1, num2):
    return num1 + num2

def sub_nums(num1, num2):
    return num1 - num2

def mult_nums(num1, num2):
    return num1 * num2

def div_nums(num1, num2):
    return num1 / num2

oper_list = ["1. addition", "2. subtraction", "3. multiplication", "4. division"]

print_instr()
num1 = float(input("Number 1: "))
num2 = float(input("Number 2: "))
operation = int(input("Operation: " + str(oper_list) + " "))

if operation == 1:
    result = add_nums(num1, num2)
elif operation == 2:
    result = sub_nums(num1, num2)
elif operation == 3:
    result = mult_nums(num1, num2)
elif operation == 4:
    if num2 != 0:
        result = div_nums(num1, num2)
    else:
        print("Cannot divide by 0")
        exit()
else:
    print("This operation is not available")
    exit()

print("Result: " + str(result))
