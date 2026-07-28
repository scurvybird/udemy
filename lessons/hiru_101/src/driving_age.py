#input the country
country = input("What country are you driving in? (South Africa, India, France, or Mexico) ")

#input the age
age = int(input("What is your age? "))

#if S. Africa and >= 17 -> you can drive
    #else -> you cannot drive
if country == "South Africa":
    if age >= 17:
        print("You can drive here")
    else:
        print("You cannot drive here")
#else if India and >= 18 -> you can drive
    #else -> you cannot drive
elif country == "India":
    if age >= 18:
        print("You can drive here")
    else:
        print("You cannot drive here")
#else if France and >= 18 -> you can drive
    #else if >= 15 -> you can drive with supervision
    #else -> you cannot drive
elif country == "France":
    if age >= 18:
        print("You can drive here")
    elif age >= 15:
        print("You can drive here with supervision")
    else:
        print("You cannot drive here")
#else if Mexico and >= 18 -> you can drive
    #else if >= 16 -> you can drive with parental agreement
    #else if >= 15 -> you can drive with parental supervision
    #else -> you cannot drive
elif country == "Mexico":
    if  age >= 18:
        print("You can drive here")
    elif age >= 16:
        print("You can drive here with parental agreement")
    elif age >= 15:
        print("You can drive here with parental supervision")
    else:
        print("You cannot drive here")
#else -> Data is not available
else:
    print("Data is not available")