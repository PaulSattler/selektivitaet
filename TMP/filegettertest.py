import os

OptionListLS = []

def readLS(path):
    try:
        files = os.listdir(path)
        while files != []:
            for file in files:
                files.remove(file)
                for checkfile in files:
                    if (str(file)[:-6] == str(checkfile)[:-6]) and (str(file)[-4:] == '.txt') and (str(checkfile)[-4:] == '.txt'):
                        OptionListLS.append(str(file)[:-6])
                        files.remove(checkfile)
        OptionListLS.sort()
    except Exception:
        print(Exception)

readLS('C:/Users/PSA/Desktop/selektivitaet/DATA/LS'+'/'.strip())
                                                    #^?


print(OptionListLS)