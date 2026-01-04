from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Date, Float, ForeignKey, Enum
from datetime import datetime, date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

STATUS_OPTIONS = ("Active", "Paid", "Overdue", "Forgiven")

db = SQLAlchemy()

class Base(DeclarativeBase):
    pass

class User(db.Model, UserMixin):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(250))
    last_name: Mapped[str] = mapped_column(String(250))
    email: Mapped[str] = mapped_column(String(250), unique=True)
    _password_hash: Mapped[str] = mapped_column(String(250))
    @property
    def password(self):
        raise AttributeError("password is not a readable attribute")

    @password.setter
    def password(self, password):
        self._password_hash = generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self._password_hash, password)

    debtors = relationship("Debtors", backref="user")
        



class Debtors(db.Model):
    __tablename__ = "debtors"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    debtor_name: Mapped[str] = mapped_column(String(250), nullable=False)
    date_borrowed: Mapped[date] = mapped_column(Date) #Filled by me automatically 
    amount_borrowed: Mapped[float] = mapped_column(Float)
    promised_payment_date: Mapped[date] = mapped_column(Date, nullable=True, default=datetime.utcnow)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    status: Mapped[str] = mapped_column(Enum(*STATUS_OPTIONS, name="status_types"), nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=True)

