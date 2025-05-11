# 🧾 Paso 3: Formularios (WTForms)

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, TimeField
from wtforms.validators import DataRequired, Email, Length

class LoginForm(FlaskForm):
    email = StringField('Correo Electrónico', validators=[
        DataRequired(message="El correo es obligatorio."),
        Email(message="Ingrese un correo válido.")
    ])
    password = PasswordField('Contraseña', validators=[
        DataRequired(message="La contraseña es obligatoria.")
    ])
    submit = SubmitField('Iniciar Sesión')

class RegisterForm(FlaskForm):
    username = StringField('Nombre de Usuario', validators=[
        DataRequired(message="El nombre de usuario es obligatorio."),
        Length(min=3, max=50, message="Debe tener entre 3 y 50 caracteres.")
    ])
    email = StringField('Correo Electrónico', validators=[
        DataRequired(message="El correo es obligatorio."),
        Email(message="Ingrese un correo válido.")
    ])
    password = PasswordField('Contraseña', validators=[
        DataRequired(message="La contraseña es obligatoria."),
        Length(min=6, message="Debe tener al menos 6 caracteres.")
    ])
    is_barber = BooleanField('¿Eres barbero?')
    submit = SubmitField('Registrarse')

class AppointmentForm(FlaskForm):
    date = DateField('Fecha de la Cita', format='%Y-%m-%d', validators=[
        DataRequired(message="La fecha es obligatoria.")
    ])
    time = TimeField('Hora de la Cita', format='%H:%M', validators=[
        DataRequired(message="La hora es obligatoria.")
    ])
    submit = SubmitField('Reservar Cita')
