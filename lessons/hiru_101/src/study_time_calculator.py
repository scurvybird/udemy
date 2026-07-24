#iteration 1: One day

#hours_sleep = int(input("How many hours do you sleep each day? ")) #input sleeping hours
#hours_work = int(input("How many hours do you work each day? ")) #input working hours
#hours_relax_wd = int(input("How many hours do you relax each day? ")) #input relaxing hours
#hours_avail_wd = 24 - (hours_sleep + hours_work + hours_relax_wd + 3) #calculate available hours: 24 - (sleeping hours + working hours + relaxing hours + 3)
#print("You will have " + str(hours_avail_wd) + " hours to study each day.") #print available hours

#iteration 2: One week

hours_sleep = int(input("How many hours do you sleep each day? ")) #input sleeping hours
hours_work = int(input("How many hours do you work each day? ")) #input working hours
hours_relax_wd = int(input("How many hours do you relax each work day? ")) #input work day relaxing hours
hours_relax_we = int(input("How many hours do you relax each weekend day? ")) #input weekend day relaxing hours
hours_avail_wd = 24 - (hours_sleep + hours_work + hours_relax_wd + 3)
hours_avail_total = (hours_avail_wd * 5) + (48 - ((hours_sleep + hours_relax_we + 3) * 2)) #calculate available hours: (one day available hours * 5) + (48 - ((sleeping hours + weekend day relaxing hours + 3) * 2))
print("You will have " + str(hours_avail_total) + (" hours to study through the week")) #print available hours