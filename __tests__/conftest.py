import pytest
from application import create_app,db
from application.places.model import Place
from application.activities.model import Activity
from application.tourists.model import Tourist
from application.guides.model import Guide
from application.reviews.model import Review
from application.plans.model import Plan

@pytest.fixture
def client():
    env = "TEST"
    # Initialise a test app
    app = create_app(env)
    
    # Create a test client to which we can make requests
    client = app.test_client()
    
    with app.app_context():
        db.session.rollback()
        db.drop_all()
        
    # Create a test database with some test data
    with app.app_context():
        # Create the test database
        db.create_all()
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

    return client
