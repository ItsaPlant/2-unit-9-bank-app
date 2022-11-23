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
        amount = request.form.get('amount')

        value = bank_data.calculate_amount(amount, currency_code, action)
        print(value)

    return render_template('currency.html', amount=amount, value=value, currency=currency_code)

if __name__ == '__main__':
    app.run(debug=True)