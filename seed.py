from application import create_app, db

from application.tourists.model import Tourist
from application.guides.model import Guide
from application.places.model import Place
from application.activities.model import Activity
from sqlalchemy import text




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
tags = ["#photo"]
description="awesome"
location = "USA"

place = Place(name=name, tags=tags, description=description, location=location)

db.session.add(place)


guide1 = Guide(place_id=1, name='Guy Dunn', user_type='GUIDE', username='guydunn42', email='guy.dunn@gmail.com')
guide1.set_password('password')
guide1.filters = ['HISTORICAL', 'OUTDOOR_ACTIVITIES']
db.session.add(guide1)

activity = Activity(name="canoe", location="nyc",
                    filters=["OUTDOOR_ACTIVITIES"], place_id=1, description="sick as", zip_code="NE3 4RY")

db.session.add(activity)

guide1.activities.append(activity)

# ... (existing code)


def create_tourist(name, user_type, username, email):
    tourist = Tourist(name=name, user_type=user_type,
                      username=username, email=email)
    tourist.set_password('password')
    db.session.add(tourist)


def create_place(name, tags, description, location):
    place = Place(name=name, tags=tags,
                  description=description, location=location)
    db.session.add(place)


def create_guide(place_id, name, user_type, username, email, filters):
    guide = Guide(place_id=place_id, name=name,
                  user_type=user_type, username=username, email=email)
    guide.set_password('password')
    guide.filters = filters
    db.session.add(guide)


def create_activity(name, location, filters, place_id, description, zip_code):
    activity = Activity(name=name, location=location, filters=filters,
                        place_id=place_id, description=description, zip_code=zip_code)
    db.session.add(activity)


# Add more tourists
tourist_data = [
    ('John Smith', 'TOURIST', 'johnsmith456', 'john.smith@gmail.com'),
    ('Emily Wilson', 'TOURIST', 'emilywilson789', 'emily.wilson@gmail.com'),
    ('Michael Brown', 'TOURIST', 'michaelbrown123', 'michael.brown@gmail.com'),
    ('Sophia Rodriguez', 'TOURIST', 'sophiarodriguez456', 'sophia.rodriguez@gmail.com'),
    ('Daniel Taylor', 'TOURIST', 'danieltaylor789', 'daniel.taylor@gmail.com')
]

for data in tourist_data:
    create_tourist(*data)

db.session.commit()

# Add more places
place_data = [
    ("Malta", ["#beach"], "best island", "Europe"),
    ("Los Angeles", ["#city"], "vibrant city", "USA"),
    ("Paris", ["#culture"], "City of Love", "France"),
    ("Tokyo", ["#technology"], "Futuristic city", "Japan"),
    ("Sydney", ["#beach"], "Beautiful beaches", "Australia"),
    ("Rome", ["#history"], "Eternal City", "Italy")
]

for data in place_data:
    create_place(*data)

db.session.commit()

# Add more guides
guide_data = [
    (2, 'Alice Johnson', 'GUIDE', 'alicejohnson88','alice.johnson@gmail.com', ['CULTURAL', 'SHOPPING']),
    (2, 'David Lee', 'GUIDE', 'davidlee42','david.lee@gmail.com', ['HISTORICAL', 'FOOD']),
    (2, 'Mia Williams', 'GUIDE', 'miawilliams123','mia.williams@gmail.com', ['NATURE', 'ENTERTAINMENT']),
    (2, 'Oliver Smith', 'GUIDE', 'oliversmith456','oliver.smith@gmail.com', ['ART', 'OUTDOOR_ACTIVITIES']),
    (2, 'Emma Davis', 'GUIDE', 'emmadavis789', 'emma.davis@gmail.com', ['CULTURAL', 'NIGHTLIFE'])
]

for data in guide_data:
    create_guide(*data)

db.session.commit()

# Add more activities
activity_data = [
    ("hiking", "Los Angeles", ["OUTDOOR_ACTIVITIES"], 2, "amazing views", "90210"),
    ("museum tour", "Paris", ["CULTURAL", "HISTORICAL"],3, "art and history exploration", "75001"),
    ("sushi cooking class", "Tokyo", ["FOOD", "CULTURAL"], 4, "learn the art of sushi making", "100-0005"),
    ("beach volleyball", "Sydney", ["OUTDOOR_ACTIVITIES", "SPORTS"], 5, "fun in the sun", "2000"),
    ("Colosseum tour", "Rome", ["HISTORICAL","CULTURAL"], 6, "ancient wonders", "00184")
]

for data in activity_data:
    create_activity(*data)

db.session.commit()



db.session.commit()
