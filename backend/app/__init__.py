from flask import Flask

app = Flask(__name__, template_folder="../templates", static_folder="../static")

# Load environment variables from .env file

from app import routes
