# 💳 /routes/payments.py – Pagos con Stripe
import stripe
import os
from flask import Blueprint, request, redirect, url_for, jsonify
from app import app

bp = Blueprint('payments', __name__, url_prefix='/payment')

# Configurar Stripe con clave secreta desde variables de entorno
stripe.api_key = os.environ.get("STRIPE_SECRET_KEY")

@bp.route('/checkout', methods=['POST'])
def checkout():
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': 'Barber Appointment',
                    },
                    'unit_amount': 1500,  # $15.00
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=url_for('payments.success', _external=True),
            cancel_url=url_for('payments.cancel', _external=True),
        )
        return redirect(session.url, code=303)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@bp.route('/success')
def success():
    return "¡Pago realizado con éxito!"

@bp.route('/cancel')
def cancel():
    return "El pago fue cancelado."
