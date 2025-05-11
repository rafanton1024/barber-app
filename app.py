# 🔑 Paso 1: Configuración inicial

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from routes import auth, appointments, payments
app.register_blueprint(auth.bp)
app.register_blueprint(appointments.bp)
app.register_blueprint(payments.bp)
from routes import auth, appointments, payments, main
app.register_blueprint(main.bp)
if __name__ == '__main__':
    app.run(debug=True)



