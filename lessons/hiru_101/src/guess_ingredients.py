import time
ingredient_list = ["eggs", "flour", "chocolate", "butter", "sugar", "salt"]
score = 0

print("Can you guess the ingredients in this cookie recipe? You have 3 chances.")
time.sleep(3.0)

for i in range(3):
    ingredient = input("What is your #" + str(i + 1) + " guess? ")
    if ingredient in ingredient_list:
        print("Correct, " + ingredient + " is on the list!")
        score += 1
    else:
        print("That is not correct.")

time.sleep(1.0)
print("Well done, you guessed " + str(score) + " of the ingredients correctly!")
