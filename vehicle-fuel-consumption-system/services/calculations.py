def calculate_efficiency(records):
    """
    Returns one row per record.
    Full-tank method: distance between consecutive full-tank records / litres
    added at the ending full-tank record. Partial fills are not treated as
    exact tank-to-tank consumption; they receive an explicitly approximate
    distance-per-litre estimate when a previous reading exists.
    """
    output = []
    previous = None

    for record in records:
        row = dict(record)
        row["distance_km"] = None
        row["mileage_kmpl"] = None
        row["cost_per_km"] = None
        row["calculation_note"] = "First reading: no previous odometer value"

        if previous is not None:
            distance = float(record["odometer_km"]) - float(previous["odometer_km"])
            if distance >= 0:
                row["distance_km"] = distance
                if record["full_tank_flag"] and previous["full_tank_flag"]:
                    litres = float(record["litres"])
                    row["mileage_kmpl"] = distance / litres if litres > 0 else None
                    row["calculation_note"] = "Full-tank-to-full-tank estimate"
                elif float(record["litres"]) > 0:
                    row["mileage_kmpl"] = distance / float(record["litres"])
                    row["calculation_note"] = "Approximate only: partial fill involved"
                if row["mileage_kmpl"] and row["mileage_kmpl"] > 0:
                    row["cost_per_km"] = float(record["total_cost"]) / distance if distance > 0 else None
            else:
                row["calculation_note"] = "Invalid: odometer decreased"

        output.append(row)
        previous = record

    return output
