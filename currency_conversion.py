import urllib.request

import json

import pandas as pd

url_link = 'https://api.exchangeratesapi.io/history?start_at=2019-07-02&end_at=2019-09-30&base=INR'

json_file = urllib.request.urlopen(url_link)
datum = json.load(json_file)


currency=pd.DataFrame(datum['rates'])
currency=currency.T.sort_index()


currency.insert(0,'base_currency',"INR")

print (currency)