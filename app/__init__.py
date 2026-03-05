from flask import Flask, send_from_directory
from flask_cors import CORS
import os
from .db import mongo
from .config import MONGO_URI
from .routes.chat_routes import chat_bp
from .routes.auth_routes import auth_bp
from .routes.blog_routes import blog_bp
from .routes.job_routes import job_bp
from .routes.partner_routes import partner_bp
from .routes.contact_routes import contact_bp
from .routes.testimonial_routes import testimonial_bp
from .routes.hero_routes import hero_bp
from .routes.step_routes import steps_bp
from .routes.profile_routes import profile_bp
from .routes.lead_routes import leads_bp
from .routes.formlead_routes import formleads_bp
from .routes.dashboard_routes import dashboard_bp

# mongo = PyMongo() # Moved to db.py

def create_app():
    app = Flask(__name__)

    app.config["MONGO_URI"] = MONGO_URI
    mongo.init_app(app)

    CORS(
        app,
        resources={r"/*": {"origins": "*"}},
        allow_headers=["*"],
        methods=["*"],
    )

    @app.route('/uploads/<path:filename>')
    def serve_upload(filename):
        return send_from_directory(os.path.join(app.root_path, '../uploads'), filename)

    app.register_blueprint(chat_bp, url_prefix="/py/api")
    app.register_blueprint(auth_bp, url_prefix="/py/api/auth")
    app.register_blueprint(blog_bp, url_prefix="/py/api/blogs")
    app.register_blueprint(job_bp, url_prefix="/py/api/jobs")
    app.register_blueprint(contact_bp, url_prefix="/py/api/contact")
    app.register_blueprint(testimonial_bp, url_prefix="/py/api/testimonial")
    app.register_blueprint(hero_bp, url_prefix="/py/api/hero")
    app.register_blueprint(partner_bp, url_prefix="/py/api/partner")
    app.register_blueprint(steps_bp, url_prefix="/py/api/steps")
    app.register_blueprint(profile_bp, url_prefix="/py/api/profile")
    app.register_blueprint(leads_bp, url_prefix="/py/api/leads")
    app.register_blueprint(formleads_bp, url_prefix="/py/api/formleads")
    app.register_blueprint(dashboard_bp, url_prefix="/py/api")

    return app
