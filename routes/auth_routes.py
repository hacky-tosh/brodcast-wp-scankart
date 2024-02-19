from flask import Blueprint
from controller.auth import signup, login
from controller.contacts import add_single_contact,get_all_contacts, upload_contacts
from controller import auth
from controller.campaign import send_bulk_sms

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/signup', methods=['POST'])
def signup_route():
    return signup()

@auth_blueprint.route('/login', methods=['POST'])
def login_route():
    print("login route")
    return login()


@auth_blueprint.route('/add-contact', methods=['POST'])
def single_contact():
    return add_single_contact()

@auth_blueprint.route('/upload-contacts', methods=['POST'])
def upload_multiple_contacts():
    return upload_contacts()

@auth_blueprint.route('/get-contacts', methods=['GET'])
def get_contacts():
    return get_all_contacts()


@auth_blueprint.route('/send_bulk_sms',methods=["POST"])
def send_sms():
    print("send sms route")
    return send_bulk_sms()