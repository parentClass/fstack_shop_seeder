# Fstack Shop Seeder

A python script for seeding/populating the specific database and collection with csv

### Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See running for notes on how to deploy the project on a live system.

### Pre-requisites

What things you need to install the software and how to install them

```
 - Python 3.8
 - Pip 19
 - MongoDB Compass
 - PostgreSQL 12
```

### Installation

Follow if python is not yet installed.

* [Where to download python 3.8?](https://www.python.org/)
* [How to install pip 19?](https://github.com/BurntSushi/nfldb/wiki/Python-&-pip-Windows-installation)

### Setting up

A step by step series of examples that tell you how to get this project running

1. After making sure python is working, let's start cloning the project
 ```git clone https://github.com/parentClass/fstack_shop_seeder.git```
2. Start mongo db service with strict equal connection string line
 ```mongodb://localhost:27017```
3. Start postgre sql service with strict equal connection string line
 ```
    const (
        host     = "127.0.0.1"
        port     = 5432
        user     = "postgres" // Change this within the code if user is not available
        password = "password" // Change this also within the code if password is different
        dbname   = "fstack_shop"
    )
 ```
4. Install packages/dependencies
 ```pip install -r requirements.txt```

### Running

Ensure that databases are running properly and accordingly

1. Go the project directory
2. ```py main.py```

### Packages

* [PyMongo](https://github.com/mongodb/mongo-python-driver.git) - PyMongo - the Python driver for MongoDB 
* [Psycopg2](https://github.com/psycopg/psycopg2/) - PostgreSQL database adapter for the Python programming language
* [Pandas](https://github.com/pandas-dev/pandas) - Flexible and powerful data analysis / manipulation library for Python, providing labeled data structures similar to R data.frame objects, statistical functions, and much more
* [NumPy](https://github.com/numpy/numpy) - NumPy is the fundamental package needed for scientific computing with Python.

### Examinee

* Daniel Sarabusing

### See also

* [Fstack-shop (back_end)](https://github.com/parentClass/fstack_shop_backend)
* [Fstack-shop (front_end)](https://github.com/parentClass/fstack_shop_frontend)