import pytest
from application import create_app,db
from application.places.model import Place
from application.activities.model import Activity
from application.tourists.model import Tourist
from application.guides.model import Guide
from application.reviews.model import Review
from application.plans.model import Plan
from application.message.model import Message
from application.chat.model import Chat
from application.notes.model import Note
from application.notification.model import Notification
from datetime import datetime

@pytest.fixture(scope='session')
def client():
    env = "TEST"
    # Initialise a test app
    app = create_app(env)
    
    # Create a test client to which we can make requests
    client = app.test_client()

    with app.app_context():
        db.session.rollback()
        db.drop_all()
        db.create_all()
        create_test_data()
    yield client

    
    with app.app_context():
        db.session.rollback()
        db.drop_all()
        
    # Create a test database with some test data
def create_test_data():
    # Create the test database
    db.create_all()

    tourist1 = Tourist(name='Jane Doe', user_type='TOURIST',username='janedoe123', email='jane.doe@gmail.com')
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


    guide1 = Guide(place_id=1, name='Guy Dunn', user_type='GUIDE', username='guydunn42', email='guy.dunn@gmail.com', availible_from=datetime.now(), availible_to=datetime.now())
    guide1.set_password('password')
    guide1.filters = ['HISTORICAL', 'OUTDOOR_ACTIVITIES']
    db.session.add(guide1)

    activity = Activity(name="canoe", location="nyc",
                        filters=["OUTDOOR_ACTIVITIES"], place_id=1, description="sick as", zip_code="NE3 4RY", images=['fsdf'])

    db.session.add(activity)

    guide1.activities.append(activity)

    # ... (existing code)


    def create_tourist(name, user_type, username, email, images):
        tourist = Tourist(name=name, user_type=user_type,
                        username=username, email=email, images=images)
        tourist.set_password('password')
        db.session.add(tourist)


    def create_place(name, tags, description, location, images=None):
        place = Place(name=name, tags=tags,
                    description=description, location=location, images=images or [])
        db.session.add(place)


    def create_guide(place_id, name, user_type, username, email, filters, availible_from, availible_to,info,images=None):
        guide = Guide(place_id=place_id, name=name,
                    user_type=user_type, username=username, email=email,  availible_from=availible_from, availible_to=availible_to,info=info,images=images or [])
        guide.set_password('password')
        guide.filters = filters
        db.session.add(guide)


    def create_activity(name, location, filters, place_id, description, zip_code, images):
        activity = Activity(name=name, location=location, filters=filters,
                            place_id=place_id, description=description, zip_code=zip_code, images=images)
        db.session.add(activity)


    # Add more tourists
    tourist_data = [
        ('John Smith', 'TOURIST', 'johnsmith456', 'john.smith@gmail.com',[]),
        ('Emily Wilson', 'TOURIST', 'emilywilson789', 'emily.wilson@gmail.com',[]),
        ('Michael Brown', 'TOURIST', 'michaelbrown123', 'michael.brown@gmail.com',[]),
        ('Sophia Rodriguez', 'TOURIST', 'sophiarodriguez456', 'sophia.rodriguez@gmail.com',[]),
        ('Daniel Taylor', 'TOURIST', 'danieltaylor789', 'daniel.taylor@gmail.com', [])
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
        (2, 'Hiroshi Tanaka', 'GUIDE', 'hiroshi88','hiroshi.tanakaj@gmail.com', ['CULTURAL', 'SHOPPING'],datetime.now(),datetime.now(), 'sfdhjkfds' ),
        (2, 'Yuki Nakamura', 'GUIDE', 'yuki42','yuki.nakamura@gmail.com', ['HISTORICAL', 'FOOD'],datetime.now(),datetime.now(), 'sfdhjkfds'  ),
        (2, 'Haruki Ito', 'GUIDE', 'haruki123', 'haruki.ito@gmail.com', ['NATURE', 'ENTERTAINMENT'],datetime.now(),datetime.now(), 'sfdhjkfds'  ),
        (2, 'Kaori Fujimoto', 'GUIDE', 'fujimoto456', 'koari.fujimoto@gmail.com', ['ART', 'OUTDOOR_ACTIVITIES'],datetime.now(),datetime.now(), 'sfdhjkfds'  ),
        (2, 'Ryota Kobayashi', 'GUIDE', 'kobayashi789','ryota.kobayashi@gmail.com', ['CULTURAL', 'NIGHTLIFE'],datetime.now(),datetime.now(), 'sfdhjkfds'  )
    ]

    for data in guide_data:
        create_guide(*data)

    db.session.commit()

    # Add more activities
    activity_data = [
        ("hiking", "Los Angeles", ["OUTDOOR_ACTIVITIES"], 2, "amazing views", "90210",[]),
        ("museum tour", "Paris", ["CULTURAL", "HISTORICAL"],3, "art and history exploration", "75001",[]),
        ("sushi cooking class", "Tokyo", ["FOOD", "CULTURAL"], 4, "learn the art of sushi making", "100-0005", []),
        ("beach volleyball", "Sydney", ["OUTDOOR_ACTIVITIES", "SPORTS"], 5, "fun in the sun", "2000", []),
        ("Colosseum tour", "Rome", ["HISTORICAL","CULTURAL"], 6, "ancient wonders", "00184", [])
    ]

    for data in activity_data:
        create_activity(*data)

    db.session.commit()

    review = Review(guide_id=1, tourist_id=1, rating=10, title='review',comment="nice", timestamp=datetime.now())
    db.session.add(review)

    db.session.commit()
    plan = Plan(tourist_id=1,guide_id=1, place_id=1, status="BOOKED", date_from=datetime.now(), date_to=datetime.now(), notes='hsjk')
    db.session.add(plan)

    message = Message(chat_id=1, sender_id=1, text='a message')
    db.session.add(message)

    chat = Chat(chat_id=1, sender=1, receiver=1)
    db.session.add(chat)

    notes = Note(sender_id=1, text='dffs', guide_id=1, timestamp=datetime.now())
    db.session.add(notes)

    notifications = Notification(sender=1, receiver=1)
    db.session.add(notifications)
    db.session.commit()

