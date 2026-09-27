# import csv
# with open("./weather_data.csv", "r") as file:
#     data = csv.reader(file)
#     temperatures = []
#
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

data = pandas.read_csv("./weather_data.csv")
data_dict = data.to_dict()

# print(data["temp"].mean())
# print(data["temp"].max())
#
# print(data.condition)
#
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.temp[0] * (9/5) + 32)

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65],
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")