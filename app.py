from application import create_app # app from __init__.py

from application import routes
from application.Place import routes
if __name__=='__main__':
    app = create_app("PROD")
    app.run(port=5000, debug=True,host="0.0.0.0") 
