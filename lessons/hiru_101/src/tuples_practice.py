import ast

a = [[1, 2], [1, 2], [5, 5, 4]]  #list within a list
b = ("english word", "french word")  #example of a tuple
another_list = [("a", "b"), ("R", "t"), ("t", "t")]  #tuple within a list
another_list[2][0]  #element in a list within a list

number_list = "[4, 5, 6]"
print(number_list[0])  #convert list into string
print(ast.literal_eval(eval))[0]  #convert string into list

####

a = 2  #global variable

def any_function():
    global a  #calls the gloabl variable
    a = 2  #modifies the global variable after the global variable gets called