# 💳 /routes/payments.py – Pagos con Stripe

import os
import stripe
from flask import Blueprint, request, redirect, url_for, current_app

bp = Blueprint('payments', __name__, url_prefix='/payment')

# Usar configuración directamente desde el entorno de Flask
@bp.before_app_first_request
def setup_stripe():
    stripe.api_key = current_app.config['STRIPE_SECRET_KEY']

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
                    'unit_amount': 1500,  # $15.00 en centavos
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=url_for('payments.success', _external=True),
            cancel_url=url_for('payments.cancel', _external=True),
        )
        return redirect(session.url, code=303)
    except Exception as e:
        return f"Error creando sesión de pago: {str(e)}", 500

@bp.route('/success')
def success():
    return "<h2>✅ Pago exitoso. ¡Gracias por tu cita!</h2>"

@bp.route('/cancel')
def cancel():
    return "<h2>❌ Pago cancelado. Puedes intentarlo de nuevo.</h2>"
