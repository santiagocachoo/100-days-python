names = ["Mark", "Dylan", "Seth", "Helly", "Irving"]

import random

student_scores = {student:random.randint(0, 100) for student in names}
print(student_scores)

#passed_students = {student:student_scores.get(student) for student in student_scores if student_scores.get(student) > 60}
passed_students = {student:score for (student, score) in student_scores.items() if score > 60}
print(passed_students)

# create dict with number of letters in each word
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words = sentence.split()
result = {word:len(word) for word in words}

# create dictionary with temperatures in fahrenheit
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {day:((weather * 9/5) + 32) for (day, weather) in weather_c.items()}

# iterate over pandas dataframe
student_dict = {
    "student": ["Tung Tung Tung Sahur", "Ballerina Capuccina", "Bombardilo Crocodrilo"],
    "score": [56, 76, 98]
}

#for (key, value) in student_dict.items():
#    print(value)

import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# loop through data frame
for (key, value) in student_data_frame.items():
    print(value)

# loop through each row in data frame
for (index, row) in student_data_frame.iterrows():
    if row.student == "Tung Tung Tung Sahur":
        print(row.score)