from application import create_app, db

from application.tourists.model import Tourist
from application.guides.model import Guide
from application.places.model import Place
from application.activities.model import Activity
from application.plans.model import Plan
from application.reviews.model import Review
from datetime import datetime

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


guide1 = Guide(name='Guy Dunn', user_type='GUIDE', username='guydunn42', email='guy.dunn@gmail.com', place_id=1)
guide1.set_password('password')
guide1.filters = ['HISTORICAL', 'OUTDOOR_ACTIVITIES']
db.session.add(guide1)

activity = Activity(name="canoe", location="nyc", place_id=1, description="jkl", guide_id=1,post_code="722",specialisation="OUTDOOR_ACTIVITIES")



db.session.add(activity)

plan = Plan(tourist_id=1,guide_id=1,activity_id=1,status="PLANNED", timestamp=14)
db.session.add(plan)

review = Review(guide_id=1, tourist_id=1, rating=10, comment="nice")
db.session.add(review)
db.session.commit()
