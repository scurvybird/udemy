#for i in range(10):  #syntax for creating a fixed loop
#    print("Hello " + str(i + 1))

#i = 0  
#while i < 10:  #syntax for creating a conditional loop
#    i += 1
#    print("Hello " + str(i))

temp_list = [20.3, 13.6, -6.8, 12.1, -5.0, 0.4, 15.9]

for i, temp in enumerate(temp_list):
    print(str(i) + ": " + str(temp))
