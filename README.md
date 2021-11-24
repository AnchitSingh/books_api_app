# BOOKS API

## Installation

The package manager [pip](https://pip.pypa.io/en/stable/) and MySQL is required to run this project.

```bash
pip3 install django
sudo apt-get install python3-dev libmysqlclient-dev
pip3 install mysqlclient
```

## Usage
Deafult user credentials for MySQL database are following
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'practice',
        'USER': 'root',
        'PASSWORD': 'very_strong_password',
        'HOST': 'localhost',
        'OPTIONS': {
            'charset': 'utf8mb4' 
        }
    }
}
```
In case you want to use your own credentials, you can update these though `settings.py` file present in `portal` directory. Then run the following commands to create the database tables.

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```
Now we just need to start the web server to complete the setup, which can be done by following command.
```python
python3 manage.py runserver
```
Web server will be running on port 8000 of localhost.

## Features
The web app supports following routes

1. `/api/external-books?name` : It takes book name as query-string and returns the json fetched from **Ice and Fire API**
2. `/api/v1/books` : It accepts only GET and POST request
   - `GET` : Returns JSON of all the books present in the local database
       - This also supports the searching operations, i.e. user can add query-string with the url to search the book via its name, year, pubisher, country and even via **author**
   - `POST` : Using the data from POST request it creates a new book and returns the JSON of newly created book
3. `/api/v1/books/<id>` : It accepts only *GET*, PATCH and DELETE requests
   - If the request is of `PATCH` method then it searches for book with given id in the database and the update it with data mentioned in PATCH request. Finally it returns the updated book details in JSON fromat.
    - If the requested method is of `DELETE` type, then app searches for the book with given id in the database and deletes it. Finally it returns the JSON data related to the operation
    - If the requested method is of `GET` type, then app searches for the book with given id in the database and returns the JSON data related to the book.

## Test Cases
To run the test case use the following comman
```python
python3 manage.py test api
```

## Cloud Version

This webapp is also deployed on cloud and can be accessed via [this link](http://178.18.244.251/)
User can visit the routes with *GET* method enabled to see the various JSON outputs.
