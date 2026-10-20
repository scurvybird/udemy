import math
import time
import csv
from pathlib import Path
cwd = Path(__file__).resolve().parent
import logging

# Set the global logging level to DEBUG
logging.basicConfig(level=logging.DEBUG)

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
            item = item.rstrip('\n')
            sorting_set.add(item)
sorting_list = list(sorting_set)

# print(sorting_list)

def compare_strings(sorting_item: str, final_item: str) -> int:
    letter_index = 0
    while letter_index < len(sorting_item) and letter_index < len(final_item):
        if sorting_item[letter_index] > final_item[letter_index]:
            return 1
        elif sorting_item[letter_index] < final_item[letter_index]:
            return -1
        else:
            letter_index += 1
    if len(sorting_item) < len(final_item):
        return -1
    if len(sorting_item) > len(final_item):
        return 1
    return 0

# def compare_strings(sorting_item: str, final_item: str):
#     if sorting_item > final_item:
#         return 1
#     elif sorting_item < final_item:
#         return -1
#     else:
#         return 0

input("Press ENTER to execute the sort")
time_begin = time.time()

test_item = sorting_list.pop(0)

final_list.append(test_item)

while len(sorting_list) > 0:
    final_list_index = 0
    final_item = final_list[final_list_index]
    while len(final_list) > final_list_index:
        sorting_list_index = 0
        sorting_item = sorting_list[sorting_list_index]
        if compare_strings(sorting_item, final_item) == -1:
            # logging.debug("put into final_list")
            final_list.insert(final_list_index, sorting_item)
            sorting_list.remove(sorting_item)
        else:
            # logging.debug(final_list_index)
            final_list_index += 1
    final_list.insert(final_list_index + 1, sorting_item)
    sorting_list.remove(sorting_item)

    
time_end = time.time()
duration = time_end - time_begin
print("The sorting process took " + str(duration) + " seconds")

with open(cwd.joinpath("final_list.json"), 'w', encoding='utf-8') as file:
        json.dump(list(final_list), file, indent=4)

# with open(cwd.joinpath("sorting_list.json"), 'w', encoding='utf-8') as file:
#         json.dump(list(sorting_list), file, indent=4)
