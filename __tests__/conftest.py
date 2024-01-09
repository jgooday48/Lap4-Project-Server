import pytest
from application import create_app,db

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
        # test_author = Author(name="Test")
        # test_book = Book(title="Test", author_id=1,genre="fantasy")
        # # Inject it into the database
        # db.session.add(test_author)
        # db.session.add(test_book)
        db.session.commit()

    return client
