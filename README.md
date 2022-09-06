# ESP8266 WiFi Car application

#### Video Demo: < https://youtu.be/C9AkDO3eui8 >

#### Description:
This is a application that allows the user to register an account then login using their login details. The main function of the application is to control a wifi car 
made using an node mcu 1. The application is a flask application and it communicates with the node mcu through web sockets. the application asks for the ip address that the node mcu is connected to and then it communicatesn with the node mcu via that address. 

My project consists of one big folder called project and within that folder there are 2 sub folders caled staic and templates, there are also python files namely app.py and helpers.py and a database file. In the static folder there are 2 files namely style.css this file contains all the styling of all html pages in this application and then there is script.js which contains the javascript responsible for the communication between the node mcu and our webpage and our keyboard.

The templates folder consists of nine html pages which are:
# apology.html: 
This file was inspired by cs50 finance and it contains an apology of our choosing that is rendered when ever the user does something outside the parameters of the application

# index.html
This file has the home page of our application where you contect to the node mcu and start controlling it. Users are required to login before they can access the home page.

# login.html
This file has the login page ,where the user puts their login details in order to access the home page and be able to use the application

# layout.html
This file contains the main layout of our application and other html pages acces the layout using jinja

# register.html
This is the page where users create their accounts and their details are added into the database.db file using SQL and python and they can be accesed when logging in

# code.html
This file contains the arduino code that the user copies and uploads into the arduino IDE then they get the ip address the node mcu will be connect to on the serial monitor of the arduino IDE. The arduino code is written in C language

# schematic.html
This file contains the picture of the schematic diagram on how the coonctions of the motors and the node mcu and th motor sheild are done

# home.html
this page just returns the index.html page.

In the templates folder there are also 3 images that are used in different pages of our application.

App.py and helpers.py contaian all the python that is responsible for the running or our flask application and its functionality. The folder with car final project stl files contains all the .stl files designed using fusion 360 and ready to be printed.


