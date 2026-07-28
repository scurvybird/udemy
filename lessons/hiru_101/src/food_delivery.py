avail_pizza = ["four cheese", "pepperoni", "calzone", "napoli", "margherita"]
pizza_order = []
total_price = 0.00
print("Welcome to Scurvy's Pizzeria!")

for i, pizza in enumerate(avail_pizza):
    print(str(i) + ". " + pizza)

valid_choice = False
while not valid_choice:
    pizza_choice = int(input("what number would you like to order? "))
    #Validate user input here
    if pizza_choice >= 0 and pizza_choice <= len(avail_pizza) - 1:
        pizza_order.append(avail_pizza[pizza_choice])
        print("That'll be a " + avail_pizza[pizza_choice])
        total_price += 10
        valid_choice = True
    else:
        print("I'm sorry, that option is not available on our menu.")

cont_order = True
while cont_order:
    answer = input("Anything else you would like to order? (yes/no) ")
    if answer =="yes":
        valid_choice = False
        while not valid_choice:
            pizza_choice = int(input("what number would you like to add? "))
            #Validate user input here
            if pizza_choice >= 0 and pizza_choice <= len(avail_pizza) - 1:
                pizza_order.append(avail_pizza[pizza_choice])
                print("That'll be a " + avail_pizza[pizza_choice])
                total_price += 10
                valid_choice = True
            else:
                print("I'm sorry, that option is not available on our menu.")
    else:
        cont_order = False

print("Your order is: ")
print(pizza_order)
print("Your total comes to $" + str(total_price))

valid_tip = False
while not valid_tip:
    tip = float(input("Would you like to add a tip? (0 to 25%) "))
    if tip >= 0:
        valid_tip = True
    else:
        print("Please provide a proper tip for our service staff")

total_price += total_price * (tip / 100)
print("Thank you! Your total has been adjusted to $" + str(total_price) + ". Thank you for dining with us!")
