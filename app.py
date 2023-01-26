import logging
import os
from flask_mail import Mail
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from rq import Queue
from rq.registry import ScheduledJobRegistry
from redis import Redis
from rq_scheduler import Scheduler
from datetime import date
from datetime import datetime
from flask_login import UserMixin
from flask_login import login_user, current_user, logout_user, login_required
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DecimalField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange
from flask import Flask, render_template, url_for, flash, redirect, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from waitress import serve
import random
import string
import os
import secrets
from PIL import Image
import psutil
import json
from dijkstra import run_left_stairs, run_central_stairs, run_right_stairs

print('\nStarting Server...\n\x1b[34m \x1b[1m\n                                                .....                   \n          .....................               ..........                \n         .......................             ...........                \n          .....................               ..........                \n                                                .....                   \n                                                                        \n                                                                        \n                                                                        \n                                                                        \n                                                                        \n     ........                                       ........            \n      .......                                      ........             \n      ........                                    .........             \n       ........                                  .........              \n        .........                               .........               \n         ..........                           ..........                \n           ...........                     ...........                  \n             ................       ................                    \n                 ...............................                        \n                     .......................                            \n                            .........\n        \x1b[0m\n      ')

app = Flask(__name__)

r = Redis(host='', # Change to the host to the redis server, if you're using redislabs, it's the host in the connection string
    port=15723, password="") # Put the redis server password & port here, if you're not using a password, just delete the password= part
queue = Queue(name='occupy_queue', connection=r)
scheduler = Scheduler(queue=queue, connection=r, interval=1)

try:
    r.ping() 
    print('SERVER: Successfully Connected to Redis @ "{}"'.format("[ENTER REDIS SERVER HERE]")) 
except Exception as errlog:
    print("ERROR: Couldn't connect to Redis Server. |", errlog)

registry = ScheduledJobRegistry(queue=queue)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
mail = Mail(app)

logging.basicConfig(filename='flask-tailwind.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

app.config['SECRET_KEY'] = 'BDy9asydnasdna98n^B&D*tsa87dvbats67asrv67r'

POSTGRES = {
    'user': 'user',
    'pw': 'password',
    'db': 'db_name',
    'host': 'db_host',
    'port': 'db_port',
}

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask-server.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)

from email_sender import send_reset_email, send_order_email # IMPORT THE FUNCTIONS TO SEND THE EMAIL FROM ANOTHER FILE SINCE IT'S NEARLY 2000 LINES OF CODE/HTML

def run_dijkstras(items):
    """Runs the dijkstra algorithm on the items passed in and returns the smallest distance and path from all 3 stairs.

    Args:
        items (list): The list of all the nodes that need to be visited.
    """
    smallest = None
    left_dist, left_path = run_left_stairs(items)
    cent_dist, cent_path = run_central_stairs(items)
    right_dist, right_path = run_right_stairs(items)
    if sum(left_dist.values()) < sum(cent_dist.values()) and sum(left_dist.values()) < sum(right_dist.values()):
        smallest = {'dist': sum(left_dist.values()), 'path': left_path, 'type': 'left'}
    if sum(cent_dist.values()) < sum(left_dist.values()) and sum(cent_dist.values()) < sum(right_dist.values()):
        smallest = {'dist': sum(cent_dist.values()), 'path': cent_path, 'type': 'central'}
    if sum(right_dist.values()) < sum(left_dist.values()) and sum(right_dist.values()) < sum(cent_dist.values()):
        smallest = {'dist': sum(right_dist.values()), 'path': right_path, 'type': 'right'}
    return smallest

def find_rooms():
    """Finds all the rooms that need housekeeping for each floor and runs the dijkstra function with the respective nodes and the floor number.
    
    Returns:
        dict: A dictionary containing the smallest distance and path for each floor as well as the stairs used for the path.
    """
    flr1_smallest, flr2_smallest, flr3_smallest, flr4_smallest, flr5_smallest = {}, {}, {}, {}, {}
    flr1_items, flr2_items, flr3_items, flr4_items, flr5_items = [], [], [], [], []
    nearest_node = {}
    for i in range(1,6):
        nearest_node.update({f"{i}00": "node4", f"{i}01": "node3", f"{i}02": "node1", f"{i}03": "node10", f"{i}04": "node12", f"{i}05": "node18", f"{i}06": "node19", f"{i}07": "node20", f"{i}08": "node19", f"{i}09": "node18", f"{i}10": "node17", f"{i}11": "node13", f"{i}12": "node16", f"{i}13": "node15", f"{i}14": "node14", f"{i}15": "node12", f"{i}16": "node11", f"{i}17": "node9", f"{i}18": "node7", f"{i}19": "node8"})
    floor1 = db.session.query(room) \
        .with_entities(room.num, room.floor, room.housekeeping_status) \
        .filter(room.floor=="1", room.housekeeping_status=="Awaiting Cleaning").all()
    floor2 = db.session.query(room) \
        .with_entities(room.num, room.floor, room.housekeeping_status) \
        .filter(room.floor=="2", room.housekeeping_status=="Awaiting Cleaning").all()
    floor3 = db.session.query(room) \
        .with_entities(room.num, room.floor, room.housekeeping_status) \
        .filter(room.floor=="3", room.housekeeping_status=="Awaiting Cleaning").all()
    floor4 = db.session.query(room) \
        .with_entities(room.num, room.floor, room.housekeeping_status) \
        .filter(room.floor=="4", room.housekeeping_status=="Awaiting Cleaning").all()
    floor5 = db.session.query(room) \
        .with_entities(room.num, room.floor, room.housekeeping_status) \
        .filter(room.floor=="5", room.housekeeping_status=="Awaiting Cleaning").all()
    for i in floor1:
        flr1_items.append(nearest_node[str(i.num)])
    for i in floor2:
        flr2_items.append(nearest_node[str(i.num)])
    for i in floor3:
        flr3_items.append(nearest_node[str(i.num)])
    for i in floor4:
        flr4_items.append(nearest_node[str(i.num)])
    for i in floor5:
        flr5_items.append(nearest_node[str(i.num)])
    if len(floor1) != 0:
        flr1_smallest = json.dumps(run_dijkstras(flr1_items))
    if len(floor2) != 0:
        flr2_smallest = json.dumps(run_dijkstras(flr2_items))
    if len(floor3) != 0:
        flr3_smallest = json.dumps(run_dijkstras(flr3_items))
    if len(floor4) != 0:
        flr4_smallest = json.dumps(run_dijkstras(flr4_items))
    if len(floor5) != 0:
        flr5_smallest = json.dumps(run_dijkstras(flr5_items))
    return flr1_smallest, flr2_smallest, flr3_smallest, flr4_smallest, flr5_smallest

