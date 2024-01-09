import pytest
from application import create_app,db
from application.places.model import Place

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
  
        # Inject it into the database

        db.session.add(test_place)
        db.session.commit()

    return client
