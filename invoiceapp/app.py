import smtplib
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import urllib.request
import json
import sqlite3
import datetime
import random
from flask import Flask, render_template, request, send_file, redirect
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, request, send_file
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import io

app = Flask(__name__)
app.secret_key = 'expressdeal2026'
limiter = Limiter(key_func=get_remote_address)
limiter.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
def init_db():
    conn = sqlite3.connect('invoices.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS invoices
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  invoice_number TEXT,
                  date TEXT,
                  seller_name TEXT,
                  client_name TEXT,
                  total REAL)''')
    conn.commit()
    conn.close()
def init_db():
    conn = sqlite3.connect('invoices.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS invoices
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  invoice_number TEXT,
                  date TEXT,
                  seller_name TEXT,
                  client_name TEXT,
                  total REAL,
                  user_id INTEGER)''')
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  email TEXT UNIQUE,
                  password_hash TEXT)''')
    conn.commit()
    conn.close()
init_db()
class User(UserMixin):
    def __init__(self, id, email):
        self.id = id
        self.email = email

@login_manager.user_loader
def load_user(user_id):
    conn = sqlite3.connect('invoices.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = c.fetchone()
    conn.close()
    if user:
        return User(user[0], user[1])
    return None
def send_invoice_email(to_email, client_name, pdf_buffer, invoice_number, sender_email, sender_name):
    app_password = "wyxi pwjl twfx eydy"
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = f"Invoice {invoice_number} from {sender_name}"
    
    body = f"Dear {client_name},\n\nPlease find your invoice {invoice_number} attached.\n\nBest regards,\n{sender_name}"
    msg.attach(MIMEText(body, 'plain'))
    
    attachment = MIMEBase('application', 'octet-stream')
    attachment.set_payload(pdf_buffer.getvalue())
    encoders.encode_base64(attachment)
    attachment.add_header('Content-Disposition', f'attachment; filename="invoice_{invoice_number}.pdf"')
    msg.attach(attachment)
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, app_password)
        server.sendmail(sender_email, to_email, msg.as_string())
        server.quit()
        return True
    except:
        return False
@app.route('/')
def home():
    return render_template('landing.html')

@app.route('/app')
def app_page():
    return render_template('index.html')

@app.route('/invoice', methods=['POST'])
@limiter.limit("10 per minute")
def invoice():
    seller_name = request.form['seller_name']
    seller_tax = request.form['seller_tax']
    seller_phone = request.form['seller_phone']
    seller_email = request.form['seller_email']
    client_name = request.form['client_name']
    services = request.form.getlist('service[]')
    prices = request.form.getlist('price[]')
    prices = [float(p) for p in prices]
    subtotal = sum(prices)
    vat = subtotal * 0.20
    total = subtotal + vat
    # Get live currency rates
    try:
        url = "https://api.exchangerate-api.com/v4/latest/MAD"
        response = urllib.request.urlopen(url)
        rates = json.loads(response.read())
        usd = round(total * rates['rates']['USD'], 2)
        eur = round(total * rates['rates']['EUR'], 2)
        currency_line = f"≈ {usd} USD / {eur} EUR"
    except:
        currency_line = ""
    invoice_number = f"ED-{random.randint(1000, 9999)}"
    invoice_date = datetime.datetime.now().strftime("%d/%m/%Y")
    # Create PDF in memory
    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    # Title
    pdf.setFont("Helvetica-Bold", 24)
    pdf.drawString(50, height - 60, "EXPRESSDEAL")
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, height - 80, "Invoice")

    # Invoice number and date
    pdf.setFont("Helvetica", 11)
    pdf.drawString(50, height - 100, f"Invoice #: {invoice_number}")
    pdf.drawString(50, height - 118, f"Date: {invoice_date}")

    # Line
    pdf.line(50, height - 140, width - 50, height - 140)

    # Seller and client
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(50, height - 170, "From:")
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, height - 190, seller_name)
    pdf.drawString(50, height - 208, f"Tax ID: {seller_tax}")

    
    pdf.drawString(50, height - 190, seller_name)
    pdf.drawString(50, height - 208, f"Tax ID: {seller_tax}")
    pdf.drawString(50, height - 226, f"Phone: {seller_phone}")
    pdf.drawString(50, height - 244, f"Email: {seller_email}")
    # Line
    pdf.line(50, height - 310, width - 50, height - 310)

    # Services
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(50, height - 340, "Services:")
    y = height - 360
    for i, (service, price) in enumerate(zip(services, prices)):
        pdf.setFont("Helvetica", 12)
        pdf.drawString(50, y, f"- {service}")
        pdf.drawString(400, y, f"{price} MAD")
        y -= 20

    # Line
    pdf.line(50, y - 10, width - 50, y - 10)

    # Prices
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, y - 35, f"Subtotal:     {subtotal} MAD")
    pdf.drawString(50, y - 55, f"VAT (20%):    {vat} MAD")
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(50, y - 85, f"TOTAL:        {total} MAD")
    pdf.setFont("Helvetica", 11)
    pdf.drawString(50, y - 105, currency_line)
    # Footer
    pdf.setFont("Helvetica", 10)
    pdf.drawString(50, 50, "Generated by ExpressDeal")

    pdf.save()
    buffer.seek(0)
    # Save to database
    conn = sqlite3.connect('invoices.db')
    c = conn.cursor()
    c.execute("INSERT INTO invoices (invoice_number, date, seller_name, client_name, total, user_id) VALUES (?, ?, ?, ?, ?, ?)",
          (invoice_number, invoice_date, seller_name, client_name, total, current_user.id))
    conn.commit()
    conn.close()
    # Send email if client email provided
    if seller_email and client_name:
        buffer.seek(0)
        email_sent = send_invoice_email(
            seller_email,
            client_name,
            buffer,
            invoice_number,
            seller_email,
            seller_name
        )
        buffer.seek(0)
    return send_file(
        buffer,
        as_attachment=True,
        download_name=f"invoice_{client_name}.pdf",
        mimetype='application/pdf'
    )
@app.route('/history')
@login_required
def history():
    conn = sqlite3.connect('invoices.db')
    c = conn.cursor()
    c.execute("SELECT * FROM invoices WHERE user_id = ? ORDER BY id DESC", (current_user.id,))
    invoices = c.fetchall()
    conn.close()
    return render_template('history.html', invoices=invoices)
if __name__ == '__main__':
    app.run(debug=True)
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        password_hash = generate_password_hash(password)
        try:
            conn = sqlite3.connect('invoices.db')
            c = conn.cursor()
            c.execute("INSERT INTO users (email, password_hash) VALUES (?, ?)",
                      (email, password_hash))
            conn.commit()
            conn.close()
            return redirect('/login')
        except:
            return "Email already exists. <a href='/register'>Try again</a>"
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
@limiter.limit("5 per minute")
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        conn = sqlite3.connect('invoices.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = c.fetchone()
        conn.close()
        if check_password_hash(user[2], password):
            login_user(User(user[0], user[1]))
            return redirect('/app')
        else:
            return "Wrong email or password. <a href='/login'>try again</a>"
    return render_template('login.html')
           
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')
if __name__ == '__main__':
    app.run(debug=True)
