from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Resource(db.Model):
    """Todo Model"""

    __tablename__ = "resources"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    url = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    login_required = db.Column(db.Boolean, default=False)
    api_available = db.Column(db.Boolean, default=False)
    country_of_origin = db.Column(db.Text)
    documentation_url = db.Column(db.Text)
    keywords = db.Column(db.Text, nullable=False)

    def serialize(self):
        """Returns a dict representation of todo which we can turn into JSON"""
        return {
            'id': self.id,
            'name': self.name,
            'url': self.url,
            'description': self.description,
            'login_required': self.login_required,
            'api_available': self.api_available,
            'country_of_origin': self.country_of_origin,
            'documentation_url': self.documentation_url,
            'keywords': self.keywords
        }