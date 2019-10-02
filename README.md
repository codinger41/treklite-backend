# Treklite-API

**Check out the frontend here (contains every detail):** https://github.com/codinger41/TrekLite

## Requirements and Installation
**Via Cloning The Repository**
```
# Clone the app
git clone https://github.com/codinger41/treklite-backend.git

# Setup Env
Follow the format specified in the .env example

# Switch to directory
cd treklite-backend

# Create virtual env
virtualenv --python=python3 venv

# Activate virtual env
source venv/bin/activate

# Install Package dependencies
 pip install -r requirements.txt

# create and setup .env file according to .env.example

# Run migrations
python3 manage.py db migrate
python3 manage.py db upgrade

#Start the application
python3 manage.py runserver

#View the application
navigate to localhost:3000 to view the application
```
## Testing
- Running Tests
 - To run tests and observe test coverage for various versions of python . Run the command below.
 ```
 tox
 ```
 - To run  and check for test coverage. Run the command below:
 ```
 pytest -v --cov
 ```
 - To obtain coverage report. Run the command below:

 ```
 coverage report
 ```
 - To obtain html browser report. Run command below:
 ```
 coverage html
 ```
 ```
 A folder titled html_coverage_report will be generated. Open it and copy the path  of index.html and paste it in your browser.
 ```
## Technologies 

### Backend

* [Python-Flask](http://flask.pocoo.org/) Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions
* [GraphQl](https://graphql.org/) GraphQL is a new API standard that provides a more efficient, powerful and flexible alternative to REST.
* [SQLAlchemy](https://www.sqlalchemy.org/) SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.
* [Flask Migrate](https://flask-migrate.readthedocs.io/en/latest/) Alembic is a lightweight database migration tool for usage with the SQLAlchemy Database Toolkit for Python.


