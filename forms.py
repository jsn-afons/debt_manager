from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, DateField, FloatField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email, Optional

class LoginForm(FlaskForm):
    # Form for user login
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])

class SignUpForm(FlaskForm):
    # Form for user registration
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])

class AddDebtForm(FlaskForm):
    # Form for adding a new debt record
    debtor_name = StringField("Debtor Name", validators=[DataRequired()])
    amount_borrowed = FloatField("Amount Borrowed", validators=[DataRequired()])
    promised_payment_date = DateField("Promised Payment Date", validators=[Optional()])
    status = SelectField("Status", choices=[("Active", "Active"), ("Paid", "Paid"), ("Overdue", "Overdue"), ("Forgiven", "Forgiven")])
    description = TextAreaField("Description", validators=[Optional()])

class EditDebtForm(FlaskForm):
    # Form for editing an existing debt record
    debtor_name = StringField("Debtor Name", validators=[Optional()])
    amount_borrowed = FloatField("Amount Borrowed", validators=[Optional()])
    promised_payment_date = DateField("Promised Payment Date", validators=[Optional()])
    status = SelectField("Status", choices=[("Active", "Active"), ("Paid", "Paid"), ("Overdue", "Overdue"), ("Forgiven", "Forgiven")])
    amount_paid = FloatField("Amount Paid", validators=[Optional()])
    description = TextAreaField("Description", validators=[Optional()])