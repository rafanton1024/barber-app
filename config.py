import os

class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///barber.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STRIPE_SECRET_KEY = 'your_stripe_secret_key'
    PAYPAL_CLIENT_ID = 'your_paypal_client_id'
    PAYPAL_CLIENT_SECRET = 'your_paypal_client_secret'
