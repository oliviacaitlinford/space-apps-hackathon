from models import db, connect_db, Resource
from app import app

db.drop_all()
db.create_all()

resource = Resource(
                name ="NASA Earth Observatory", 
                url = "https://earthobservatory.nasa.gov/",
                description = "Images of atmosphere, heat, human, land, life, natural events, remote sensing, snow and ice, water",
                login_required = False,
                api_available = True,
                country_of_origin = "United States",
                documentation_url = "https://earthobservatory.nasa.gov/map#2/0.0/0.0",
                keywords = "sky, images, land")
   
db.session.add(resource)
db.session.commit()
