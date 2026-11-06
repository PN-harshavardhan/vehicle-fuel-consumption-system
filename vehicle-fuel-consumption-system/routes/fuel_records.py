from datetime import date
from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.vehicle import all_vehicles
from models.fuel_record import all_records, create_record

fuel_bp = Blueprint("fuel", __name__)

@fuel_bp.route("/")
def list_fuel():
    return render_template("fuel_records.html", records=all_records())

@fuel_bp.route("/add", methods=["GET", "POST"])
def add_fuel():
    vehicles = all_vehicles()
    if request.method == "POST":
        try:
            vehicle_id = int(request.form["vehicle_id"])
            fill_date = date.fromisoformat(request.form["fill_date"])
            odometer = float(request.form["odometer_km"])
            litres = float(request.form["litres"])
            cost = float(request.form["total_cost"])
            full_tank = request.form.get("full_tank_flag") == "on"

            if odometer < 0 or litres <= 0 or cost < 0:
                raise ValueError("Odometer must be non-negative, litres must be greater than zero, and cost cannot be negative.")
            create_record(vehicle_id, fill_date, odometer, litres, cost, full_tank)
            flash("Fuel record saved.", "success")
            return redirect(url_for("fuel.list_fuel"))
        except ValueError as exc:
            flash(str(exc), "danger")
        except Exception as exc:
            flash(f"Could not save record: {exc}", "danger")
    return render_template("add_fuel.html", vehicles=vehicles)
