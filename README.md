data-engineering-task
=====================

This repository provides a data engineering task suitable for completion in one hour.

Important notes
---------------

Please do not spend more than one hour on this task. This does not include preparation time.

Start by forking the repository and then cloning it to your local machine (so that you can work freely on your changes to the base code).

Be sure to read the following notes in full before beginning the task.

Prerequisites for this task
---------------------------

First, some requirements:

- you should be able to run Python 3 (exercise tested on version 3.8, but should work for other minor versions)
- you should ensure the following libraries are installed in your environment
  1. `Flask`
  2. `sqlalchemy`
  3. `pytest`

You should feel free to swap these out for the alternative libaries of your choice, but will need to fix the example application and unit test.

How to get the skeleton app running
-----------------------------------

We provide the skeleton of a Flask app as the basis of this task. There are many ways to run such apps, but for development purposes the following should be sufficient:

1. set the `FLASK_APP` environment variable to the path to the app, e.g. from the terminal `export FLASK_APP=src/app.py` (`set FLASK_APP=src/app.py` on Windows)
2. execute `flask run`

This will start the Flask development server on port 5000 by default.

This means the application is ready to receive HTTP requests, e.g. using

- any web browser: visiting `http://127.0.0.1:5000/` in your browser will show the test response, proving the app is working
- command line tools such as curl
- the Python `requests` library

If you have trouble at this point, please contact the task assessor.

The task
--------

**Please read these instructions carefully before proceeding**

Your task today is to extend the skeleton app to create a useful API for internal company use. This is intended to be an everyday task; the assessor will be looking for

- a working solution (runs locally) that matches the requirements - see below
- a demonstration of good coding practices
- some thought to be given to how this code might be deployed to production
- good communication skills

Your solution should be provided as a GitHub repository (your fork of the original repository) with all changes merged into the main branch.

The task should be completed in one hour - we want to see what you are able to achieve in that time. It is acceptable to exceed this time frame by a little, in which case please tell the assessor how long it actually took.

After completing the task, please ensure your solution is pushed to GitHub and that all changes are merged into the main branch.

Finally, you should contact the task assessor with a link to your solution and handover notes. The handover is an important part of the exercise: 

- if you did not have time for a complete solution, you should outline what work should be done next
- you should explain how to run your code and how you would go about deploying it to production
- you should explain how other teams can retrieve data from your API when it is deployed (valid requests, routes to hit, expected response format)
- include any other important notes (such as how long the exercise took).

Your handover can take the form of a README file in the repo if you wish, or can be emailed directly.

### Information about the skeleton app

The skeleton app currently has two routes, `/` and `/product/<ID>`. The first of these returns a simple response, indicating the service is available. The second is currently incomplete. A request to `http://127.0.0.1:5000/product/x` will return some data, but it is  is just an example: the response is neither actually specific to the product with ID `x`, nor in the format this exercise requires.

A database for development purposes has been provided in `/data/musical_instrument_reviews.sqlite`. It contains some reviews left on Amazon for musical instruments. The skeleton app assumes you will be connecting to this SQLite database, so it is not suitable for a production environment.

The structure of the repo is as follows:

```
data-engineering-task
├── .gitignore
├── LICENSE
├── README.md
├── data
│   └── musical_instrument_reviews.sqlite
├── src
│   ├── __init__.py
│   └── app.py
└── tests
    ├── __init__.py
    └── test_app.py
```

### App requirements

We want to create a production-ready API that can return some simple information regarding the reviews for a specific product or made by a particular user.

**If any of the following requirements are unclear, please contact the task assessor for clarification.**

1. your app should be able to connect to a PostgreSQL database in production (with the same schema as the provided SQLite database)
2. your app should have a route that allows end-users to retrieve aggregated review information for a product with a particular ID
3. your app should have a route that allows end-users to retrieve aggregated review information from a user with a particular ID
4. both routes should allow the end-user to _optionally_ filter by review date
5. your app should follow coding best-practices (at a minimum, it should be well-documented, preferably with unit tests)
6. you should take steps to make the app easy to deploy to production (think about how you will manage dependencies and any required environment variables - you may use any tools/libraries you like), although a complete pipeline is not necessary and assessment will be done in a development environment

Submitting a solution
---------------------

After completing the task, please ensure your solution is pushed to GitHub and that all changes are merged into the main branch.

You should then contact the task assessor with a link to your solution and handover notes (see above for guidance).

# How to run the db!
---------------------
$ export FLASK_APP=src/app.py
# Intitalize the table in our database
$ flask db init
$ flask db migate
$ flask db upgrade
