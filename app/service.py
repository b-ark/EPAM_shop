"""Modules with functions / classes to work with DB (CRUD operations)"""
import os
from datetime import datetime
from flask import redirect, abort
from sqlalchemy import exc
from app.models import db, Category, Product


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
    db.session.commit()


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


def post_category_service(request):
    """Gets data from POST request and ads it to database (only for Category items)"""
    title = request.values.get('title')
    description = request.values.get('description')
    item = Category(title=title, description=description)
    db_add(item)
    return item


def post_product_service(request):
    title = request.values.get('title')
    price = request.values.get('price')
    description = request.values.get('description')
    sales_start = datetime.strptime(request.values.get('sales_start'), '%Y-%m-%d').date()
    amount = request.values.get('amount')
    if request.values.get('category_id') is not None:
        category_id = request.values.get('category_id')
    else:
        cat = Category.query.filter_by(title=request.values.get('category_title')).first()
        category_id = cat.id
    element = Product(title=title,
                      price=price,
                      description=description,
                      sales_start=sales_start,
                      amount=amount,
                      category_id=category_id)
    db_add(element)
    return element


def put_category_service(_id, request):
    item = get_item(Category, _id)
    if check_request(request.values.get('title')):
        item.title = request.values.get('title')
    if check_request(request.values.get('description')):
        item.description = request.values.get('description')
    db_commit()
    return item


def put_product_service(_id, request):
    item = get_item(Product, _id)

    if check_request(request.values.get('title')):
        item.title = request.values.get('title')
    if check_request(request.values.get('price')):
        item.price = request.values.get('price')
    if check_request(request.values.get('description')):
        item.description = request.values.get('description')
    if check_request(request.values.get('sales_start')):
        item.sales_start = datetime.strptime(request.values.get('sales_start'), '%Y-%m-%d').date()
    if check_request(request.values.get('amount')):
        item.amount = request.values.get('amount')
    if check_request(request.values.get('img_path')):
        item.img_path = request.values.get('img_path')
    if check_request(request.values.get('category_id')):
        item.category_id = request.values.get('category_id')
    db_commit()
    return item


def delete_category_service(_id):
    item = get_item(Category, _id)
    db_delete(item)
    return item


def delete_product_service(_id):
    item = get_item(Product, _id)
    if item.img_path != './static/images/products/default.jpg':
        os.remove('./app' + item.img_path)
    db_delete(item)
    return item
