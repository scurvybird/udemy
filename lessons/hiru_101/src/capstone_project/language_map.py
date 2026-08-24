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
    en_trans = en_fr_dict.get(en_word)
    print(en_trans)
    return en_trans

def fr_translate(fr_word):
    fr_trans = fr_en_dict.get(fr_word)
    print(fr_trans)
    return fr_trans


#en_translate("hello")

# def fr_translate(fr_word):
#     print(fr_en_dict.get(fr_word))

# fr_translate("bonjour")
