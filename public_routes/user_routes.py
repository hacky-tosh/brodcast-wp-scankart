from flask import Blueprint
# from routes.auth_routes import auth_blueprint
from flask.templating import render_template
from middleware.middleware import token_required

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@user_blueprint.route('/signup', methods=['GET'])
def signup():
    return render_template('signup.html')


@user_blueprint.route('/list-customers', methods=['GET'])
# @token_required
def home():
    return render_template('list-customers.html')


@user_blueprint.route('/create-campaign', methods=['GET'])
# @token_required
def create_campaign():
    return render_template('create-campaign.html')
