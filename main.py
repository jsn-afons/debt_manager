from flask import Flask, request, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from database import db, User, Debtors
from forms import *
import os
from dotenv import load_dotenv
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from datetime import datetime

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///debt_collector.db'
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            email = form.email.data
            user = db.session.execute(db.select(User).where(User.email == email)).scalar_one_or_none()
            if user is None:
                flash('User not found!\n\nPlease sign up')
                return redirect(url_for('signup'))
            elif user and user.verify_password(form.password.data):
                #login users
                login_user(user)
                return redirect(url_for('dashboard'))
            else:
                flash('Invalid email or password')
    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        new_user = User(
            first_name=form.first_name.data.title(),
            last_name=form.last_name.data.title(),
            email=form.email.data.lower(),
            password=form.password.data
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    my_id = current_user.id
    my_debts = db.session.execute(db.select(Debtors).where(Debtors.user_id == my_id)).scalars().all()
    return render_template('index.html', debts=my_debts)

@app.route('/add_debt', methods=['GET', 'POST'])
def add_debt():
    form = AddDebtForm()
    if form.validate_on_submit():
        new_debt = Debtors(
            debtor_name = form.debtor_name.data,
            amount_borrowed = form.amount_borrowed.data,
            promised_payment_date = form.promised_payment_date.data,
            date_borrowed = datetime.now(),
            status = form.status.data,
            description = form.description.data,
            user_id = current_user.id
        )
        db.session.add(new_debt)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('add_debt.html', form=form)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)