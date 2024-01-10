from application import create_app, db

from application.tourists.model import Tourist
from application.guides.model import Guide
from application.places.model import Place
from application.activities.model import Activity


app = create_app()
app.app_context().push()  # push the app context

db.drop_all()
print("Dropping Database")

db.create_all()
print("Creating Database")

print("Seeding Database")
tourist1 = Tourist(name='Jane Doe', user_type='TOURIST',username='janedoe123', email='jane.doe@gmail.com')
tourist1.set_password('password')

db.session.add(tourist1)
db.session.commit()

name = "NYC"
tags = "#photo"
description="awesome"
location = "USA"

place = Place(name=name, tags=tags, description=description, location=location)

db.session.add(place)


guide1 = Guide(name='Guy Dunn', user_type='GUIDE', username='guydunn42', email='guy.dunn@gmail.com')
guide1.set_password('password')
guide1.filters = ['HISTORICAL', 'OUTDOOR_ACTIVITIES']
db.session.add(guide1)

activity = Activity(name="canoe", location="nyc", place_id=1, description="jkl", post_code="722",specialisation="OUTDOOR_ACTIVITIES")


db.session.add(activity)

db.session.commit()