def checkavailable(Roomtype):
    """Checks if there's any available rooms of the specified type and returns the room number of the first available room

    Args:
        Roomtype (integer): The type of room to check for availability

    Returns:
        integer: returns the room number of the first available room of the specified type
    """
    record = db.session.query(room) \
        .with_entities(room.num, room.status, room.owner, room.type) \
        .filter(room.status.like("Vacant"), room.type.like(Roomtype)).first()
    try:
        if len(record) != 0:
            return record.num
        else:
            return None # "No available rooms"
    except:
        return None # "No available rooms"

def checkout(id, roomnum):
    """Checks out a room and updates the database

    Args:
        id (string): _description_
        roomnum (_type_): _description_

    Returns:
        None: Returns none so that nothing can be used from the function.
    """
    db.session.query(room).filter(room.num == roomnum).update({"dnd": (False), "occupant": (""), "owner": (""), "status": ("Vacant"), "housekeeping_status": ("Awaiting Cleaning")})
    db.session.query(order).filter(order.id==id).update({"assignedroom": (""), "expired": ("True")})
    db.session.commit()
    print("CHECKOUT: Room {} has been checked out.".format(roomnum))
    return None

# These functions' purpose is to generate a random string of characters to be used as a unique ID for the room and booking IDs
def random_string_generator(str_size, allowed_chars):
    str = ''.join(random.choice(allowed_chars) for x in range(str_size))
    if db.session.query(db.exists().where(room.id != str)).scalar():
        return str
    else: 
        str = ''.join(random.choice(allowed_chars) for x in range(str_size))
        return str
    
def booking_id_generator(str_size, allowed_chars):
    str = ''.join(random.choice(allowed_chars) for x in range(str_size))
    if db.session.query(db.exists().where(order.id != str)).scalar():
        return str
    else: 
        str = ''.join(random.choice(allowed_chars) for x in range(str_size))
        return str

def get_date():
    today = date.today()
    # dd/mm/YY
    strdate = today.strftime("%d/%m/%Y")
    return strdate

# This function is very useful to grab room data for API calls, reception page and housekeeping page
def get_room_data():
    """A function that grabs all the room data, and returns it in a dictionary. Very useful for the receptionist, housekeeping, and dashboard for displaying rooms and analytics.

    Returns:
        dictionaries: returns all the floors with the relative rooms and their id, number, status, floor, owner, type, and housekeeping status
    """
    floor1 = db.session.query(room) \
        .with_entities(room.id, room.num, room.status, room.floor, room.owner, room.type, room.housekeeping_status) \
        .filter(room.floor=="1").all()
    floor2 = db.session.query(room) \
        .with_entities(room.id, room.num, room.status, room.floor, room.owner, room.type, room.housekeeping_status) \
        .filter(room.floor=="2").all()
    floor3 = db.session.query(room) \
        .with_entities(room.id, room.num, room.status, room.floor, room.owner, room.type, room.housekeeping_status) \
        .filter(room.floor=="3").all()
    floor4 = db.session.query(room) \
        .with_entities(room.id, room.num, room.status, room.floor, room.owner, room.type, room.housekeeping_status) \
        .filter(room.floor=="4").all()
    floor5 = db.session.query(room) \
        .with_entities(room.id, room.num, room.status, room.floor, room.owner, room.type, room.housekeeping_status) \
        .filter(room.floor=="5").all()
    allrooms = db.session.query(room) \
        .with_entities(room.id, room.num, room.status, room.floor, room.owner, room.type, room.housekeeping_status) \
        .filter().all()
    return floor1, floor2, floor3, floor4, floor5, allrooms

