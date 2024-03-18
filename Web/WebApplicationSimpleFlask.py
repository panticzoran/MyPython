# Simple web application built using Flask

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! Hello, Jovane!'

# Ensure that Flask is installed
# Run the web application from shell:
#    export FLASK_APP=main.py (or whatever the file name is, instead of "main.py")
#    flask run
# Navigate to http://127.0.0.1:5000