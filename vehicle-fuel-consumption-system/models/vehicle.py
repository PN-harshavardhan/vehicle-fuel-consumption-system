from . import get_db

def all_vehicles():
    db = get_db()
    cur = db.cursor(dictionary=True)
    cur.execute("SELECT * FROM vehicles ORDER BY vehicle_code")
    rows = cur.fetchall()
    cur.close()
    db.close()
    return rows

def create_vehicle(code, vehicle_type, fuel_type):
    db = get_db()
    cur = db.cursor()
    cur.execute(
        "INSERT INTO vehicles (vehicle_code, vehicle_type, fuel_type) VALUES (%s,%s,%s)",
        (code, vehicle_type, fuel_type)
    )
    db.commit()
    cur.close()
    db.close()

def get_vehicle(vehicle_id):
    db = get_db()
    cur = db.cursor(dictionary=True)
    cur.execute("SELECT * FROM vehicles WHERE vehicle_id=%s", (vehicle_id,))
    row = cur.fetchone()
    cur.close()
    db.close()
    return row
