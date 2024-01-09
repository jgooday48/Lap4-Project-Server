from application import create_app, db
from application.places.model import Place
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




db.session.commit()
