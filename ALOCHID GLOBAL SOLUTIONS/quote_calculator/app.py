from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/quote')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    purchase_price = float(request.form['purchase_price'])
    quantity = int(request.form['quantity'])
    freight_costs = float(request.form['freight_costs'])
    insurance = float(request.form['insurance'])
    handling_fees = float(request.form['handling_fees'])
    import_duties = float(request.form['import_duties'])
    customs_fees = float(request.form['customs_fees'])
    transportation = float(request.form['transportation'])
    storage = float(request.form['storage'])
    packaging = float(request.form['packaging'])
    documentation = float(request.form['documentation'])
    bank_charges = float(request.form['bank_charges'])
    profit_margin_percentage = float(request.form['profit_margin'])

    total_purchase_price = purchase_price * quantity
    total_landed_cost = (total_purchase_price + freight_costs + insurance + handling_fees + 
                         import_duties + customs_fees + transportation + storage + packaging + 
                         documentation + bank_charges)

    profit_margin = total_landed_cost * (profit_margin_percentage / 100)
    selling_price = total_landed_cost + profit_margin

    return render_template('index.html', total_landed_cost=total_landed_cost, 
                           profit_margin=profit_margin, selling_price=selling_price)

if __name__ == '__main__':
    app.run(debug=True)
