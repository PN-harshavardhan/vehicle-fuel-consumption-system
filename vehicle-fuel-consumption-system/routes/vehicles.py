from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.vehicle import all_vehicles, create_vehicle

vehicles_bp = Blueprint("vehicles", __name__)

@vehicles_bp.route("/")
def list_vehicles():
    return render_template("vehicles.html", vehicles=all_vehicles())

@vehicles_bp.route("/add", methods=["GET", "POST"])
def add_vehicle():
    if request.method == "POST":
        code = request.form.get("vehicle_code", "").strip()
        vehicle_type = request.form.get("vehicle_type", "").strip()
        fuel_type = request.form.get("fuel_type", "").strip()
        if not code or not vehicle_type or not fuel_type:
            flash("Please complete every field.", "danger")
        else:
            try:
                create_vehicle(code, vehicle_type, fuel_type)
                flash("Vehicle added successfully.", "success")
                return redirect(url_for("vehicles.list_vehicles"))
            except Exception as exc:
                flash(f"Could not add vehicle: {exc}", "danger")
    return render_template("add_vehicle.html")