def occupyroom(id, email, type, checkout):
    """If there's an available room of the specified type, it will assign the room to the user and update the database

    Args:
        id (string): Order ID
        email (string): User email
        type (string): Room type (to check available rooms)
        checkout (string): Checkout date (to queue the checkout job)

    Returns:
        string/None: returns if the room was successfully occupied or not
    """
    roomnum = checkavailable(type)
    if roomnum != None:
      db.session.query(room).filter(room.num==roomnum).update({"owner": (email), "status": ("Occupied")})
      db.session.query(order).filter(order.id==id).update({"assignedroom": (roomnum)})
      db.session.commit()
      print(f"SERVER: NEW ROOM OCCUPIED! ROOM NUMBER: {roomnum}")
      try:
          list = checkout.split("/")
          job = scheduler.enqueue_at(datetime(int(list[2]), int(list[1]), int(list[0]), 11, 59), 'checkout', id, roomnum)
          print("SUCCESS: Enqueued Job;",job, "(Checkout Job)")
      except Exception as e:
            print("ERROR: Failed to queue job (Checkout Job) |", e)
      return "Done!"
    else:
      print("WARNING: No available rooms!")
      return None

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def cb(id, email, firstname, lastname, address, housenum, city, county, residence, postcode, phone, type, checkin, checkout):
    """Creates a new order in the database and if the check-in date is after today, it will queue the check-in job

    Args: The passed arguments correspond to the order table in the database as well as input fields in the booking form
    """
    if phone == None:
        phonex = "N/A"
    else:
        phonex = phone
    db.session.add(order(id=id, email=email, firstname=firstname, lastname=lastname, address=address, housenum=housenum, city=city, county=county, countryresidence=residence, postcode=postcode, phone=phonex, type=type, checkin=checkin, checkout=checkout, expired="False", assignedroom="N/A", created_on=datetime.utcnow()))
    db.session.commit()
    list = checkin.split('/')
    # Queue another function to occupy the room instead of doing it on booking so it can be done at the right time
    if checkin == get_date():
        occupyroom(id, email, type, checkout)
    else:
        try:
            job = scheduler.enqueue_at(datetime(int(list[2]), int(list[1]), int(list[0]), 11, 59), 'occupyroom', id, email, type, checkout)
            print("SUCCESS: Enqueued Job;",job)
        except Exception as e:
            print("ERROR: Failed to queue job: creating booking anyway. |", e)
            occupyroom(id, email, type, checkout)

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class OrderForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    firstname = StringField('First name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    lastname = StringField('Last name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    address = StringField('Address',
                           validators=[DataRequired(), Length(min=2, max=40)])
    housenum = DecimalField('House/Flat Number',
                            validators=[NumberRange(min=0, max=1000)])
    city = StringField('City',
                           validators=[DataRequired(), Length(min=2, max=20)])
    county = StringField('County',
                           validators=[DataRequired(), Length(min=2, max=30)])
    residence = StringField('Country of Residence',
                           validators=[DataRequired(), Length(min=2, max=30)])
    postcode = StringField('Postcode',
                           validators=[DataRequired(), Length(min=2, max=10)]) 
    phone = StringField('Phone number (+44)')
    submit = SubmitField('Pay as Guest')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    displayname = StringField('Display Name',
                           validators=[Length(min=0, max=32)])
    description = TextAreaField('Description', validators=[Length(min=0, max=190)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')

class BookingForm(FlaskForm):
    adults = DecimalField('Adults',
                            validators=[DataRequired(), NumberRange(min=0, max=4)])
    children = DecimalField('Children',
                            validators=[NumberRange(min=0, max=3)])
    checkin = StringField('Date',validators=[DataRequired()])
    checkout = StringField('Date',validators=[DataRequired()])
    
    submit = SubmitField('Submit')
    
    def validate(self):
        rv = FlaskForm.validate(self)
        roomtype = ""
        children = self.children.data
        adults = self.adults.data
        if not rv:
            return False
        try:
            checkindate = str(self.checkin.data).split('/')
            checkoutdate = str(self.checkout.data).split('/')
            d0 = date(int(checkindate[2]), int(checkindate[1]), int(checkindate[0]))
            d1 = date(int(checkoutdate[2]), int(checkoutdate[1]), int(checkoutdate[0]))
            delta = d1 - d0
            if delta.days < 0:
                self.submit.errors.append('Enter a valid date range')
                return False
            elif delta.days > 14:
                self.submit.errors.append("Can't book over two weeks")
                return False
        except:
            self.submit.errors.append('Enter the date in the format D/M/Y')
            return False
        if children == 0 and (adults == 1):
            roomtype = "Single"
        elif children == 0 and adults == 2:
            roomtype = "Double"
        elif (children == 1 and adults == 2) or (children == 2 and adults == 1):
            roomtype = "Double"
        elif (children+adults == 3) or (adults == 3):
            roomtype = "Triple"
        elif (adults == 1 or adults == 2) or (children == 1 or children == 2):
            roomtype = "Quad"
        elif (children+adults == 4):
            roomtype = "Quad"
        else:
            roomtype = "N/A"
        roomnum = checkavailable(roomtype)
        if roomnum != None:
            return True
        else: 
            self.submit.errors.append("No more available rooms")
            return False
    
    def validate_2(self):
        rv = FlaskForm.validate_2(self)
        if not rv:
            return False
        # Check if the date is before today
        try:
            print("SERVER: Validate 2 ran.")
            checkindate = str(self.checkin.data).split('/')
            checkoutdate = str(self.checkout.data).split('/')
            d0 = datetime(int(checkindate[2]), int(checkindate[1]), int(checkindate[0]))
            d1 = datetime(int(checkoutdate[2]), int(checkoutdate[1]), int(checkoutdate[0]))
            today = date.today()
            if d0.date() < today or d1.date() < today:
                self.submit.errors.append('Please enter a date that is not in the past.')
                return False
            else:
                return True
        except:
            self.submit.errors.append('Please make sure to format the date as D/M/Y')
            return False
        return True

class RequestResetForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email. You must register first.')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')

class CreateBookingForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    roomtype = StringField('Room Type', validators=[DataRequired()])
    checkin = StringField('Check-in Date',validators=[DataRequired()])
    checkout = StringField('Check-out Date',validators=[DataRequired()])
    
    submit = SubmitField('Check-in')
    def validate(self):
        rv = FlaskForm.validate(self)
        roomtype = self.roomtype.data
        if not rv:
            return False

        try:
            checkindate = str(self.checkin.data).split('/')
            checkoutdate = str(self.checkout.data).split('/')
            d0 = date(int(checkindate[2]), int(checkindate[1]), int(checkindate[0]))
            d1 = date(int(checkoutdate[2]), int(checkoutdate[1]), int(checkoutdate[0]))
            delta = d1 - d0
            if delta.days < 0:
                self.submit.errors.append('Enter a valid date range')
                return False
            elif delta.days > 14:
                #print(delta.days)
                self.submit.errors.append("Can't book over two weeks")
                return False
        except:
            self.submit.errors.append('Enter the date in the format D/M/Y')
            return False
        roomnum = checkavailable(roomtype)
        if roomnum != None:
            return True
        else: 
            self.submit.errors.append("No more available rooms")
            return False

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String(20), nullable=False, default='Guest')
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    # columns for user profile
    description = db.Column(db.String(190), nullable=True)
    display_name = db.Column(db.String(32), nullable=True)
    status = db.Column(db.String(20), nullable=True)
    

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.role}', '{self.image_file}')"
   
