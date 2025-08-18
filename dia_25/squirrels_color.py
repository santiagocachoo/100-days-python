import pandas

squirrel_census = pandas.read_csv("/Users/santiagocachoh/Code/100python/dia_25/squirrel_census.csv")

#colors_list = squirrel_census["Primary Fur Color"].to_list()
#
#gray = 0
#cinnamon = 0
#black = 0
#
#for color in colors_list:
#    if color == "Black":
#        black += 1
#    elif color == "Gray":
#        gray += 1
#    elif color == "Cinnamon":
#        cinnamon += 1

gray = len(squirrel_census[squirrel_census["Primary Fur Color"] == "Gray"])
cinnamon = len(squirrel_census[squirrel_census["Primary Fur Color"] == "Cinnamon"])
black = len(squirrel_census[squirrel_census["Primary Fur Color"] == "Black"])


colors_dict = {
    "Fur Color" : ["Gray", "Black", "Cinnamon"],
    "Count" : [gray, black, cinnamon]
}

colors_data = pandas.DataFrame(colors_dict)

print(colors_data)