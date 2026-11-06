from . import get_db

def all_records():
    db = get_db()
    cur = db.cursor(dictionary=True)
    cur.execute("""
        SELECT f.*, v.vehicle_code
        FROM fuel_records f JOIN vehicles v ON f.vehicle_id=v.vehicle_id
        ORDER BY f.fill_date DESC, f.record_id DESC
    """)
    rows = cur.fetchall()
    cur.close()
    db.close()
    return rows

def records_for_vehicle(vehicle_id):
    db = get_db()
    cur = db.cursor(dictionary=True)
    cur.execute("""
        SELECT * FROM fuel_records WHERE vehicle_id=%s
        ORDER BY fill_date, odometer_km, record_id
    """, (vehicle_id,))
    rows = cur.fetchall()
    cur.close()
    db.close()
    return rows

def create_record(vehicle_id, fill_date, odometer, litres, cost, full_tank):
    db = get_db()
    cur = db.cursor(dictionary=True)
    cur.execute("""
        SELECT fill_date, odometer_km FROM fuel_records
        WHERE vehicle_id=%s ORDER BY fill_date DESC, odometer_km DESC, record_id DESC LIMIT 1
    """, (vehicle_id,))
    previous = cur.fetchone()
    if previous:
        if fill_date < previous["fill_date"] or float(odometer) < float(previous["odometer_km"]):
            cur.close()
            db.close()
            raise ValueError("Date and odometer reading must not be earlier/lower than the latest record.")
    cur.close()
    cur = db.cursor()
    cur.execute("""
        INSERT INTO fuel_records
        (vehicle_id, fill_date, odometer_km, litres, total_cost, full_tank_flag)
        VALUES (%s,%s,%s,%s,%s,%s)
    """, (vehicle_id, fill_date, odometer, litres, cost, full_tank))
    db.commit()
    cur.close()
    db.close()
