# 📅 /routes/appointments.py – Citas
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from models import Appointment, User
from forms import AppointmentForm
from app import db

bp = Blueprint('appointments', __name__, url_prefix='/appointments')

# Vista del panel de citas del usuario o barbero
@bp.route('/dashboard')
@login_required

def dashboard():
    if current_user.is_barber:
        appointments = Appointment.query.filter_by(barber_id=current_user.id).all()
    else:
        appointments = Appointment.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', appointments=appointments)

# Vista para reservar una cita con un barbero
@bp.route('/book/<int:barber_id>', methods=['GET', 'POST'])
@login_required
def book(barber_id):
    barber = User.query.get_or_404(barber_id)
    if not barber.is_barber:
        flash("Este usuario no es un barbero válido.", "danger")
        return redirect(url_for('appointments.dashboard'))

    form = AppointmentForm()
    if form.validate_on_submit():
        new_appt = Appointment(
            user_id=current_user.id,
            barber_id=barber_id,
            date=str(form.date.data),
            time=str(form.time.data)
        )
        db.session.add(new_appt)
        db.session.commit()
        flash("Cita agendada exitosamente.", "success")
        return redirect(url_for('appointments.dashboard'))

    return render_template('appointment.html', form=form, barber=barber)
