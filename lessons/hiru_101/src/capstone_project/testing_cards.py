from language_map import en_translate
from language_map import fr_translate
import time
import random

from pathlib import Path
cwd = Path(__file__).resolve().parent

import json

try:
    with open(cwd.joinpath('card_list.json'), 'r', encoding='utf-8') as file:
        data = json.load(file)
        # print("file parsed as data type: " + str(type(data)))
        # print("parsed json string is: " + str(data))
except:
    data = {}
    print("unable to load json")

# print("database flat file path is: " + str(cwd.joinpath("card_list.json")))
# with open(cwd.joinpath("card_list.json"), "r") as f:
#     contents = f.read()


saved_list = data
# saved_list = []

print("The current card list contains " + str(len(saved_list)) + " words")  #number of words will be ties to length in a card list file later
time.sleep(2)
print("Please enter the french translation")
time.sleep(1)
input("Ready? Press ENTER to continue...")
time_begin = time.time()
while len(saved_list) > 0:
    random_word = random.choice(saved_list)
    fr_word = input("translate " + random_word + " ")
    if random_word == fr_translate(fr_word):
        saved_list.remove(random_word)
        print("Correct!")
    else:
        print("Not correct, will retry later.")
time_end = time.time()
duration = time_end - time_begin
with open(cwd.joinpath("card_list.json"), 'w', encoding='utf-8') as file:
        json.dump(list(saved_list), file, indent=4)
print("You guessed all words in " + str(duration) + " seconds!")

#say "The current list contains '#' words."
#input "Ready? Press ENTER to start. "
    #timer runs from when pressing ENTER to ending the quiz
#input <english word from the saved list> <words are randomized>
    #incorrect answer -> "Not correct, will retry later."
    #correct answer -> "Correct!"
    #correct answers are removed from the list
#timer ends when all words are removed from the list
#say "You guessed all the cards in '#' seconds!"
#End Program