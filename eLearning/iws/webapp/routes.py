from flask import Blueprint, render_template
from flask import request

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return "Welcome to eLearning!"

