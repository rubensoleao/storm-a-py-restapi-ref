# Projeto MGL

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

## Database

Database is set up using the mysql docker image in port `32000`. It can be set up seperatly using the following comamnds:

Start DB: 
- `make db-up`
Stop DB:
- `make db-down`