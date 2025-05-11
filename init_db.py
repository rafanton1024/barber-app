#🔧 1. Crear la base de datos de prueba (barber.db)


from app import app, db

with app.app_context():
    db.create_all()
    print("Base de datos creada exitosamente.")
