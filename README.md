# Lap4-Project-Server

# Instructions for installation and usage
- `pipenv shell`
- `pipenv install`
- `touch .env`
- Copy and paste the following into the .env file:
```
FLASK_DEBUG=1
SQLALCHEMY_DATABASE_URI=
```
- Edit the docker-compose.yaml file to your own specifications
- `docker compose up -d`
- Make sure that your interpreter is selected as a pipenv one related to your file
- Run `python seed.py` to seed the db instance
- Run `pipenv run dev` to start the api
- The api runs on http://localhost:5000/
