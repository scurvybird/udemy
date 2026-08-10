en_fr_dict = {
    "hello": "bonjour",
    "goodbye": "au revoir",
    "thank you": "merci",
    "welcome": "bienvenue"
}

fr_en_dict = {
    "bonjour": "hello",
    "au revoir": "goodbye",
    "merci": "thank you",
    "bienvenue": "welcome"
}

def en_translate(en_word):
    print(en_fr_dict.get(en_word))

def fr_translate(fr_word):
    print(fr_en_dict.get(fr_word))


#en_translate("hello")

# def fr_translate(fr_word):
#     print(fr_en_dict.get(fr_word))

# fr_translate("bonjour")
