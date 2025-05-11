# 💳 /routes/payments.py – Pagos con Stripe

import stripe
from flask import Blueprint, request, redirect, url_for
from app import app

bp = Blueprint('payments', __name__, url_prefix='/payment')

stripe.api_key = app.config['STRIPE_SECRET_KEY']

@bp.route('/checkout', methods=['POST'])
def checkout():
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': 'Barber Appointment',
                },
                'unit_amount': 1500,  # $15.00 in cents
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://localhost:5000/payment/success',
        cancel_url='http://localhost:5000/payment/cancel',
    )
    return redirect(session.url, code=303)

@bp.route('/success')
def success():
    return "Payment successful!"

@bp.route('/cancel')
def cancel():
    return "Payment cancelled."
