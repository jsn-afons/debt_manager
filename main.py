from flask import Flask, request, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from database import db, User, Debtors

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///debt_collector.db'
db.init_app(app)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)