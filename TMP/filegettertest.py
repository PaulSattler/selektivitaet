import os

Auswahl = []

def readLS(path):
    files = os.listdir(path)
    while files != []:
        if (str(files[0])[:-6] == str(files[1])[:-6]) and (str(files[0])[-4:] == '.txt'):
            Auswahl.append(str(files[0])[:-6])
            files.pop(0)
            files.pop(0)
            pass
        else:
            print("Fehler im Dateiverzeichniss")
            files.pop(0)
        pass

    for file in Auswahl:
        datei = open(path + "/" + file,'r')
        #print(datei.read())
    
readLS('C:/Users/PSA/Desktop/selektivitaet/DATA/LS'.strip())
print(Auswahl)