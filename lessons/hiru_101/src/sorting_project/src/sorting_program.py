import math
import time
import csv
from pathlib import Path
cwd = Path(__file__).resolve().parent

import json

try:
    with open(cwd.joinpath('../data_files/countries_1.json'), 'r', encoding='utf-8') as file:
        tmp_1 = json.load(file)
except:
    tmp_1 = {}
    print("unable to load json")
    exit(1)

try:
    with open(cwd.joinpath('../data_files/countries_2.txt'), 'r', encoding='utf-8') as file:
        tmp_2 = file.readlines()
except:
    tmp_2 = {}
    print("unable to load txt")
    exit(1)

try:
    with open(cwd.joinpath('../data_files/countries_3.txt'), 'r', encoding='utf-8') as file:
        tmp_3 = file.readlines()
except:
    tmp_3 = {}
    print("unable to load txt")
    exit(1)

try:
    with open(cwd.joinpath('../data_files/countries_4.json'), 'r', encoding='utf-8') as file:
        tmp_4 = json.load(file)
except:
    tmp_4 = {}
    print("unable to load json")
    exit(1)

try:
    with open(cwd.joinpath('../data_files/countries_5.csv'), 'r', encoding='utf-8') as file:
        tmp_5 = list(csv.reader(file))
except:
    tmp_5 = {}
    print("unable to load csv")
    exit(1)

try:
    with open(cwd.joinpath('../data_files/countries_6.csv'), 'r', encoding='utf-8') as file:
        tmp_6 = list(csv.reader(file))
except:
    tmp_6 = {}
    print("unable to load csv")
    exit(1)

try:
    with open(cwd.joinpath('../data_files/countries_7.csv'), 'r', encoding='utf-8') as file:
        tmp_7 = list(csv.reader(file))
except:
    tmp_7 = {}
    print("unable to load csv")
    exit(1)

try:
    with open(cwd.joinpath('../data_files/countries_8.json'), 'r', encoding='utf-8') as file:
        tmp_8 = json.load(file)
except:
    tmp_8 = {}
    print("unable to load json")
    exit(1)

# sorting_list = set(tmp_1 + tmp_2 + tmp_3 + tmp_4 + tmp_5 + tmp_6 + tmp_7 + tmp_8)
# final_list = {}

final_list = []
sorting_set = set()
all_groups = [tmp_1, tmp_2, tmp_3, tmp_4, tmp_5, tmp_6, tmp_7, tmp_8]
for group in all_groups:
    for item in group:
        if isinstance(item, list):
            sorting_set.update(item)
        else:
            sorting_set.add(item)
sorting_list = list(sorting_set)

def item_sort(sorting_list):
    letter_index = 0
    while letter_index <= len(sorting_item):
        if sorting_item[letter_index] < final_item[letter_index]:
            return True
        elif sorting_item[letter_index] > final_item[letter_index]:
            return False
        else:
            letter_index += 1

input("Press ENTER to execute the sort")
time_begin = time.time()


final_list.append(sorting_list[0])
del sorting_list[0]

while len(sorting_list) > 0:
    list_index = 0
    sorting_item = sorting_list[list_index]
    final_item = final_list[list_index]
    if item_sort(sorting_list) == True:
        final_list.insert(list_index, sorting_item)
        sorting_list.remove(sorting_item)
    else:
        if len(sorting_list) <= list_index:
            final_list.insert(list_index + 1, sorting_item)
            sorting_list.remove(sorting_item)
        else:
            list_index += 1
    
time_end = time.time()
duration = time_end - time_begin
print("The sorting process took " + str(duration) + " seconds")

with open(cwd.joinpath("final_list.json"), 'w', encoding='utf-8') as file:
        json.dump(list(final_list), file, indent=4)