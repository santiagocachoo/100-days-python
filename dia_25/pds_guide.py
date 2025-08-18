#with open("/Users/santiagocachoh/Code/100python/dia_25/weather_data.csv") as file:
#    data = file.readlines()
#    print(data)

#import csv
#
#with open("/Users/santiagocachoh/Code/100python/dia_25/weather_data.csv") as file:
#    data = csv.reader(file)
#    temperatures = []
#    for row in data:
#        if row[1] != "temp":
#            temperatures.append(int(row[1]))
#    print(temperatures)



import pandas

data = pandas.read_csv("/Users/santiagocachoh/Code/100python/dia_25/weather_data.csv")

#print(type(data))
#print(data)

# TURNING DATA DO DICTIONARY
#data_dict = data.to_dict()
#print(data_dict)

# TURNING DATA TO LIST
#temp_list = data["temp"].to_list()

# calculate average
#average = sum(temp_list)/(len(temp_list))
#print(f"The average weather is: {average}")    

# average with pandas method
#print(f"The average weather is: {data["temp"].mean()}")

# maximum value
#print(f"The maximum weather is: {data["temp"].max()}")

# get data in columns
#print(data["condition"])
#print(data.condition)

# get data in row
#print(data[data.day == "Monday"])

# CHALLENGE = get row of data with highest temp
#print(data[data.temp == data.temp.max()])

## CHALLENTE = turn temp in monday to celcius
#monday = data[data.day == "Monday"]
#print(monday.condition)

#monday_temp = monday.temp[0]

#monday_fahrenheit = (monday_temp * (9/5) + 32)
#print(monday_fahrenheit)

# create dataframe from scratch
data_dict = {
    "students" : ["Pedro", "Juan", "Francisco"],
    "scores" : [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)

    
