
import requests
import json


def openfile():
    myfile = open("text.txt", "r")
    while myfile:
        line = myfile.readline()
        response = requests.get("https://api.whatsapp.com"+line)
        if response.status_code == 200:
            tablevalue = True
        else:
            tablevalue = False

        text_file = open("write.txt", "a")
        text_file.write(line +" "+tablevalue )
        text_file.close()

        if line == "":
            break

    myfile.close()





if __name__ == '__main__':
    openfile()

