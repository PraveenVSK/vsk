from flask import Blueprint, render_template
from flask_login import login_required

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')  # Your base HTML modified with extends base.html

@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')  # Empty for now

@main.route('/about')
def about():
    return render_template('pages/about.html', title='About')

@main.route('/academics')
def academics():
    return render_template('pages/academics.html', title='Academics')

@main.route('/departments')
def departments():
    return render_template('pages/departments.html', title='Departments')