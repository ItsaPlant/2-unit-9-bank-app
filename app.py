import bank_data
from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def myapp():
    amount = None
    value = []
    currency_code = None
    currency_code_from = 'PLN'
    
    if request.method == 'POST':
        action = request.form.get('action')
        currency_code = request.form.get('currency')
        amount = request.form.get('amount')

        if action == 'EXCHANGE':
            currency_code_from = request.form.get('currency_payed')
            currency_code_to = currency_code
            value = bank_data.calculate(amount, currency_code_to, currency_code_from)
            print('xx' + str(value))
        else:
            value = bank_data.calculate_amount(amount, currency_code, action)
            print('x' + str(value))

    return render_template('currency.html', amount=amount, value=value, currency=currency_code, currency_from=currency_code_from)

if __name__ == '__main__':
    app.run(debug=True)