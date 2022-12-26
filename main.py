
import requests
import json


def openfile():
    myfile = open("text.txt", "r")
    while myfile:
        line = myfile.readline()
        response = requests.get("https://api.whatsapp.com/send/?phone=%2B91"+line+"8249129309&text&type=phone_number&app_absent=0");
        if response.status_code == 200:
            text_file = open("write.txt", "a")
            text_file.write(line + " True")

        else:
            text_file = open("write.txt", "a")
            text_file.write(line + " False")


        if line == "":
            break
    myfile.close()
    text_file.close()







openfile()

