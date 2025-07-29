# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     for row in data:
#         print(row)
import pandas as pd
# data = pd.read_csv("weather_data.csv")
# # print(data)
# # print("------------------------------")
# # print(data["day"])
#
# temp_list = data["temp"].to_list()
# media = data["temp"].sum() / len(temp_list)
# print(media)
#
# meanPandas = data["temp"].mean()
# print(meanPandas)
#
# maxPAndasTemp = data["temp"].max()
# print(maxPAndasTemp)
#
# print(data[data.day == "Monday"])
data = pd.read_csv("esquilos.csv")
esquilos_cinzas = len(data[data["Primary Fur Color"] == "Gray"])
esquilos_canela = len(data[data["Primary Fur Color"] == "Cinnamon"])
esquilos_pretos = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Pelagem" : ["Cinza", "Canela", "Preto"],
    "Quantidade" : [esquilos_cinzas, esquilos_canela, esquilos_pretos]
}

df = pd.DataFrame(data_dict)
df.to_csv("quantidade_esquilos.csv")

print(df)
