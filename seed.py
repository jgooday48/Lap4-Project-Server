from application import create_app, db
from application.places.model import Place
from application.activities.model import Activity
from application.enums import Specialisation
app = create_app()
app.app_context().push()  # push the app context

db.drop_all()
print("Dropping Database")

db.create_all()
print("Creating Database")

print("Seeding Database")

name = "NYC"
tags = "#photo"
description="awesome"
location = "USA"

place = Place(name=name, tags=tags, description=description, location=location)

db.session.add(place)

activity = Activity(name="canoe", location="nyc", place_id=1, description="jkl", post_code="722",specialisation=Specialisation.OUTDOOR_ACTIVITIES)

db.session.add(activity)

db.session.commit()
