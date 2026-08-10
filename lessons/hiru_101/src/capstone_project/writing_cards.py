from language_map import en_translate
import time
import card_list
saved_list = []

print("The current card list contains " + len.list(card_list) + " words")  #number of words will be ties to length in a card list file later
time.sleep(2)

more_words = True
if more_words:
    en_word = input("Type a word in English to get the French translation: ")
    translator = en_translate(en_word)
    save_word = input("Do you want to save this card? (yes/no) ")
    if save_word == "yes":
        save_word = True
        saved_list.append(en_word)
    elif save_word == "no":
        save_word = False
        exit()
    else:
        print("Invalid response, please answer yes or no")
    more_words = input("Do you want to translate a new word? (yes/no) ")
    if more_words == "yes":
        more_words = True
    elif more_words == "no":
        more_words = False
        exit()
    else:
        print("Invalid response, please answer yes or no")
else:
    exit()

print("Your card list includes: ")
print(saved_list)
save_cards = input("Save cards to file? (yes/no) ")
if save_cards == "yes":
    with open("card_list.py", "a") as f:
        f.write(card_list.append(saved_list))
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