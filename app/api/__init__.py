from flask import Blueprint

bp = Blueprint('rest', __name__)

from app.api import rest