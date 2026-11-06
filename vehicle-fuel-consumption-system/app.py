from flask import Flask, render_template, redirect, url_for, flash
from config import Config
from models import get_db
from routes.dashboard import dashboard_bp
from routes.vehicles import vehicles_bp
from routes.fuel_records import fuel_bp
from routes.reports import reports_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Verify database connection at startup only when a page is requested.
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(vehicles_bp, url_prefix="/vehicles")
    app.register_blueprint(fuel_bp, url_prefix="/fuel")
    app.register_blueprint(reports_bp, url_prefix="/reports")

    @app.errorhandler(404)
    def not_found(error):
        return render_template("base.html", page_title="Page not found"), 404

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
