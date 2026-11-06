USE fuel_analysis;

INSERT IGNORE INTO vehicles (vehicle_code, vehicle_type, fuel_type) VALUES
('CAR-001', 'Hatchback', 'Petrol'),
('BIKE-001', 'Motorcycle', 'Petrol'),
('CAR-002', 'Sedan', 'Diesel');

-- Sample readings are chronological for each vehicle.
INSERT INTO fuel_records
(vehicle_id, fill_date, odometer_km, litres, total_cost, full_tank_flag)
SELECT vehicle_id, '2026-01-03', 10000, 30, 3150, TRUE FROM vehicles WHERE vehicle_code='CAR-001';
INSERT INTO fuel_records
(vehicle_id, fill_date, odometer_km, litres, total_cost, full_tank_flag)
SELECT vehicle_id, '2026-01-15', 10420, 28, 2940, TRUE FROM vehicles WHERE vehicle_code='CAR-001';
INSERT INTO fuel_records
(vehicle_id, fill_date, odometer_km, litres, total_cost, full_tank_flag)
SELECT vehicle_id, '2026-02-02', 10850, 29, 3045, TRUE FROM vehicles WHERE vehicle_code='CAR-001';
INSERT INTO fuel_records
(vehicle_id, fill_date, odometer_km, litres, total_cost, full_tank_flag)
SELECT vehicle_id, '2026-01-05', 2000, 8, 880, TRUE FROM vehicles WHERE vehicle_code='BIKE-001';
INSERT INTO fuel_records
(vehicle_id, fill_date, odometer_km, litres, total_cost, full_tank_flag)
SELECT vehicle_id, '2026-01-18', 2240, 7, 770, TRUE FROM vehicles WHERE vehicle_code='BIKE-001';
INSERT INTO fuel_records
(vehicle_id, fill_date, odometer_km, litres, total_cost, full_tank_flag)
SELECT vehicle_id, '2026-01-08', 5000, 40, 3800, TRUE FROM vehicles WHERE vehicle_code='CAR-002';
INSERT INTO fuel_records
(vehicle_id, fill_date, odometer_km, litres, total_cost, full_tank_flag)
SELECT vehicle_id, '2026-01-22', 5480, 38, 3610, TRUE FROM vehicles WHERE vehicle_code='CAR-002';
