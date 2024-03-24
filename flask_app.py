 # Import flask-package
from flask import Flask

# create variable
app=Flask(__name__)

# Create default route
@app.route('/')
def home():
    return "<p>Huiswerk les 11, vraag 6</p>"
