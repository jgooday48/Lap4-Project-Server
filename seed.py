from application import create_app, db

from application.tourists.model import Tourist
from application.guides.model import Guide
from application.places.model import Place
from application.activities.model import Activity
from application.plans.model import Plan
from sqlalchemy import text
from datetime import datetime



app = create_app()
app.app_context().push()  # push the app context

db.drop_all()
print("Dropping Database")

db.create_all()
print("Creating Database")

print("Seeding Database")
tourist1 = Tourist(name='Jane Doe', user_type='TOURIST',username='janedoe123', email='jane.doe@gmail.com', guide_username=['guydunn42', 'hiroshi88'])
tourist1.set_password('password')

db.session.add(tourist1)
db.session.commit()

name = "NYC"
tags = ["#photo"]
description="The city that never sleeps"
location = "USA"
images = ["https://upload.wikimedia.org/wikipedia/commons/4/47/New_york_times_square-terabass.jpg"]

place = Place(name=name, tags=tags, description=description, location=location, images=images)
db.session.add(place)


guide1 = Guide(place_id=1, name='Guy Dunn', user_type='GUIDE', username='guydunn42', email='guy.dunn@gmail.com', availible_from=datetime.now(),availible_to=datetime.now())
guide1.set_password('password')
guide1.filters = ['HISTORICAL', 'OUTDOOR_ACTIVITIES']
db.session.add(guide1)

activity = Activity(name="canoe", location="nyc",
                    filters=["OUTDOOR_ACTIVITIES"], place_id=1, description="sick as", zip_code="NE3 4RY", images=["https://cdn.britannica.com/69/155969-050-CF4B71FA/kayaker-ocean-waves.jpg"])

db.session.add(activity)

guide1.activities.append(activity)

# ... (existing code)


def create_tourist(name, user_type, username, email):
    tourist = Tourist(name=name, user_type=user_type,
                      username=username, email=email)
    tourist.set_password('password')
    db.session.add(tourist)


def create_place(name, tags, description, location, images=None):
    place = Place(name=name, tags=tags,
                  description=description, location=location, images=images or [])
    db.session.add(place)


def create_guide(place_id, name, user_type, username, email, filters, availible_from, availible_to, images=None):
    guide = Guide(place_id=place_id, name=name, user_type=user_type, username=username, email=email, availible_from=availible_from, availible_to=availible_to, images=images or [])
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
    ("Tokyo", ["#technology"], "Futuristic city", "Japan",  [
     "https://media.cntraveller.com/photos/64f6f03779eae8fd6b04756b/16:9/w_1920,c_limit/japan-GettyImages-1345059895.jpeg"]),
    ("Malta", ["#beach"], "best island", "Europe"),
    ("Los Angeles", ["#city"], "vibrant city", "USA"),
    ("Paris", ["#culture"], "City of Love", "France"),
    ("Sydney", ["#beach"], "Beautiful beaches", "Australia"),
    ("Rome", ["#history"], "Eternal City", "Italy")
]

for data in place_data:
    create_place(*data)

db.session.commit()

# Add more guides
guide_data = [
    (2, 'Hiroshi Tanaka', 'GUIDE', 'hiroshi88','hiroshi.tanakaj@gmail.com', ['CULTURAL', 'SHOPPING'],datetime.now(), datetime.now(), [
        "https://i1.rgstatic.net/ii/profile.image/11431281103851697-1669864605754_Q512/Hiroshi-Tanaka-9.jpg"
    ] ),
    (2, 'Yuki Nakamura', 'GUIDE', 'yuki42','yuki.nakamura@gmail.com', ['HISTORICAL', 'FOOD'],datetime.now(),datetime.now(), ["https://m.media-amazon.com/images/M/MV5BMGY4ODZjYjEtOTc3MC00ZTFiLThiYjktMDk1ZTQ1NjY1YjM2XkEyXkFqcGdeQXVyMTEwODg2MDY@._V1_.jpg"]),
    (2, 'Haruki Ito', 'GUIDE', 'haruki123', 'haruki.ito@gmail.com', ['NATURE', 'ENTERTAINMENT'],datetime.now(),datetime.now(),[
    "https://i1.sndcdn.com/avatars-000336898423-5m8j59-t500x500.jpg"
    ]),
    (2, 'Kaori Fujimoto', 'GUIDE', 'fujimoto456', 'koari.fujimoto@gmail.com', ['ART', 'OUTDOOR_ACTIVITIES'],datetime.now(),datetime.now(),      [
         "https://sliverofstonemagazinedotcom.files.wordpress.com/2015/03/kaori-fujimoto.jpg?w=1016"
     ]),
    (2, 'Ryota Kobayashi', 'GUIDE', 'kobayashi789','ryota.kobayashi@gmail.com', ['CULTURAL', 'NIGHTLIFE'],datetime.now(),datetime.now(),      [
         "https://static.wikia.nocookie.net/kamenrider/images/c/c4/Kobayashi_Ryota.jpg/revision/latest?cb=20180508155304"
     ])
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
