#!/bin/python3

import json
import requests
import pandas as pd

"""
TODO:
    - Rainfall ("Yuen Long")
        - rainfall { data { unit: mm, place: name, max: int, }}
    - Temperature ("Yuen Long Park")
        - temperature { data { place: name, value: int, unit: "C"}}
    - Humidity
        - humidity { value: int }
    - Weather warning 
        - warningMessage {msg1, msg2}
    - Tropical Typhoon
        - tcmessage { msg }
    - UV index

"""


url1 = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=en"

def main():
    r = requests.get(url1)
    if r.status_code == 200:
        data = json.loads(r.text)
    pass

if __name__ == "__main__":
    main