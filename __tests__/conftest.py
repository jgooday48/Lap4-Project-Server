import pytest
from application import create_app,db
from application.places.model import Place
from application.activities.model import Activity

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
        # Create fake data
        test_place = Place(name="Test", location="test", description="test", tags="test")
        test_place2 = Place(name="Test2", location="test", description="test", tags="test")
        test_activity = Activity(name="canoe", location="nyc", place_id=1, description="jkl", post_code="722")
        # Inject it into the database

        db.session.add(test_place)
        db.session.add(test_place2)
        db.session.add(test_activity)
        db.session.commit()

    return client
