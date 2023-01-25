# GoHotel Website (NEA-Public)
This is a public Github repo for my 2023 NEA Project.
I have a private repo that's fully configured and hosted although I need to make another repo in order to publish code as there's Redis, SQL, and Email server information and password configured in most of the files.

My project is a smart Hotel Management System using Flask &amp; tailwindcss, configuration will be needed to make it function completely which is detailed below.
## Features
* Flask backend /w API Routes 
* Shortest Path Algorithm for room cleaning
* Dashboard for room data analysis
* SQLite Database for Room, User, and Order data
* Redis Queue Database to schedule room check-ins and check-outs
* User Login /w Account Registration and reset password emails
* Booking/Order Emails
* Receptionist Page to Create bookings and Check-out guests
* Automatic scheduling of housekeeping
* Normal Occupant and Do Not Disturb system as well as ability to request housekeeping
* and much much more :)

## Pictures
Landing Page:
<img src="https://cdn.discordapp.com/attachments/659031245996556325/1067832974365708298/Landing.png" alt="Landing.png"/>
Order Page:
<img src="https://cdn.discordapp.com/attachments/659031245996556325/1067832973346480200/Order.png" alt="Order.png"/>
Login Page:
<img src="https://media.discordapp.net/attachments/659031245996556325/1067840927995011124/Login.png?width=1426&height=662" alt="Order.png"/>
Dashboard Page (1):
<img src="https://cdn.discordapp.com/attachments/659031245996556325/1067832972960612433/Dashboard.png" alt="Dashboard.png"/>
Dashboard Page (2):
<img src="" alt="Dashboard2.png"/>
Receptionist Page:
<img src="https://cdn.discordapp.com/attachments/659031245996556325/1067832973883359363/Receptionist.png" alt="Receptionist.png"/>
Housekeeping Page:
<img src="https://cdn.discordapp.com/attachments/659031245996556325/1067834053711118437/Housekeeping.png" alt="Housekeeping.png"/>
 Account Settings:
 <img src="https://cdn.discordapp.com/attachments/659031245996556325/1067832973627510804/Account_Settings.png" alt="Account_Settings.png"/>

## Before you run the program!
Firstly, make sure to have [node.js](https://nodejs.org/en/download/) and [python](https://www.python.org/downloads/) installed then;
1. run `npm i` OR `npm install` to install the node.js packages
2. run `pip install -r requirements.txt` to install all the required packages
3. if you intend on hosting it then please make sure to comment out `app.run` and instead use `serve`!

If this isn't done, the CSS setup will not work and the program will not run without the intended packages

## Configuration
The SQL Server will run locally as `flask-server.db`, if you want to change this then change the SQLALCHEMY_DATABASE_URI in the app config to the appropriate SQL Server.

Before running:
1. Change the email server details in the `email_sender.py` file on lines 8-12 and lines 504-508.
2. Change the Redis server in the `app.py` file on lines 37 and 38.
3. Lastly, I'd recommend changing your secret key to something different.

