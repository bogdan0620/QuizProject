from flask import Flaskfrom flask_sqlalchemy import SQLAlchemyfrom database.models import dbapp = Flask(__name__)app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'db.init_app(app)from api import registration, test_process, leadersapp.register_blueprint(registration.registration_bp)app.register_blueprint(test_process.test_bp)app.register_blueprint(leaders.leaders_bp)