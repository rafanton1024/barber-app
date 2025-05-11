# Paso 2: Modelos

from app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'users'  # nombre explícito de tabla

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_barber = db.Column(db.Boolean, default=False)

    # Relaciones
    appointments_made = db.relationship('Appointment', backref='client', foreign_keys='Appointment.user_id', lazy='dynamic')
    appointments_received = db.relationship('Appointment', backref='barber', foreign_keys='Appointment.barber_id', lazy='dynamic')

    def __repr__(self):
        return f'<User {self.username} {"(Barber)" if self.is_barber else ""}>'

class Appointment(db.Model):
    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    barber_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    date = db.Column(db.String(20), nullable=False)
    time = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20), default='Pending')

    def __repr__(self):
        return f'<Appointment {self.date} {self.time} - Client {self.user_id} with Barber {self.barber_id}>'
