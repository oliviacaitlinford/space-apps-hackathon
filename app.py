"""START OF SPACE APPS API"""

from flask import Flask, request, jsonify, render_template
from models import db, connect_db, Resource

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///space_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oh-so-secret"

connect_db(app)

@app.route('/')
def index_page():
    """Renders html template - NOT PART OF JSON API!"""
    return render_template('index.html')

# *****************************
# RESTFUL SPACE RESOURCES JSON API
# *****************************
@app.route('/api/resources')
def list_resources():
    """Returns JSON w/ all resources"""
    all_resources = [resource.serialize() for resource in Resource.query.all()]
    return jsonify(resources=all_resources)

@app.route('/api/resources', methods=["POST"])
def create_resource():
    """Creates a new todo and returns JSON of that created todo"""
    new_resource = Resource(name = request.json["name"], 
                url = request.json["name"],
                description = request.json["name"],
                login_required = request.json["name"],
                api_available = request.json["name"],
                country_of_origin = request.json["name"],
                documentation_url = request.json["name"],
                keywords = request.json["name"])
    db.session.add(new_resource)
    db.session.commit()
    response_json = jsonify(resource=new_resource.serialize())
    return (response_json, 201)