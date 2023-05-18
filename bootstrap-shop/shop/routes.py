from sqlalchemy.sql.functions import user
#from flask_login import login_user, login_required, logout_user, current_user
from flask import redirect, url_for, flash, render_template, request, session
from .models import *
from .forms import *
from shop import app, db


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('index.html')
