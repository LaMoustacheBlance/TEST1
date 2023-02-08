import matplotlib.pyplot as plt
import json
from classes import DataSet


with open('properties.json', 'r', encoding='utf-8') as f:
    properties = json.load(f)
properties["x_data"] = DataSet.str_to_double_list(properties["x_data"])
properties["y_data"] = DataSet.str_to_double_list(properties["y_data"])
print(properties)
for i in range(len(properties["x_data"])):
    print(properties["x_data"][i], properties["y_data"][i])
    plt.plot(properties["x_data"][i], properties["y_data"][i])
plt.title(properties["title"])
plt.xlabel(properties["x_label"])
plt.ylabel(properties["y_label"])
plt.grid(properties["grid"])
plt.show()
