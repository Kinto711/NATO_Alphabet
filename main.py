# numbers = [1,1,2,3,5,8,13,21,34,55]
# squared_number = [n for n in numbers if n%2 == 0]
# print(squared_number)

# file1 = open("file1")
# file2 = open("file2")
#
# list1 = file1.readlines()
# list2 = file2.readlines()
# same_numbers = [n for n in list1 if n in list2]
#
# print(same_numbers)
#
#
# test = {student:score for (student,score) in test.items() if score > 60}

#
# sentence = "What is the airspeed velocity of an Unladen Swallow?"
#
# new_dict = {word : len(word) for word in sentence.split()}
#
#
# converted_dict = {word : temp * (9/5) + 32 for (word,temp) in new_dict.items()}
#
#
# print(converted_dict)


import pandas

stud_data_frame = pandas.DataFrame(studeent_dict)
# for (key, value) in stud_data_frame.items():
#     print(value)

for(index, rowin stud_data_frame.iterrows):
    print(row)