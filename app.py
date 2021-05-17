from flask import Flask, request, redirect, render_template, url_for
from datetime import date
from markupsafe import escape
from consumer import ValidateTransaction

app = Flask(__name__)

@app.route('/')
@app.route('/<result>')
def index(result=None):
    if result is not None:
        result = escape(result)
    months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
              'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    year = date.today().year
    return render_template("index.html", result=result, months=months, year=year, enumerate=enumerate)


@app.route('/urlSafe/<name>')
def urlSafe(name):
    return f"Hello, {escape(name)}"


@app.route('/consumer', methods=['POST'])
def consumer():
    try :
        pan = request.form['PAN']
        expirationMonth = int(request.form['ExpirationMonth'])
        expirationYear = int(request.form['ExpirationYear'])
        securityCode = request.form['SecurityCode']
        cardBrand = request.form['CardBrand']
        password = request.form['Password']
        transactionAmount = int(request.form['TransactionAmount'])

        result = ValidateTransaction(pan, expirationMonth, expirationYear, securityCode, cardBrand, password, transactionAmount)

        return redirect(url_for('index', result=result))
    except :
        return redirect(url_for('index', result='er'))

    
