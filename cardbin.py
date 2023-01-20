import requests
import json
import certifi

def bin_check_dop(bin):
    url = 'https://mrbin.io/bins/bin/getFull'
    headers = {'Content-Type': 'application/json', 'Authorization': 'Basic bXJiaW5pbzp0ZXN0X21yYmluaW8='}
    data = {'fullBin': bin}
    try:
        r = requests.post(url=url, headers=headers, data=json.dumps(data), verify=str(certifi.where()))
        if r.status_code == 200:
            r = r.json()
            data = {
                'bin': bin,
                'BankName': r['bankName'],
                'System': r['paymentSystem'],
                'Country1': r['countryAlpha2'],
                'Country2': r['countryAlpha3'],
                'Category': r['product']['category']
            }
        return data
    except:
        pass

print(bin_check_dop('<Card_bin_number_of_your_card>'))
