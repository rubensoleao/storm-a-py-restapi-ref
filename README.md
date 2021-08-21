# STORM

Storm is a reference projet for a simple *python3*  REST api using *flask* as the web framework, *mySQL* for DB, *sqlAlchemy* for DB management, *marshmallow* for schemas, *pytest* for tests.

## About

The generated API is for an endpoint to a message schedulling system, where it can register,view and delete messages.

### Endpoints

- **GET** `/msg-scheduler?id=idnumber`
    - params 
        - `scheduled_date`,`type`,`destination`,`message`,`status`, `id`
        - Pagination: `page`, `limit` 
    - JSON response:
    ```
        {
            'data': [
                'id': 1
                'scheduled_date': '2021-07-21 16:45:19.665429',
                'type': 'email',
                'destination':'test@email.com',
                'message': 'Hello, this is a test message',
                'status': 'pending',

                ...]
            'page': 1
            'total': 1
        }
    ```
    - Successful status Code 200

- **POST** `/msg-scheduler`
    - request body: A Json with the schedulled message:
    ```
        scheduled_date': '2021-07-21 16:45:19.665429',
        'type': 'email',
        'destination':'test@email.com',
        'message': 'Hello, this is a test message',
    ```
    - Successful status Code 204
    
- **DELETE** `/msg-scheduler?id=idnumber`
    - params `id`: id of the requested scheduled call to delete
    - JSON response:
    ```'id':'123'```
    - Successful status Code 200

## Installation

git clone the repo **repo url**.

Install a python version `3.9` enviroment. We recommend using your preffered virtual environment. For [python virtualenv](https://docs.python.org/3/tutorial/venv.html), setup a new virtuaenv in `venv` folder in the projects root directory.

And install the recomendend requirements in `requirements/development.txt` using `pip` version `21.1.1`.

```
git clone repo_url
cd repo_dir
 
python3 -m venv venv      # With python 3.9
source venv/bin/activate  # Activate the virtualenv
pip install -r requirements/development.txt
```

### Database

Database is set up using the mysql docker image in port `32000`. It can be set up seperatly using the following comamnds:

Start DB: 
- `make db-up`
Stop DB:
- `make db-down`
Init the DB tables
- `make init-db`

### Flask server

After the dabase is runnign the flask server can be runned locally with the command 

`make flask-run`

