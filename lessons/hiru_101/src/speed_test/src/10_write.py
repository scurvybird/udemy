import math
import time
from pathlib import Path
cwd = Path(__file__).resolve().parent

import json

import_begin = time.time()
try:
    with open(cwd.joinpath('../test_data/en_fr_10k.json'), 'r', encoding='utf-8') as file:
        data = json.load(file)
except:
    data = {}
    print("unable to load json")
    exit(1)
import_end = time.time()
import_time = (import_end - import_begin) * 1000000

def truncate(number, decimals=0):
    factor = 10 ** decimals
    return math.trunc(number * factor) / factor

def en_translate(en_word):
    en_trans = data.get(en_word)
    print(en_trans)
    return en_trans

saved_list = set(data)

print("The current card list contains " + str(len(saved_list)) + " words")  #number of words will be ties to length in a card list file later
print("json import load time " + str(truncate(import_time, 4)) + " us")
time.sleep(2)

more_words = True
while more_words:
    en_word = input("Type a word in English to get the French translation: ")
    time_begin = time.time()
    translator = en_translate(en_word)
    time_end = time.time()
    duration = (time_end - time_begin) * 1000000
    print(str(truncate(duration, 4)) + " us")
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
