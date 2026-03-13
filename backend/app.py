from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from dotenv import load_dotenv

from config import Config
from db import db

# --- import all blueprints ---
from routes.budget_routes import budget_bp
from routes.income_routes import income_bp
from routes.savings_routes import savings_bp
from routes.auth_routes import auth_bp, limiter  # 👈 new import for auth + rate limiter

# Load environment variables from .env file
load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # enable CORS for cross-origin requests (React frontend, etc.)
    CORS(app, supports_credentials=True)

    # initialize extensions
    db.init_app(app)
    Migrate(app, db)

    # attach limiter (shared from auth_routes)
    limiter.init_app(app)

    # register blueprints
    app.register_blueprint(budget_bp,  url_prefix="/api/budget")
    app.register_blueprint(income_bp,  url_prefix="/api/income")
    app.register_blueprint(savings_bp, url_prefix="/api/savings")
    app.register_blueprint(auth_bp,    url_prefix="/api/auth")   # 👈 register auth endpoints

    # simple test route for container health check
    @app.get("/api/health")
    def health():
        return {"status": "ok"}

    return app


if __name__ == "__main__":
    app = create_app()
    # bind to all interfaces inside Docker, debug for local dev
    app.run(host="0.0.0.0", port=5000, debug=True)
