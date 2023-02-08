from typing import List
import json


class DataSet:
    def __init__(self, name: str, x: List[list], y: List[list]):
        if len(x) != len(y):
            raise ValueError("Число наборов x и у должно совпадать")
        for i in range(len(x)):
            if len(x[i]) != len(y[i]):
                raise ValueError("Длины соответствующих наборов длжны сопадать")
        self.name = name
        self.x = x
        self.y = y
        self.args = {"title": "", "x_label": "", "y_label": "", "grid": True}

    def to_write_obj(self):
        properties = {}
        properties.update({"name": self.name, "x_data": str(self.x), "y_data": str(self.y)})
        for key in self.args:
            properties.update({key: self.args[key]})
        print(properties)
        json_object = json.dumps(properties, indent=4)
        with open("properties.json", "w") as outfile:
            outfile.write(json_object)

    @staticmethod
    def str_to_double_list(line: str):
        array, line = [], line[1:-1].split("], ")
        mas = [item.replace("[", "").replace("]", "").split(", ") for item in line]
        for item in mas:
            array.append([float(number) for number in item])
        return array
