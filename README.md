# My Implementation

## How to run

1. Firstly, please ensure that the `fake_profiles.zip` file is placed in the `/API/data/` directory such that the API will be able to extract and read from the contained `fake_profiles.json` file.

2. Pip3 install all the dependencies from `requirements.txt` and `requirements-dev.txt`.

3. Start the server using the following terminal command: `python3 manage.py runserver` to run in production environment or `python3 manage.py rundev` to run in development environment.

---

# Persona API Original Instructions

The Persona API is a fake RESTful API that delivers made up data on a few endpoints. The data sits within a zip file and needs to be decompressed only on deployment not when it sits in this repository. So you have to find a way to do that in an elegant manner.

## Must Haves

- Develop the server and endpoints mentioned below with a framework of your preference
- Think carefully about data storage and scalability. Determine any limitations of your server
- Write a few unit tests with good code coverage

The REST API uses the data provided and has the following endpoints:

- GET /search/{username} Searches the data for the specific username
- GET /people Returns all people with pagination
- DELETE /people/{username} Delete a person

We would like to see good practices regarding the REST API, project structure, code documentation and code organisation. Your server will need to be able to ingest new data and we are expecting to see good use of design patterns where needed and good security practices.

## Nice To Haves

- Nice to have would be to containerise your server so that it can deployed easily.
- A front-end that will allow users to search for a person and return back their information.

## Go The Extra Mile

Come up with some ideas to visualise the fake profile data on a front-end using a framework of your choice.
