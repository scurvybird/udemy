grocery_list = ["eggs", "flour", "chocolate"]  #creates a list with it's values
temperature_list = [20.4, -6.7]

print(grocery_list)
#print(len(grocery_list))
#print(temperature_list)

grocery_list[1] = "water"  #changes a specific value in a list
print(grocery_list[1])

grocery_list.append("milk")  #adds an additional value to a list

print(grocery_list)

if "water" in grocery_list:  #checks if a specific value is in a list
    print("okay")
