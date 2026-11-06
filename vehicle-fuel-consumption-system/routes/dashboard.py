from flask import Blueprint, render_template
from models.vehicle import all_vehicles
from models.fuel_record import records_for_vehicle
from services.analysis import build_analysis

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/")
def dashboard():
    vehicles = all_vehicles()
    records = {v["vehicle_id"]: records_for_vehicle(v["vehicle_id"]) for v in vehicles}
    analysis = build_analysis(vehicles, records)
    return render_template("dashboard.html", vehicles=vehicles, analysis=analysis)
