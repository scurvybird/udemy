fruit_list = ["apple", "banana", "strawberry"]
fruit_answer = input("What fruit do you want? ")

#if fruit_answer in fruit_list:
    #print("okay")
#else:
    #print("I don't have any " + fruit_answer)

if not fruit_answer in fruit_list:
    print("I don't have any " + fruit_answer)
    exit()
    
print("okay")