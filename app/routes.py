from app import app, db
from flask import render_template, url_for, redirect, flash, jsonify, request
from app.forms import TitleForm, LoginForm, RegisterForm, ContactForm, PostForm
from app.models import Title, Contact, Post, User
from flask_login import current_user, login_user, logout_user, login_required
import requests


@app.route('/')
@app.route('/index')
def index():
    products = [
        {
            'id': 1001,
            'title': 'Soap',
            'price': 3.98,
            'desc': 'Very clean soapy soap, descriptive text'
        },
        {
            'id': 1002,
            'title': 'Grapes',
            'price': 4.56,
            'desc': 'A bundle of grapey grapes, yummy'
        },
        {
            'id': 1003,
            'title': 'Pickles',
            'price': 5.67,
            'desc': 'A jar of pickles is pickly'
        },
        {
            'id': 1004,
            'title': 'Juice',
            'price': 2.68,
            'desc': 'Yummy orange juice'
        }
    ]

    header = Title.query.get(1).title

    return render_template('index.html', title='Home', products=products, header=header)


@app.route('/title', methods=['GET', 'POST'])
def title():
    form = TitleForm()

    if form.validate_on_submit():
        header = form.title.data

        data = Title.query.get(1)
        data.title = header

        # add to session and commit
        db.session.add(data)
        db.session.commit()

        flash(f'You have changed the title to {header}')
        return redirect(url_for('index'))

    return render_template('form.html', title='Change Title', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    # if user is already logged in, send them to the profile page
    if current_user.is_authenticated:
        flash('You are already logged in!')
        return redirect(url_for('profile', username=current_user.username))

    if form.validate_on_submit():
        # query the database for the user trying to log in
        user = User.query.filter_by(email=form.email.data).first()

        # if user doesn't exist, reload the page and flash message
        # or if the password doesn't match the password stored
        if user is None or not user.check_password(form.password.data):
            flash('Credentials are incorrect.')
            return redirect(url_for('login'))

        # if user does exist, and credentials are correct, log them in and send them to their profile page
        login_user(user, remember=form.remember_me.data)
        # flash('You are now logged in!')
        return redirect(url_for('profile', username=user.username))

    return render_template('form.html', title='Login', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    # check to see if the user is already logged in, if so send to index
    if current_user.is_authenticated:
        flash('You are already logged in.')
        return redirect(url_for('index'))

    if form.validate_on_submit():
        user = User(
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            username = form.username.data,
            email = form.email.data,
            url = form.url.data,
            age = form.age.data,
            bio = form.bio.data
        )

        # call set password to create hash
        user.set_password(form.password.data)

        db.session.add(user)
        db.session.commit()

        flash(f'Thanks for registering, an e-mail confirmation has been sent to {form.email.data}')
        return redirect(url_for('login'))

    return render_template('form.html', title='Register', form=form)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        try:
            contact = Contact(
                name = form.name.data,
                email = form.email.data,
                message = form.message.data
            )

            db.session.add(contact)
            db.session.commit()

            flash(f'Thanks for your submission, we will contact you shortly. A copy has been sent to {form.email.data}')
            return redirect(url_for('index'))
        except:
            flash('Sorry your submission did not go through. Try again.')
            return redirect(url_for('contact'))

    return render_template('form.html', form=form, title='Contact Us')


@app.route('/checkout')
def checkout():
    products = [
        {
            'id': 1001,
            'title': 'Soap',
            'price': 3.98,
            'desc': 'Very clean soapy soap, descriptive text'
        },
        {
            'id': 1002,
            'title': 'Grapes',
            'price': 4.56,
            'desc': 'A bundle of grapey grapes, yummy'
        },
        {
            'id': 1003,
            'title': 'Pickles',
            'price': 5.67,
            'desc': 'A jar of pickles is pickly'
        },
        {
            'id': 1004,
            'title': 'Juice',
            'price': 2.68,
            'desc': 'Yummy orange juice'
        }
    ]

    return render_template('checkout.html', title='Checkout', products=products)


@login_required
@app.route('/profile/<username>', methods=['GET', 'POST'])
def profile(username=''):
    form = PostForm()

    # posts = Post.query.all()

    user = User.query.filter_by(username=username).first()

    if form.validate_on_submit():
        post = Post(tweet=form.tweet.data, user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('profile', username=username))

    return render_template('profile.html', title='Profile', form=form, user=user)


@app.route('/logout')
def logout():
    logout_user()
    # flash('You have been logged out!')
    return redirect(url_for('login'))



# API call return posts for username
@app.route('/api/posts', methods=['GET', 'POST'])
def posts():
    username = request.headers.get('username')

    user  = User.query.filter_by(username=username).first()
    customers = [
        {
            'name': 'John',
            'age': 22
        },
        {
            'name': 'Alex',
            'age': 12
        },
        {
            'name': 'Annie',
            'age': 67
        },
        {
            'name': 'Jake',
            'age': 45
        },
        {
            'name': 'Bill',
            'age': 32
        },
    ]

    try:
        posts = []

        for post in posts:
            if customer['age'] < int(max) and customer['age'] > int(min):
                range.append(customer)

        if name:
            customers = []
            for customer in range:
                if customer['name'] == name:
                    customers.append(customer)
            return jsonify(customers)

        return jsonify(range)
    except:
        return jsonify({ 'error': 'Incompatible parameter values'})


    return jsonify({ 'error': 'Something went wrong' })
