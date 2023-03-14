# EPAM_shop
[![Build Status](https://app.travis-ci.com/b-ark/EPAM_shop.svg?branch=main)](https://app.travis-ci.com/b-ark/EPAM_shop)
[![Coverage Status](https://coveralls.io/repos/github/b-ark/EPAM_shop/badge.svg?branch=main)](https://coveralls.io/github/b-ark/EPAM_shop?branch=main)

This is a shop managment system, where you can organize your products by categories. It provides Web application and REST api, which allows user to:

- Add new categories and products
- Display lists of categories
- Sort products by categories
- Search for products that will be available for sale on a specific date

## Used technologies

- [Flask](https://flask.palletsprojects.com) as web framework
- [SQLAlchemy](https://www.sqlalchemy.org) as ORM
- [Travis-CI](https://www.travis-ci.com) as CI/CD
- [Coverage](https://coverage.readthedocs.io/en/7.2.1/) + [Coveralls.io](https://coveralls.io) as a code coverage tracker

## Getting started

Before building this project, make sure that the latest version of Python is installed on your Linux Ubuntu system.

## How to build

1. Clone repository: `git clone https://github.com/b-ark/EPAM_shop`
2. Navigate to the EPAM_shop directory: `cd EPAM_shop`
3. Create and activate new Virtual Environment: `python3 -m virtualenv venv` + `source venv/bin/activate`
4. Install requirements 'pip install -r requirements.txt'
4.1. If you want to deploy the web service on [Gunicorn](https://gunicorn.org/), install it to the project: `pip install gunicorn`
That's it, you are ready to go! Run application using Flask: `flask run` or using Gunicorn: 'gunicorn wsgi:app'
