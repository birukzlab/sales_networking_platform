# app/routes.py
from flask import Blueprint, render_template, jsonify
from services.data_aggregator import fetch_random_users

# Define a blueprint for our main routes
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/fetch_users')
def fetch_users():
    """
    Fetch random users using the data aggregator and return the results as JSON.
    """
    # Fetch 5 random users for example purposes
    df = fetch_random_users(n=10)
    # Convert DataFrame to a list of dictionaries for JSON serialization
    
    return jsonify(df)