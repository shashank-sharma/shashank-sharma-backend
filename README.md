[![Build Status](https://travis-ci.org/shashank-sharma/shashank-sharma-backend.svg?branch=master)](https://travis-ci.org/shashank-sharma/shashank-sharma-backend)

# Introduction


Backend for personal use using DRF with Django 3.0.6 using PostgreSQL.<br>
Project deployed in Heroku


### Installation

1. Clone the repository by:<br />
`git clone https://github.com/shashank-sharma/shashank-sharma-backend`

2. Create Virtual Environment named as `env` by doing<br />
`python3 -m venv env`

   Now activate it by:<br />
`source env/bin/activate` (Linux)<br>
`myvenv\Scripts\activate` (Windows)

3. Install dependencies<br />
`pip install -r requirements.txt`


4. Database configuration

   Using psql:<br />
`CREATE ROLE admin WITH LOGIN PASSWORD 'password';`<br />
`create database shanksdb;`<br />
`GRANT ALL PRIVILEGES ON DATABASE shankdb TO admin;`

   databaseurl: postgresql://admin:password@localhost/shanksdb

5. Set up Virtual Environment values (As mentioned in .env.example)<br />
a. Secret Key: `SECRET_KEY=RANDOMTEXT`<br />
b. Database Url: `DATABASE_URL=<databaseurl>`

6. Migration: <br />
`python manage.py migrate`
