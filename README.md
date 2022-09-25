# my-django-todo-api
REST API designed in Django framework to perform CRUD operations for TODO application

Set-Up Virtual Environment

$mkdir ToDo-API

Now move in that directory by running the following command.

$cd ToDo-API

Install the virtualenv package

$pip install virtualenv

Now, within the directory, create a Python virtual environment by typing:
$virtualenv myenv

Activate the virtual environment
$source myenv/bin/activate

Our prompt should change to indicate that we are now operating within a Python virtual environment. It will look something like this:

(myenv) C:\<path to dirctory\>

We can install Django by typing:
$pip install django

Creating the project
$django-admin startproject <project-name>


ToDo-API
     |- todo-api
             |- manage.py
             |- todo-api/*
     |- myenv
Open this directory ToDo-API into your favorite IDE/Editor, for me, I open it with vs code.

After opening, switch to command prompt and make sure it works. Test run the Django server:
$python manage.py runserver

![image](https://user-images.githubusercontent.com/74610603/192144061-3277e210-5eeb-4d07-b44a-1bfec1cb85f9.png)

Start the app
$python manage.py startapp <app-name>


After running the above command you will see the directory structure something like this:

ToDo-API
     |- todo-api/*
     |- myenv/*
     |- api/*
     


2.3 Migrate the database
$python manage.py makemigrations
$python manage.py migrate

2.4 Create Super User

$python manage.py createsuperuser

Username : 
Email address: 
Password: 
Password (again): 
Superuser created successfully.

to verify it, start-up the Django development server, and navigate to localhost:8000/admin
$python manage.py runserver









