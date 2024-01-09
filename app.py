from application import create_app # app from __init__.py

from application import routes
from application.places import routes
from application.activities import routes
# from application.plans import routes
# from application.reviews import routes

app = create_app()
if __name__=='__main__':
    # app = create_app("PROD")
    app.run() 
