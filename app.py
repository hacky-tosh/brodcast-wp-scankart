from flask import Flask, jsonify
from dotenv import load_dotenv
import os
from routes.auth_routes import auth_blueprint
from flask.templating import render_template
from flask_cors import CORS
from public_routes.user_routes import user_blueprint



load_dotenv()


app = Flask(__name__)
CORS(app) 
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


app.register_blueprint(auth_blueprint, url_prefix='/api')
app.register_blueprint(user_blueprint, url_prefix='/user')






@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Welcome to the API'}), 200


if __name__ == '__main__':
    app.run(port=4000, debug=True)
