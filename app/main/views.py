"""Modules with Web controllers / main"""
from datetime import datetime
import os
from flask import render_template, request, redirect
from app.models import Category, Product
from app.service import get_item, db_commit, db_delete, db_add, check_request, \
    post_product_service, post_category_service, put_category_service, put_product_service, \
    delete_product_service, delete_category_service
from app.main import bp
from app.config import Config


@bp.route('/')
def index():
    """Main page"""
    return render_template('index.html')


@bp.route('/categories')
def categories():
    """Page with the list of categories and products"""
    data = Category.query.all()
    return render_template('categories.html', data=data)


@bp.route('/products')
def products():
    """Page with the list of products"""
    data = Product.query.all()
    return render_template('products.html', data=data)


@bp.route('/categories/new', methods=['POST', 'GET'])
def new_category():
    """Page with the form to add new category"""
    if request.method == 'POST':
        post_category_service(request)
        return redirect('/categories')
    # request.method == 'GET'
    return render_template('create_category.html')


@bp.route('/products/new', methods=['POST', 'GET'])
def new_product():
    """Page with the form to add new product"""
    if request.method == 'POST':
        post_product_service(request)
        obj = Product.query.order_by(Product.id.desc()).first()
        if "file" not in request.files:
            return 'No file part'
        file = request.files['file']
        file.filename = str(obj.id) + '.' + file.filename.split('.')[1]
        path_to_file = os.path.join(Config.UPLOAD_FOLDER, file.filename)
        file.save('./app' + path_to_file)
        obj.img_path = path_to_file
        db_commit()
        return redirect('/products')
    # request.method == 'GET'
    data = Category.query.all()
    return render_template('create_product.html', data=data)


@bp.route('/product/<int:_id>', methods=['GET'])
def show_product(_id):
    """Page to show product by id"""
    item = get_item(Product, _id)
    print(item.img_path)
    return render_template('product.html', data=item)


@bp.route('/category/<int:_id>', methods=['GET'])
def show_category(_id):
    """Page to show category by id"""
    item = get_item(Category, _id)
    return render_template('category.html', data=item)


@bp.route('/search', methods=['GET', 'POST'])
def search():
    """Page to search for products, available by certain date"""
    if request.method == 'POST':
        date = datetime.strptime(request.form['date'], '%Y-%m-%d').date()
        data = Product.query.filter(Product.sales_start <= date)
        return render_template('search.html', data=data)
    # request.method == 'GET'
    return render_template('search.html')


@bp.route('/category/edit/<int:_id>', methods=['GET', 'POST'])
def edit_category(_id):
    """Page to edit category by id"""
    if request.method == 'POST':
        put_category_service(_id, request)
        return redirect('/categories')
    # request.method == 'GET'
    item = get_item(Category, _id)
    return render_template('edit_category.html', data=item)


@bp.route('/product/edit/<int:_id>', methods=['GET', 'POST'])
def edit_product(_id):
    """Page to edit product by id"""
    if request.method == 'POST':
        put_product_service(_id, request)
        return redirect('/products')
    # request.method == 'GET' functionality
    item = get_item(Product, _id)
    cats = Category.query.all()
    return render_template('edit_product.html', data=[item] + [cats])


@bp.route('/product/delete/<int:_id>', methods=['GET'])
def delete_product(_id):
    """Page to delete product by id"""
    delete_product_service(_id)
    return redirect('/products')


@bp.route('/category/delete/<int:_id>', methods=['GET'])
def delete_category(_id):
    """Page to delete category by id"""
    delete_category_service(_id)
    return redirect('/categories')
