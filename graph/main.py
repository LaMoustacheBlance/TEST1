import keyboard
import clipboard
import time
from classes import *
from win10toast import ToastNotifier
import os

base_param = {"x_data": [], "y_data": [], "x_title": "", "y_title": "", "title": ""}
step_waiting = 0.2
ds_quantity = 0
ds = []
toaster = ToastNotifier()


def data_processing(data: str):
    """
    Фунгкция переволит столбец данных в нужный формат
    :param data: входной столбец
    :return: заголок, столбец данных
    """
    mas, title = [], ""
    data = data.replace("\r", "").split("\n")
    for item in data:
        if item != "":
            title = item
            break
    for item in data:
        if item != '' and item != title:
            mas.append(float(item.replace(",", ".")))
    return title, mas


def to_process(arg: str):
    """
    Функция пополняет текущий набор данных новыми
    :param arg: определяет куда добавляется новый столбец данных (x или у)
    :return:
    """
    global step_waiting, base_param, toaster
    clipboard.copy("")
    start_time = time.time()
    while clipboard.paste() == "":
        time.sleep(step_waiting)
        keyboard.send("ctrl+c")
        if time.time() - start_time > 1:
            raise TimeoutError
    data = data_processing(clipboard.paste())
    print(data)
    if arg == "x":
        toaster.show_toast("CapybaraGraph", "Выбран набор данных X")
        print("x")
        base_param["x_label"] = data[0]
        base_param["x_data"].append(data[1])
    if arg == "y":
        toaster.show_toast("CapybaraGraph", "Выбран набор данных Y")
        print("y")
        base_param["y_label"] = data[0]
        base_param["y_data"].append(data[1])


def to_clean_all():
    """
    Метод для очистки всех наборов данных
    :return:
    """
    global base_param, ds, toaster
    base_param["x_data"], base_param["y_data"], ds = [], [], []
    toaster.show_toast("CapybaraGraph", "Все наборы данных были сброшены!!!")


def to_create_dataset():
    """
    Метод создает новый набор данных
    """
    global ds_quantity, base_param
    print(ds_quantity)
    print(base_param["x_data"], base_param["y_data"])
    ds.append(DataSet(f"ds_{str(ds_quantity)}", base_param["x_data"], base_param["y_data"]))
    ds[0].args["x_label"], ds[0].args["y_label"] = base_param["x_label"], base_param["y_label"]
    ds_quantity += 1
    ds[0].to_write_obj()
    base_param["x_data"] = base_param["y_data"] = []
    os.startfile("script.py")  # или os.startfile("script.exe") если все уже упаковано в .exe


keyboard.add_hotkey("alt+1", lambda: to_process("x"))
keyboard.add_hotkey("alt+2", lambda: to_process("y"))
keyboard.add_hotkey("alt+3", lambda: to_clean_all())
keyboard.add_hotkey("alt+s", lambda: to_create_dataset())
keyboard.wait()
