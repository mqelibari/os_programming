import json

data = {"Otto":
            {
                "https://www.otto.de/technik/heimkino/": {
                    "name": "Samsung HW-N400/ZG 2.0 Soundbar (Bluetooth)",
                    "price": "139,00"
                }
            }
        }

data2 = {"Otto":{
                    "https://www.otto.de/technik/heimkino/": {
                        "name": "LG DSN4 2.1 2.1 Soundsystem (Bluetooth, 300 W)",
                        "price": "165,00"
                    }
                }
         }

datas_for_json = [data]

with open("name_price.json", "w") as f:
    json.dump(data, f)
