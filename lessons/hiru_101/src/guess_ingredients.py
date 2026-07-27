import time
ingredient_list = ["eggs", "flour", "chocolate", "butter", "sugar", "salt"]
score = 0

print("Can you guess the ingredients in this cookie recipe? You have 3 chances.")
time.sleep(3.0)

ingredient_1 = input("What is your first guess? ")
if ingredient_1 in ingredient_list:
    print("Correct, " + ingredient_1 + " is on the list!")
    score += 1
else:
    print("That is not correct.")

ingredient_2 = input("What is your second guess? ")
if ingredient_2 in ingredient_list:
    print("Correct, " + ingredient_2 + " is on the list!")
    score += 1
else:
    print("That is not correct.")

ingredient_3 = input("What is your third guess? ")
if ingredient_3 in ingredient_list:
    print("Correct, " + ingredient_3 + " is on the list!")
    score += 1
else:
    print("That is not correct.")

time.sleep(1.0)
print("Well done, you guessed " + str(score) + " ingredients correctly!")
