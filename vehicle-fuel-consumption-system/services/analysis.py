from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from services.calculations import calculate_efficiency

CHART_DIR = Path("static/charts")
CHART_DIR.mkdir(parents=True, exist_ok=True)

def build_analysis(vehicles, records_by_vehicle):
    detail_rows = []
    for vehicle in vehicles:
        calculated = calculate_efficiency(records_by_vehicle.get(vehicle["vehicle_id"], []))
        for row in calculated:
            row["vehicle_code"] = vehicle["vehicle_code"]
            row["vehicle_type"] = vehicle["vehicle_type"]
            row["fuel_type"] = vehicle["fuel_type"]
            detail_rows.append(row)

    df = pd.DataFrame(detail_rows)
    if df.empty:
        return {"details": [], "vehicle_summary": [], "monthly_summary": [], "invalid": []}

    df["fill_date"] = pd.to_datetime(df["fill_date"])
    df["month"] = df["fill_date"].dt.to_period("M").astype(str)
    valid = df[(df["calculation_note"] == "Full-tank-to-full-tank estimate") &\n                df["mileage_kmpl"].notna() & (df["distance_km"].fillna(0) > 0)].copy()

    vehicle_summary = []
    if not valid.empty:
        for code, group in valid.groupby("vehicle_code"):
            total_distance = np.sum(group["distance_km"].astype(float))
            total_litres = np.sum(group["litres"].astype(float))
            total_cost = np.sum(group["total_cost"].astype(float))
            vehicle_summary.append({
                "vehicle_code": code,
                "mileage": round(float(total_distance / total_litres), 2) if total_litres else None,
                "distance": round(float(total_distance), 2),
                "fuel_cost": round(float(total_cost), 2),
                "cost_per_km": round(float(total_cost / total_distance), 2) if total_distance else None
            })

    monthly_summary = []
    if not valid.empty:
        monthly = valid.groupby("month").agg(
            distance_km=("distance_km", "sum"),
            litres=("litres", "sum"),
            total_cost=("total_cost", "sum")
        ).reset_index()
        monthly["mileage"] = np.where(monthly["litres"] > 0,
                                      monthly["distance_km"] / monthly["litres"], np.nan)
        monthly_summary = [
            {"month": r.month, "distance": round(float(r.distance_km), 2),
             "litres": round(float(r.litres), 2), "cost": round(float(r.total_cost), 2),
             "mileage": round(float(r.mileage), 2) if pd.notna(r.mileage) else None}
            for r in monthly.itertuples()
        ]
        plt.figure(figsize=(8, 4))
        plt.plot(monthly["month"], monthly["mileage"], marker="o")
        plt.title("Monthly Fuel Efficiency")
        plt.xlabel("Month")
        plt.ylabel("Mileage (km/l)")
        plt.xticks(rotation=30)
        plt.tight_layout()
        plt.savefig(CHART_DIR / "monthly_mileage.png")
        plt.close()

        plt.figure(figsize=(8, 4))
        plt.bar(monthly["month"], monthly["total_cost"])
        plt.title("Monthly Fuel Expense")
        plt.xlabel("Month")
        plt.ylabel("Fuel cost")
        plt.xticks(rotation=30)
        plt.tight_layout()
        plt.savefig(CHART_DIR / "monthly_cost.png")
        plt.close()

    invalid = df[df["calculation_note"].str.contains("Invalid", na=False)]
    return {
        "details": df.fillna("").to_dict("records"),
        "vehicle_summary": vehicle_summary,
        "monthly_summary": monthly_summary,
        "invalid": invalid.fillna("").to_dict("records")
    }
