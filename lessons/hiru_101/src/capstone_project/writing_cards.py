from language_map import en_translate
import time

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


saved_list = set(data)
# saved_list = []

print("The current card list contains " + str(len(saved_list)) + " words")  #number of words will be ties to length in a card list file later
print(data)
time.sleep(2)



more_words = True
while more_words:
    en_word = input("Type a word in English to get the French translation: ")
    translator = en_translate(en_word)
    valid_choice = False
    save_answer = input("Do you want to save this card? (yes/no) ")
    while not valid_choice:
        if save_answer == "yes":
            saved_list.add(en_word)
            valid_choice = True
        elif save_answer == "no":
            valid_choice = True
        else:
            print("Invalid response, please answer yes or no")
            valid_choice = False
    valid_choice2 = False
    more_answer = input("Do you want to translate a new word? (yes/no) ")
    while not valid_choice2:
        if more_answer == "yes":
            valid_choice2 = True
        elif more_answer == "no":
            valid_choice2 = True
            more_words = False
        else:
            print("Invalid response, please answer yes or no")
            valid_choice2 = False

print("Your card list includes: ")
print(saved_list)
save_cards = input("Save cards to file? (yes/no) ")
if save_cards == "yes":
    with open(cwd.joinpath("card_list.json"), 'w', encoding='utf-8') as file:
        json.dump(list(saved_list), file, indent=4)
    print("Saving cards...")
    exit()
elif save_cards == "no":
    exit()
else:
    print("Invalid response, please answer yes or no")


#say "The current card list contains '#' words."
#input "Type a word in English to get the French translation: "
    #output the French translation of the input word
#input "Do you want to save this card? (yes/no) "
    #if/else determines if the input gets added to a list of saved words
#input "Do you want to translate a new word? (yes/no) "
    #yes continues the loops, no ends the loop
#print list of saved words
#input "save cards to file? (yes/no) "
    #yes writes a new file containing the list of saved words "Saving cards..."
#End program