from app import db, ma


class Category(db.Model):
    """Class describing DB model Category"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=False)
    products = db.relationship('Product', backref='category')


class Product(db.Model):
    """Class describing DB model Product"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False, unique=True)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=False)
    sales_start = db.Column(db.Date, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    img_path = db.Column(db.String(50),
                         nullable=True,
                         default='./static/images/products/default.jpg')
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))


class ProductSchema(ma.Schema):
    """Class describing Marshmallow Schema for Product DB model"""
    class Meta:
        fields = ('id', 'title', 'price', 'description',
                  'sales_start', 'amount', 'img_path', 'category_id')


class CategorySchema(ma.Schema):
    """Class describing Marshmallow Schema for Category DB model"""
    class Meta:
        fields = ('id', 'title', 'description', 'products')

    products = ma.Nested(ProductSchema, many=True)
