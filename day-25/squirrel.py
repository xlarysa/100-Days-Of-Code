import pandas

data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_colors = data["Primary Fur Color"].unique()
fur_colors = fur_colors[1::]
data_dict = {"Fur Color": fur_colors}

occurences = []
for color in fur_colors:
    occurences.append(len(data[data["Primary Fur Color"] == color]))
data_dict["Count"] = occurences

squirrel_count = pandas.DataFrame(data_dict)
squirrel_count.to_csv("./squirrel_count.csv")