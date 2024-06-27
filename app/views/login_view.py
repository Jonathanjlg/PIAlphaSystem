from app import app
from flask import Flask, render_template,redirect,url_for,flash, request #renderização
from flask import session
from app.models.login_model import Technician
from app import db 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///technicians.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        technician = Technician.query.filter_by(email=email).first()
        if technician and technician.check_password(password):
            session['technician_id'] = technician.id
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password')
    return render_template('login_adm.html')

@app.route('/dashboard')
def dashboard():
    if 'technician_id' not in session:
        return redirect(url_for('login'))
    return 'Welcome to your dashboard!'
