from flask import Flask

app = Flask(__name__,template_folder="../templates")

from routes import user_routes