from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/invoice', methods=['POST'])
def invoice():
    seller_name = request.form['seller_name']
    client_name = request.form['client_name']
    service = request.form['service']
    price = float(request.form['price'])
    vat = price * 0.20
    total = price + vat
    return f"""
    <h1>INVOICE - ExpressDeal</h1>
    <p>From: {seller_name}</p>
    <p>To: {client_name}</p>
    <p>Service: {service}</p>
    <p>Price: {price} MAD</p>
    <p>VAT (20%): {vat} MAD</p>
    <p>Total: {total} MAD</p>
    """
if __name__ == '__main__':
    app.run(debug=True)
