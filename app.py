import bank_data
from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def myapp():
    amount = None
    value = []
    currency_code = None
    
    if request.method == 'POST':
        action = request.form.get('action')
        currency_code = request.form.get('currency')
        amount = float(request.form.get('amount'))

        value = str(bank_data.get_price(amount, currency_code, action))

    return render_template('currency.html', amount=amount, value=value, currency=currency_code)

if __name__ == '__main__':
    app.run(debug=True)