class room(db.Model):
    id = db.Column(db.String(6), primary_key=True, nullable=False)
    num = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Text, default="Vacant")
    floor = db.Column(db.String(3), nullable=False)
    owner = db.Column(db.String(20), default="N/A")
    type = db.Column(db.String(10), nullable=False)
    housekeeping_status = db.Column(db.String(30), default="Clean")
    
    dnd = db.Column(db.Boolean, default=False)
    occupant = db.Column(db.String(20), default="")
    
    def __init__(self, id, num, status, floor, owner, type, housekeeping_status, dnd, occupant):
        self.id = id
        self.num = num
        self.status = status
        self.floor = floor
        self.owner = owner
        self.type = type
        self.housekeeping_status = housekeeping_status
        self.dnd = dnd
        self.occupant = occupant

class order(db.Model):
    id = db.Column(db.String(6), primary_key=True, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)
    firstname = db.Column(db.String(15))
    lastname = db.Column(db.String(15))
    address = db.Column(db.String(30))
    housenum = db.Column(db.String(5))
    city = db.Column(db.String(20))
    county = db.Column(db.String(20))
    countryresidence = db.Column(db.String(20))
    postcode = db.Column(db.String(20))
    phone = db.Column(db.String(20), nullable=True, default="N/A")
    
    type = db.Column(db.String(10), nullable=False)
    checkin = db.Column(db.String(10), nullable=False)
    checkout = db.Column(db.String(10), nullable=False)
    
    expired = db.Column(db.String(10), default="False")
    assignedroom = db.Column(db.String(20), nullable=True)
    
    created_on = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow())
    
    def __init__(self, id, email, firstname, lastname, address, housenum, city, county, countryresidence, postcode, phone, type, checkin, checkout, expired, assignedroom, created_on):
        self.id = id
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.housenum = housenum
        self.city = city
        self.county = county
        self.countryresidence = countryresidence
        self.postcode = postcode
        self.phone = phone
        
        self.type = type
        self.checkin = checkin
        self.checkout = checkout
        
        self.expired = expired
        self.assignedroom = assignedroom
    
        self.created_on = created_on
 
# WEB PAGE ROOTS

@app.route('/', methods=['POST', 'GET'])
def root():
    form = BookingForm()
    if form.validate_on_submit():
        return redirect(url_for('finishbooking')+f"?adults={form.adults.data}&children={form.children.data}&checkin={form.checkin.data}&checkout={form.checkout.data}")
    return render_template('landing.html', Name='Home', form=form)

@app.route('/home')
@login_required
def home():
    records = db.session.query(order) \
        .with_entities(order.id, order.email, order.checkin, order.checkout, order.type, order.created_on) \
        .filter().order_by(order.created_on.desc()).limit(8).all()
    allorders = db.session.query(order) \
        .with_entities(order.id) \
        .filter().all()
    guestrooms = db.session.query(room, order) \
        .with_entities(room.id, room.num, order.email, room.type, order.checkin, order.checkout) \
        .filter(room.owner == order.email, room.owner == current_user.email, order.assignedroom == room.num).all() # .filter(room.owner.like(order.email)).all()
    latestchanges = db.session.query(order) \
        .with_entities(order.id, order.email, order.checkin, order.checkout, order.expired) \
        .filter().order_by(order.checkin.asc()).limit(5).all()
    table_file = url_for('static', filename='profile_pics/default.jpg')
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template("dash.html", Name="Dashboard", image_file=image_file, records=records, table_file=table_file, guestrooms=guestrooms, allorders=allorders, latestchanges=latestchanges) #, price=""

@app.route("/register", methods=['GET', 'POST'])
def registerpage():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, role="Guest", password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('root'))

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn

@app.route("/checkout", methods=['GET', 'POST'])
def finishbooking():
    form = OrderForm()
    args = request.args
    adults = int(args["adults"])
    children = int(args["children"])
    checkin = args["checkin"]
    checkout = args["checkout"]
    roomtype = ""
    price = ""
    price2 = ""
    if children == 0 and (adults == 1):
        roomtype = "Single"
        price = "£65"
        price2 = "65"
    elif children == 0 and adults == 2:
        roomtype = "Double"
        price = "£85"
        price2 = "85"
    elif (children == 1 and adults == 2) or (children == 2 and adults == 1):
        roomtype = "Double"
        price = "£95"
        price2 = "95"
    elif (adults == 1 or adults == 2) or (children == 1 or children == 2):
        roomtype = "Quad"
        price = "£115"
        price2 = "115"
    elif (children+adults == 3) or (adults == 3):
        roomtype = "Triple"
        price = "£100"
        price2 = "100"
    elif (children+adults == 4):
        roomtype = "Quad"
        price = "£115"
        price2 = "115"
    else:
        roomtype = "N/A"
        price = "£80"
        price2 = "80"
    if form.validate_on_submit():
        idstr = booking_id_generator(6, string.ascii_letters)
        cb(idstr, form.email.data, form.firstname.data, form.lastname.data, form.address.data, form.housenum.raw_data[0], form.city.data, form.county.data, form.residence.data, form.postcode.data, form.phone.data, roomtype, checkin, checkout)
        try:
            send_order_email(form.email.data, idstr, form.firstname.data, url_for('root', _external=True), price2, form.firstname.data, form.lastname.data, form.phone.data, form.housenum.raw_data[0], form.address.data, form.city.data, form.county.data, form.postcode.data, form.residence.data, roomtype, checkin, checkout)
        except:
            print("Failed to send email (Booking Email)")
        return redirect(url_for('thankyou'))
    return render_template('finishbooking.html', Name="Finish Booking", adults=adults, children=children, checkin=checkin, checkout=checkout, type=roomtype, price=price, form=form)

