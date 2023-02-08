import os


def to_compile_exe(filename: str, no_console=False, windowed=False, icon=''):
    """
    Метод компилирует файл .py в .exe
    """
    param = window = ""
    if type(filename) is not str:
        raise TypeError('Имя .py файля должно быть строкой')
    if type(filename) is not str:
        raise TypeError('Имя .ico файля должно быть строкой')
    if no_console is True:
        param = " --noconsole"
    if windowed is True:
        window = " --windowed"
    if icon != '':
        icon = f" icon={icon} "
    os.system(f"pyinstaller --onefile{param}{window}{icon} {filename}")


to_compile_exe("script.py", no_console=True, windowed=True)
