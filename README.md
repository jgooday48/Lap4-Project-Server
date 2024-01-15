# Lap4-Project-Server

# Instructions for installation and usage
- Run `pipenv shell` to create a pipenv shell
- Run `pipenv install` to install the required modules
- Run `touch .env`
- Copy and paste the following into the .env file:
```
FLASK_DEBUG=1
SQLALCHEMY_DATABASE_URI=DB_URI=postgresql://username:password@localhost:5432/database
```
- Open docker
- Edit the docker-compose.yaml file to your own specifications
- Hence, edit the DB URI in the .env file to replace username, password and database with your own
- Run `docker compose up -d` to start the docker container
- Make sure that your interpreter is selected as a pipenv one related to your file
- Run `pipenv run seed-db` to seed the db instance
- Run `pipenv run dev` to start the api
- The api runs on http://localhost:5000
- To close the docker container run `docker compose down`

# Instructions to test
- Create an elephant SQL instance
- copy and paste the following into the .env file:
```
TEST_DB=
```
- copy and paste the URL into .env
- Run `pipenv run test` or `pipenv run coverage`

## Technologies
- Python
- Flask
- PyTest
- SQL (for database)
