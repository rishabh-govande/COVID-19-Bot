import requests
from win10toast import ToastNotifier
import json
import time

def update():
    r = requests.get("https://coronavirus-19-api.herokuapp.com/all")
    data = r.json()
    text = f'Active Cases: {data["cases"]} \n Deaths: {data["deaths"]} \n Recovered: {data["recovered"]}'

    while True:
        toast = ToastNotifier()
        toast.show_toast("COVID-19 World wide Updates", text, duration = 40)
        time.sleep(60)

update()