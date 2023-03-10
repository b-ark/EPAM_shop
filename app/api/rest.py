"""Modules with RESTful service implementation"""
from datetime import datetime
import os
from flask import request, jsonify
from app.models import Category, Product, CategorySchema, ProductSchema
from app.service import db_add, get_item, check_request, db_commit, db_delete
from app.api import bp


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)


@bp.route('/api/category', methods=['GET', 'POST', 'DELETE', 'PUT'])
def rest_category():
    """Operations with single category object"""
    if request.method == 'POST':
        title = request.values.get('title')
        description = request.values.get('description')
        item = Category(title=title, description=description)
        db_add(item)
    if request.method == 'GET':
        _id = request.values.get('id')
        item = get_item(Category, _id)
    if request.method == 'PUT':
        _id = request.values.get('id')
        item = get_item(Category, _id)
        if check_request(request.values.get('title')):
            item.title = request.values.get('title')
        if check_request(request.values.get('description')):
            item.description = request.values.get('description')
        db_commit()
    if request.method == 'DELETE':
        item = get_item(Category, request.values.get('id'))
        db_delete(item)
    return category_schema.jsonify(item)


@bp.route('/api/product', methods=['GET', 'POST', 'DELETE', 'PUT'])
def rest_product():
    """Operations with single product object"""
    if request.method == 'POST':
        title = request.values.get('title')
        price = request.values.get('price')
        description = request.values.get('description')
        sales_start = datetime.strptime(request.values.get('sales_start'), '%Y-%m-%d').date()
        amount = request.values.get('amount')
        category_id = request.values.get('category_id')
        element = Product(title=title,
                          price=price,
                          description=description,
                          sales_start=sales_start,
                          amount=amount,
                          category_id=category_id)
        db_add(element)
        return product_schema.jsonify(element)

    if request.method == 'GET':
        _id = request.values.get('id')
        item = get_item(Product, _id)
        return product_schema.jsonify(item)

    if request.method == 'PUT':
        _id = request.values.get('id')
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
        return product_schema.jsonify(item)

    if request.method == 'DELETE':
        item = get_item(Product, request.values.get('id'))
        if item.img_path != './static/images/products/default.jpg':
            os.remove('./app' + item.img_path)
        db_delete(item)
        return product_schema.jsonify(item)


@bp.route('/api/categories', methods=['GET'])
def rest_categories():
    """Operations with all category objects"""
    data = Category.query.all()
    return categories_schema.jsonify(data)


@bp.route('/api/products', methods=['GET'])
def rest_products():
    """Operations with all product objects"""
    data = Product.query.all()
    return products_schema.jsonify(data)


@bp.route('/api/category/sum', methods=['GET'])
def rest_products_sum():
    """Calculates the sum of all products in the certain category"""
    _id = request.values.get('id')
    item = get_item(Category, _id)
    result = 0
    for i in item.products:
        result += i.amount
    return jsonify({'sum': result})


@bp.route('/api/search', methods=['GET'])
def rest_search():
    """Returns products, available by certain date"""
    date = datetime.strptime(request.values.get('date'), '%Y-%m-%d').date()
    data = Product.query.filter(Product.sales_start <= date)
    return products_schema.jsonify(data)
