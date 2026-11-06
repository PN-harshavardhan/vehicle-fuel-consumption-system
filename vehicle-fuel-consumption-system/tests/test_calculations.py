import unittest
from services.calculations import calculate_efficiency

class CalculationTests(unittest.TestCase):
    def test_full_tank_mileage(self):
        records = [
            {"odometer_km": 1000, "litres": 10, "total_cost": 1000, "full_tank_flag": True},
            {"odometer_km": 1200, "litres": 10, "total_cost": 1000, "full_tank_flag": True},
        ]
        result = calculate_efficiency(records)
        self.assertEqual(result[1]["distance_km"], 200)
        self.assertEqual(result[1]["mileage_kmpl"], 20)

    def test_partial_fill_is_marked_approximate(self):
        records = [
            {"odometer_km": 1000, "litres": 10, "total_cost": 1000, "full_tank_flag": True},
            {"odometer_km": 1100, "litres": 5, "total_cost": 500, "full_tank_flag": False},
        ]
        result = calculate_efficiency(records)
        self.assertIn("Approximate", result[1]["calculation_note"])

if __name__ == "__main__":
    unittest.main()
