import os

class Config:
    # Clave secreta para formularios y sesiones
    SECRET_KEY = os.environ.get('SECRET_KEY', 'clave_por_defecto_segura')

    # URI de la base de datos SQLite
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///barber.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Stripe y PayPal: claves extraídas desde variables de entorno (más seguras)
    STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY', '')
    PAYPAL_CLIENT_ID = os.environ.get('PAYPAL_CLIENT_ID', '')
    PAYPAL_CLIENT_SECRET = os.environ.get('PAYPAL_CLIENT_SECRET', '')

