temp = int(input("What is the temperature? "))

if temp < 20.0:
    print("Turn the heater on.")
elif temp > 25.0:
    print("Turn the cooler on.")
#elif temp >= 20.0 and temp <= 25.0: #alternate way to code the condition
#    print("Temperature is okay") 
else:
    print("Temperature is okay")
