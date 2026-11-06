# Vehicle Fuel Consumption Analysis System

A Flask + MySQL application for managing vehicles and fuel purchases, calculating fuel efficiency, and analyzing fuel expenses.

## Features
- Add and list vehicles.
- Record fill date, odometer, litres, cost, and full-tank status.
- Reject zero/negative litres and decreasing chronological odometer/date entries.
- Calculate full-tank-to-full-tank mileage.
- Clearly label partial-fill calculations as approximate.
- Vehicle-wise and month-wise summaries.
- Monthly mileage and fuel-cost charts.
- Invalid-reading report.

## Requirements
- Python 3.11 or 3.12 recommended.
- MySQL Server 8.x.
- Git.

## Setup on Windows / VS Code

1. Extract this project ZIP and open the `vehicle-fuel-consumption-system` folder in VS Code.
2. Open Terminal > New Terminal. Confirm the terminal is in the project folder:
   ```powershell
   dir
   ```
   You should see `app.py`, `requirements.txt`, and the `database` folder.
3. Create and activate a virtual environment:
   ```powershell
   py -3.12 -m venv .venv
   .venv\\Scripts\\Activate.ps1
   ```
   If Python 3.12 is not installed, install Python 3.12 first. Newer Python versions may not yet have compatible prebuilt wheels for every scientific package.
4. Install dependencies:
   ```powershell
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```
5. Create the database. Open MySQL Workbench or MySQL command line and run:
   ```sql
   SOURCE C:/full/path/to/vehicle-fuel-consumption-system/database/schema.sql;
   SOURCE C:/full/path/to/vehicle-fuel-consumption-system/database/sample_data.sql;
   ```
   Replace the path with your actual extracted folder path. In MySQL Workbench, you can instead open each `.sql` file and click the lightning bolt.
6. Copy `.env.example` to `.env` in the project root. Edit `.env` and enter your MySQL password:
   ```env
   MYSQL_USER=root
   MYSQL_PASSWORD=your_actual_password
   MYSQL_DATABASE=fuel_analysis
   ```
7. Start Flask:
   ```powershell
   python app.py
   ```
8. Open this address in your browser:
   `http://127.0.0.1:5000`

## Run tests
```powershell
python -m unittest discover -s tests
```

## Mileage method and limitations
- For two consecutive full-tank records, distance = current odometer - previous odometer. Mileage = distance / litres added at the current fill.
- If either reading is a partial fill, distance / litres added is displayed as approximate only. It is not a precise tank-consumption measurement because the fuel level may not have returned to the same starting level.
- The first reading has no previous reading, so no mileage is calculated.
- Records must be entered in chronological order for each vehicle. Correct an earlier mistake in the database before entering later readings.

## Git and GitHub

From the project root:
```powershell
git init
git add .
git commit -m "Initial commit: vehicle fuel consumption analysis system"
git branch -M main
```
Create an empty repository on GitHub, then copy its HTTPS URL and run:
```powershell
git remote add origin https://github.com/YOUR-USERNAME/vehicle-fuel-consumption-system.git
git push -u origin main
```
Do not commit `.env`; it contains your database password. `.gitignore` excludes it.
