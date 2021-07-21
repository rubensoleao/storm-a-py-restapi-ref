# Projeto MGLU

**Rubens Ozório Leão**

Message scheduling system.

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

# Endpoints

The system includes 3 endpoints:

- **GET** `/msg-scheduler?id=idnumber`
    - params `id`: id of the requested scheduled call
    - JSON response:
    ```
        scheduled_date': '2021-07-21 16:45:19.665429',
        'type': 'email',
        'destination':'test@email.com',
        'message': 'Hello, this is a test message',
        'status': 'pending',
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