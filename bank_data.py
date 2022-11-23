import csv, requests


def create_data():
    responce = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
    data = responce.json()
    rates = data[0]['rates']

    with open('currency_rates.csv', 'w', newline='') as scvfile:
        tablewriter = csv.writer(scvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        tablewriter.writerow(rates[0].keys())

        for i, currency in enumerate(rates):
            tablewriter.writerow(rates[i].values())

def get_data():
    data = {}
    with open('currency_rates.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in csvreader:
            data[row[1]]=[row[2], row[3]]
    return data

def get_price(amount, currency_code, action):
    data = get_data()
    if action == 'SELL':
        value = float(data.get(currency_code)[0])
    elif action == 'BUY':
        value = float(data.get(currency_code)[1])
    else:
        value = 0
    
    price = round(float(amount) * value, 2)
    return price