@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.display_name = form.displayname.data
        current_user.description = form.description.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.displayname.data = current_user.display_name
        form.description.data  = current_user.description
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form, page="Account Settings", Name="Account")

@app.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        email = form.email.data
        token = user.get_reset_token()
        rp_link = url_for('reset_token', token=token, _external=True)
        flash('An email has been sent with instructions to reset your password.', 'info')
        send_reset_email(rp_link, email)
        return redirect(url_for('login'))
    return render_template('reset_request.html', title='Reset Password', form=form)

@app.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token.', 'warning')
        return redirect(url_for('reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Your password has been updated! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('reset_token.html', title='Reset Password', form=form)

@app.route('/bookingredirect', methods=['GET', 'POST'])
@login_required
def bookingredirect():
    args = request.args
    adults = int(args["adults"])
    children = int(args["children"])
    checkin = args["checkin"]
    checkout = args["checkout"]
    roomtype = ""
    price = ""
    if children == 0 and (adults == 1):
        roomtype = "Single"
        price = "65"
    elif children == 0 and adults == 2:
        roomtype = "Double"
        price = "85"
    elif (children == 1 and adults == 2) or (children == 2 and adults == 1):
        roomtype = "Double"
        price = "95"
    elif (children+adults == 3) or (adults == 3):
        roomtype = "Triple"
        price = "100"
    elif (adults == 1 or adults == 2) or (children == 1 or children == 2):
        roomtype = "Quad"
        price = "115"
    elif (children+adults == 4):
        roomtype = "Quad"
        price = "115"
    else:
        roomtype = "N/A"
        price = "80"
    idstr = booking_id_generator(6, string.ascii_letters)
    cb(idstr, current_user.email, current_user.username, "QuickPay", "QuickPay", "QuickPay", "QuickPay", "QuickPay", "QuickPay", "QuickPay", "QuickPay", roomtype, checkin, checkout)
    try:
        send_order_email(current_user.email, idstr, current_user.username, url_for('root', _external=True), price, current_user.username, " ", "Quickpay", "Quickpay", "Quickpay", "Quickpay", "Quickpay", "Quickpay", "Quickpay", roomtype, checkin, checkout)
        print("SUCCESS: Created order and sent email (Booking Email).")
    except:
        print("ERROR: Failed to send email (Booking Email)")
    return redirect(url_for('thankyou'))

@app.route('/checkout/thankyou', methods=['GET'])
def thankyou():
    return render_template('thankyou.html', Name='Thank you')

@app.route('/manage/<id>', methods=['GET'])
@login_required
def roommanage(id):
    roomdata = db.session.query(room) \
        .with_entities(room.id, room.num, room.status, room.floor, room.owner, room.type, room.dnd, room.occupant) \
        .filter(room.id.like(id)).first() 
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template("manageroom.html", Name="Manage Room", id=id, roomdata=roomdata, image_file=image_file)

@app.route('/housekeeping', methods=['GET'])
@login_required
def housekeeping():
    if current_user.role == "Housekeeper" or current_user.role == "Manager":
        image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
        floor1, floor2, floor3, floor4, floor5, allrooms=get_room_data()
        return render_template('housekeeping.html', Name="Housekeeping", image_file=image_file, floor1=floor1, floor2=floor2, floor3=floor3, floor4=floor4, floor5=floor5, allrooms=allrooms)
    else:
        return redirect(url_for('home'))

@app.route('/receptionist', methods=['GET', 'POST'])
@login_required
def receptionist():
    form = CreateBookingForm()
    price = ""
    roomtype = form.roomtype.data
    email = form.email.data
    checkin = form.checkin.data
    checkout = form.checkout.data
    if form.validate_on_submit():
        if roomtype.lower() == "single":
            price = "65"
        elif roomtype.lower() == "double":
            price = "85"
        elif roomtype.lower() == "triple":
            price = "100"
        elif roomtype.lower() == "quad":
            price = "115"
        else:
            price = "80"
        idstr = booking_id_generator(6, string.ascii_letters)
        cb(idstr, email, "Guest Booking", "Booking", "Booking", "Booking", "Booking", "Booking", "Booking", "Booking", "Booking", roomtype.capitalize(), checkin, checkout)
        try:
            send_order_email(email, idstr, "Guest Booking", url_for('root', _external=True), price, "Guest Booking", " ", "Booking", "Booking", "Booking", "Booking", "Booking", "Booking", "Booking", roomtype.capitalize(), checkin, checkout)
        except:
            print("ERROR: Failed to send email (Booking Email).")
    if current_user.role == "Receptionist" or current_user.role == "Manager":
        floor1, floor2, floor3, floor4, floor5, allrooms=get_room_data()
        image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
        return render_template('receptionist.html', Name="Receptionist", image_file=image_file, floor1=floor1, floor2=floor2, floor3=floor3, floor4=floor4, floor5=floor5, form=form, allrooms=allrooms)
    else:
        return redirect(url_for('home'))

@app.route('/profile/<id>', methods=['GET'])
@login_required
def profile(id):
    user = User.query.filter_by(id=id).first_or_404()
    image_file = url_for('static', filename='profile_pics/' + user.image_file)
    return render_template('profile.html', Name="Profile", user=user, image_file=image_file)

# API ROOTS

@app.route('/api/test', methods=['POST', 'GET'])
def test():
    if request.method == 'GET':
        msg = "Message101"
        print("SENT >>", msg)
        return msg
    print("RECEIVED >>",list(request.form))
    return "Message Received"

@app.route('/api/addroom', methods=['POST', 'GET'])
def addroom():
    if request.method == 'GET':
        idstr = random_string_generator(6, string.ascii_letters)
        db.session.add(room(id=idstr, num=101, status="Vacant", floor="1", owner="", type="Single", housekeeping_status="Clean"))
        db.session.commit() 
        return "Room Added"
    return "Message Received"

@app.route('/api/editroom/', methods=['POST', 'GET'])
def editroom():
    db.session.query(room).filter(room.id == "xoINGH").update({"owner": ("ayee_itzluke@icloud.com")})
    #db.session.query(order).filter(order.id == "CKrQsi").update({"assignedroom": ("101")})
    db.session.commit()
    return "Room Edited"

@app.route('/api/deleteroom/<id>', methods=['POST', 'GET'])
def deleteroom(id):
    if request.method == 'GET':
        room2 = room.query.get_or_404(id)
        db.session.delete(room2)
        db.session.commit()
        return "Room Deleted"
    return "Message Received"

@app.route('/api/GuestUser/<id>', methods=['POST', 'GET'])
def guestuser(id):
    db.session.query(User).filter(User.id == id).update({"role": ("Guest")})
    db.session.commit()
    return "User has been added as a Guest"

@app.route('/api/ReceptionistUser/<id>', methods=['POST', 'GET'])
def receptionistuser(id):
    db.session.query(User).filter(User.id == id).update({"role": ("Receptionist")})
    db.session.commit()
    return "User has been added as a receptionist"

@app.route('/api/HousekeepingUser/<id>', methods=['POST', 'GET'])
def housekeeperuser(id):
    db.session.query(User).filter(User.id == id).update({"role": ("Housekeeper")})
    db.session.commit()
    return "User has been added as a housekeeper"

@app.route('/api/ManagerUser/<id>', methods=['POST', 'GET'])
def manageruser(id):
    db.session.query(User).filter(User.id == id).update({"role": ("Manager")})
    db.session.commit()
    return "User has been added as a manager"

@app.route('/api/CleanRoom/<id>', methods=['POST', 'GET'])
def cleanroom(id):
    if request.method == 'GET':
        return "Please send a request through POST"
    else:
        roomid=request.get_json()['id']
        db.session.query(room).filter(room.id == id).update({"housekeeping_status": ("Clean")})
        db.session.commit()
        #print(roomid)
        return "Rooms has been cleaned :)"

@app.route('/api/CheckoutRequest', methods=['POST'])
def checkoutrequest():
    if request.method == 'POST':
        username=request.get_json()['usr']
        roomnum=request.get_json()['num']
        if username == "" and roomnum != "":
            db.session.query(room).filter(room.num == roomnum).update({"dnd": (False), "occupant": "", "owner": (""), "status": ("Vacant"), "housekeeping_status": ("Awaiting Cleaning")}) # , "dnd": (False), "occupant": ("")
            db.session.query(order).filter(order.assignedroom == roomnum).update({"assignedroom": (""), "expired": ("True")})
            db.session.commit()
            return jsonify({"message": "Success"})
        elif username != "" and roomnum == "":
            record = db.session.query(room) \
            .with_entities(room.num) \
            .filter(room.owner==username).first()
            roomnum2 = record[0]
            db.session.query(room).filter(room.owner == username).update({"dnd": (False), "occupant": "", "owner": (""), "status": ("Vacant"), "housekeeping_status": ("Awaiting Cleaning")})
            db.session.query(order).filter(order.assignedroom == roomnum2).update({"assignedroom": (""), "expired": ("True")})
            db.session.commit()
            return jsonify({"message": "Success"})
        else: # Check both
            check = db.session.query(room).filter(room.owner == username)
            check2 = db.session.query(room).filter(room.num == roomnum)
            if len(check) != 0:
                check.update({"dnd": (False), "occupant": "", "owner": (""), "status": ("Vacant"), "housekeeping_status": ("Awaiting Cleaning")})
                record = db.session.query(room) \
                .with_entities(room.num) \
                .filter(room.owner==username).first()
                roomnum2 = record[0]
                db.session.query(order).filter(order.assignedroom == roomnum2).update({"assignedroom": (""), "expired": ("True")})
            elif len(check2) != 0:
                check2.update({"dnd": (False), "occupant": "" , "owner": (""), "status": ("Vacant"), "housekeeping_status": ("Awaiting Cleaning")})
                db.session.query(order).filter(order.assignedroom == roomnum).update({"assignedroom": (""), "expired": ("True")})
            else:
                return jsonify({"message": "There was an error, please check what you input and try again."})
        # CHECK IF DATA IS A ROOM NUMBER, IF NOT THEN CHECK USERNAMES
        # IF NOTHING WORKS THEN SEND BACK AN ERROR AS JSON :)
        return jsonify({"message": "There was an error, please check what you input and try again."})

@app.route('/api/requesthousekeeping', methods=['POST'])
def requesthousekeeping():
    roomnum = request.get_json()['num']
    db.session.query(room).filter(room.num == roomnum).update({"housekeeping_status": ("Awaiting Cleaning")})
    db.session.commit()
    return jsonify({"message": "Success"})

@app.route('/api/addoccupant', methods=['POST'])
def add_occupant():
    roomnum = request.get_json()['num']
    occupant = request.get_json()['occupant']
    db.session.query(room).filter(room.num == roomnum).update({"occupant": (occupant)})
    db.session.commit()
    return jsonify({"message": "Success"})
    
@app.route('/api/toggleDND', methods=['POST'])
def toggleDND():
    roomnum = request.get_json()['num']
    status = db.session.query(room) \
                .with_entities(room.dnd) \
                .filter(room.num==roomnum).first()
    if status[0] == False:
        db.session.query(room).filter(room.num == roomnum).update({"dnd": (True)})
        db.session.commit()
        return jsonify({"message": "Success"})
    else:
        db.session.query(room).filter(room.num == roomnum).update({"dnd": (False)})
        db.session.commit()
        return jsonify({"message": "Success"})

@app.route('/api/buildrooms', methods=["GET"])
def buildrooms():
    # FUNCTION TO BUILD ALL THE ROOMS IF THE DATABASE IS EMPTY
    rooms = db.session.query(room) \
        .with_entities(room.id) \
        .filter().all()
    if len(rooms) == 0: # I'm so sorry for doing this but there's no clear better way to do this :( lord have mercy on my soul
        for floor in range(1,6):
            db.session.add(room(id=random_string_generator(6, string.ascii_letters), num=int(f"{floor}00"), status="Vacant", floor=str(floor), owner="", type="Double", housekeeping_status="Clean", dnd=False, occupant=""))
            db.session.add(room(id=random_string_generator(6, string.ascii_letters), num=int(f"{floor}01"), status="Vacant", floor=str(floor), owner="", type="Single", housekeeping_status="Clean", dnd=False, occupant=""))
            db.session.add(room(id=random_string_generator(6, string.ascii_letters), num=int(f"{floor}02"), status="Vacant", floor=str(floor), owner="", type="Single", housekeeping_status="Clean", dnd=False, occupant=""))
            db.session.add(room(id=random_string_generator(6, string.ascii_letters), num=int(f"{floor}03"), status="Vacant", floor=str(floor), owner="", type="Triple", housekeeping_status="Clean", dnd=False, occupant=""))
            db.session.add(room(id=random_string_generator(6, string.ascii_letters), num=int(f"{floor}04"), status="Vacant", floor=str(floor), owner="", type="Quad", housekeeping_status="Clean", dnd=False, occupant=""))
            db.session.add(room(id=random_string_generator(6, string.ascii_letters), num=int(f"{floor}05"), status="Vacant", floor=str(floor), owner="", type="Double", housekeeping_status="Clean", dnd=False, occupant=""))
            db.session.add(room(id=random_string_generator(6, string.ascii_letters), num=int(f"{floor}06"), status="Vacant", floor=str(floor), owner="", type="Single", housekeeping_status="Clean", dnd=False, occupant=""))
            db.session.add(room(id=random_string_generator(6, string.ascii_letters), num=int(f"{floor}07"), status="Vacant", floor=str(floor), owner="", type="Double", housekeeping_status="Clean", dnd=False, occupant=""))
            db.session.add(room(id=random_string_generator(6, string.ascii_letters), num=int(f"{floor}08"), status="Vacant", floor=str(floor), owner="", type="Quad", housekeeping_status="Clean", dnd=False, occupant=""))
            db.session.add(room(id=random_string_generator(6, string.ascii_letters), num=int(f"{floor}09"), status="Vacant", floor=str(floor), owner="", type="Double", housekeeping_status="Clean", dnd=False, occupant=""))
            db.session.add(room(id=random_string_generator(6, string.ascii_letters), num=int(f"{floor}10"), status="Vacant", floor=str(floor), owner="", type="Double", housekeeping_status="Clean", dnd=False, occupant=""))
            db.session.add(room(id=random_string_generator(6, string.ascii_letters), num=int(f"{floor}11"), status="Vacant", floor=str(floor), owner="", type="Quad", housekeeping_status="Clean", dnd=False, occupant=""))
            db.session.add(room(id=random_string_generator(6, string.ascii_letters), num=int(f"{floor}12"), status="Vacant", floor=str(floor), owner="", type="Single", housekeeping_status="Clean", dnd=False, occupant=""))
            db.session.add(room(id=random_string_generator(6, string.ascii_letters), num=int(f"{floor}13"), status="Vacant", floor=str(floor), owner="", type="Single", housekeeping_status="Clean", dnd=False, occupant=""))
            db.session.add(room(id=random_string_generator(6, string.ascii_letters), num=int(f"{floor}14"), status="Vacant", floor=str(floor), owner="", type="Double", housekeeping_status="Clean", dnd=False, occupant=""))
            db.session.add(room(id=random_string_generator(6, string.ascii_letters), num=int(f"{floor}15"), status="Vacant", floor=str(floor), owner="", type="Quad", housekeeping_status="Clean", dnd=False, occupant=""))
            db.session.add(room(id=random_string_generator(6, string.ascii_letters), num=int(f"{floor}16"), status="Vacant", floor=str(floor), owner="", type="Double", housekeeping_status="Clean", dnd=False, occupant=""))
            db.session.add(room(id=random_string_generator(6, string.ascii_letters), num=int(f"{floor}17"), status="Vacant", floor=str(floor), owner="", type="Double", housekeeping_status="Clean", dnd=False, occupant=""))
            db.session.add(room(id=random_string_generator(6, string.ascii_letters), num=int(f"{floor}18"), status="Vacant", floor=str(floor), owner="", type="Triple", housekeeping_status="Clean", dnd=False, occupant=""))
            db.session.add(room(id=random_string_generator(6, string.ascii_letters), num=int(f"{floor}19"), status="Vacant", floor=str(floor), owner="", type="Quad", housekeeping_status="Clean", dnd=False, occupant=""))
        db.session.commit()
        return "Successfully built"
    else:
        return "Rooms already built, clear the database to rebuild the rooms."

@app.route('/api/get_room_type_data', methods=['GET'])
def getroomtype():
    single = order.query.filter_by(type="Single").count()
    double = order.query.filter_by(type="Double").count()
    triple = order.query.filter_by(type="Triple").count()
    quad = order.query.filter_by(type="Quad").count()
    return jsonify({"Single": single, "Double": double, "Triple": triple, "Quad": quad})

@app.route('/api/get_memory_usage', methods=['GET'])
def getmemory():
    data = psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2
    return jsonify({'data': data})

@app.route('/api/clear_queue', methods=['GET'])
def clearqueue():
    queue.empty()
    return f"Queue cleared to {queue.count}"

@app.route('/api/get_queue', methods=['GET'])
def getqueue():
    return f"Queue: \n{queue.jobs} OR {queue.get_job_ids()}<br>Size: {queue.count}<br>Registry: {registry.get_job_ids()}<br>Registry Size: {registry.count}<br><br>Sheduler Jobs: {str(scheduler.get_jobs(with_times=True))}<br>Sheduler Size: {scheduler.count()}"

@app.route('/api/get_capacity', methods=['GET'])
def getcapacity():
    capacity = room.query.filter_by(status="Vacant").count() # Doesn't need to be converted to a percenatage due to it being exactly 100 rooms :)
    return jsonify({'data': capacity})

@app.route('/loginbackground', methods=['GET']) # For the iframe stuff :)
def loginbackground():
    return render_template('loginbackground.html')

@app.route('/controls', methods=['GET'])
@login_required
def controls():
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('controls.html', Name="Controls", current_user=current_user, image_file=image_file)

@app.route('/api/reset_database', methods=['GET'])
def reset():
    try:
        try:
            queue.empty()
        except:
            print("Couldn't clear the queue")
        db.session.query(order).delete()
        db.session.query(room).update({"status": ("Vacant"), "owner": (""), "housekeeping_status": ("Clean"), "dnd": (False), "occupant": ("")})
        db.session.commit()
        print("SERVER: USER HAS RESET THE DATABASE!")
        return "Successfully reset the database"
    except:
        print("ERROR: Failed to reset the database.")
        return "Failed to reset the database"

@app.route('/api/get_routes', methods=['GET'])
def get_routes():
    floor1, floor2, floor3, floor4, floor5 = find_rooms()
    return jsonify({"Floor 1": floor1, "Floor 2": floor2, "Floor 3": floor3, "Floor 4": floor4, "Floor 5": floor5})

# DJANGO TEMPLATE FUNCTIONS

@app.context_processor
def utility_processor():
    def get_price(type):
        if type == "Single":
            price="65"
            return f"{price}"
        elif type == "Double":
            price="95"
            return f"{price}"
        elif type == "Triple":
            price="100"
            return f"{price}"
        elif type == "Quad":
            price="115"
            return f"{price}"
        else:
            price="80"
            return f"{price}"
    return dict(format_price=get_price)
        
@app.context_processor
def utility_processor():
    def get_status_colour(housekeeping_status):
        if housekeeping_status == "Clean":
            colour="green-300"
            return f"{colour}"
        elif housekeeping_status == "Awaiting Cleaning":
            colour="yellow-300"
            return f"{colour}"
        elif housekeeping_status == "Awaiting Deep Clean":
            colour="red-300"
            return f"{colour}"
        else:
            colour="gray-400"
            return f"{colour}"
    return dict(get_status_colour=get_status_colour)

@app.context_processor
def utility_processor():
    def get_owner_image(owner):
        owner_record = db.session.query(User) \
            .with_entities(User.email, User.image_file) \
            .filter(User.email==owner).first()
        if owner == "" or owner == None:
            image_file = url_for('static', filename='profile_pics/default.jpg')
            return f"{image_file}"
        elif owner_record == None:
            image_file = url_for('static', filename='profile_pics/default.jpg')
            return f"{image_file}"
        else:
            image_file = url_for('static', filename='profile_pics/' + owner_record.image_file)
            return f"{image_file}"
    return dict(get_owner_image=get_owner_image)

@app.context_processor
def utility_processor():
    def get_room_no(email):
        rooms = db.session.query(room) \
            .with_entities(room.owner) \
            .filter(room.owner==email).all()
        if rooms:
            return f"{len(rooms)}"
        else:
            return f"0"
    return dict(get_room_no=get_room_no)

@app.context_processor
def utility_processor():
    def get_order_no(email):
        orders = db.session.query(order) \
            .with_entities(order.email) \
            .filter(order.email==email).all()
        if orders:
            return f"{len(orders)}"
        else:
            return f"0"
    return dict(get_order_no=get_order_no)

@app.context_processor
def utility_processor():
    def get_action(expired):
        if expired == "False":
            return f"Check-in"
        else:
            return f"Check-out"
    return dict(get_action=get_action)

# ERROR HANDLING

@app.errorhandler(400)
def resource_not_found(error):
    return f"Browser/Proxy Error/Bad Request | {error}"

@app.errorhandler(404)
def resource_not_found(error):
    return f"Page not found | {error}"

#db.create_all()

if __name__ == '__main__':  # Declare the main application
    print("SERVER: LIVE @ http://0.0.0.0:5000")
    #serve(app, host='0.0.0.0', port=5000)
    app.run(host='0.0.0.0', debug=True, port=5000)