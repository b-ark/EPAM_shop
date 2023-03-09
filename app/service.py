"""Modules with functions / classes to work with DB (CRUD operations)"""
from flask import redirect, abort
from sqlalchemy import exc
from app.models import db, Category


def db_add(element):
    """Adds element to database"""
    try:
        db.session.add(element)
        db.session.commit()
        return None
    except exc.SQLAlchemyError:
        return 'Error'


def db_commit():
    """Database commit"""
    try:
        db.session.commit()
        return None
    except exc.SQLAlchemyError:
        return 'Error'


def db_delete(item):
    """Deletes item from database by id and type of object"""
    try:
        db.session.delete(item)
        db_commit()
        return None
    except exc.SQLAlchemyError:
        return 'Error'


def check_request(element):
    """Checks if the element in request exists"""
    if element is None:
        return False
    return True


def get_item(obj, _id):
    """Gets an item from database by id and type of object"""
    item = obj.query.filter_by(id=_id).first()
    if item is None:
        return abort(404, f'No such item {obj} in database with id = {_id}')
    return item


def POST_category(request):
    """Gets data from POST request and ads it to database (only for Category items)"""
    title = request.form['title']
    description = request.form['description']
    category = Category(title=title, description=description)
    db_add(category)
    return redirect('/categories')
