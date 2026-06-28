import requests
import pandas as pd 

schemes={
    "HDFC_Top_100_Direct": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for name, code in schemes.items():
    url = f"https://api.mfapi.in/mf/{code}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data['data'])
        df.to_csv(f"data/raw/{name}_nav.csv", index=False)
        print(f"Data for {name} fetched and saved successfully.")
    else:
        print(f"Failed to fetch data for {name}. Status code: {response.status_code}")