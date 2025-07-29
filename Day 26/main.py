import turtle as tt
import random as rd

numbers = [1,2,3]

new_numbers = [n + 1 for n in numbers]

new_list = [n * 2 for n in range(1,10)]
# print(new_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

upperCaseNames = [name.upper() for name in names]
# print(upperCaseNames)

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
new_integers = [int(n) for n in list_of_strings]

# print(new_integers)

student_dict = {
    "student" : ["Alex", "Beth", "Caroline"],
    "score" : [56, 76, 98]
}

import pandas as pd

student_data_frame = pd.DataFrame(student_dict)

# Iterando sobre as linhas como tuplas (index, row)
for index, row in student_data_frame.iterrows():
    print(f"Index: {index}, Student: {row['student']}, Score: {row['score']}")
