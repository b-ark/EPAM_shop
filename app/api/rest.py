"""Modules with RESTful service implementation"""
from datetime import datetime
from flask import request, jsonify
from app.models import Category, Product, CategorySchema, ProductSchema
from app.service import get_item, post_category_service, post_product_service, \
     put_product_service, put_category_service, delete_category_service, \
     delete_product_service
from app.api import bp


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)


@bp.route('/api/category', methods=['GET', 'POST', 'DELETE', 'PUT'])
def rest_category():
    """Operations with single category object"""
    if request.method == 'POST':
        item = post_category_service(request)
    if request.method == 'GET':
        _id = request.values.get('id')
        item = get_item(Category, _id)
    if request.method == 'PUT':
        item = put_category_service(request.values.get('id'), request)
    if request.method == 'DELETE':
        item = delete_category_service(request.values.get('id'))
    return category_schema.jsonify(item)


@bp.route('/api/product', methods=['GET', 'POST', 'DELETE', 'PUT'])
def rest_product():
    """Operations with single product object"""
    if request.method == 'POST':
        element = post_product_service(request)
        return product_schema.jsonify(element)

    if request.method == 'GET':
        _id = request.values.get('id')
        item = get_item(Product, _id)
        return product_schema.jsonify(item)

    if request.method == 'PUT':
        item = put_product_service(request.values.get('id'), request)
        return product_schema.jsonify(item)

    if request.method == 'DELETE':
        item = delete_product_service(request.values.get('id'))
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
