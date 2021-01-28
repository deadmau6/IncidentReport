# Incident Report

Fetch Emergency incidents with additional data.

## Table of Contents:

 * [**TODOs**](#todos)
 * [**Setup for Ubuntu**](#setup-for-ubuntu)
 * [**Running Integration Tests**](#running-integration-tests)
 * [**Improvements**](#improvements)
 * [**Summary**](#summary)

### TODOs {#todos}

 - [X] Download and Setup environment
 - [X] Create Weather API Interface
 - [X] Create Incident Report Interface
 - [X] Create Endpoints for API requests
 - [X] Document installation process
 - [X] Create Integration tests for API
 - [ ] Security considerations
 - [X] Data storage considerations
 - [X] Possible Improvements

### Setup for Ubuntu {#setup-for-ubuntu}

These are the installation instructions for Ubuntu 20.04 but it could work for other distributions either way **Python3.6+ is required**.

There are _two_ ways to install and run the application. **One** is to install and run with a virtual environment like **pipenv** _(Recommended)_. **Option Two**, is to install everything with **pip** and then run everything from the command line normally.

#### Prerequiste:

 * [**Python3.6+**](https://realpython.com/installing-python/)
 * [**pip installation**](https://linuxize.com/post/how-to-install-pip-on-ubuntu-20.04/)
 * [**Pipenv installation**](https://pipenv.pypa.io/en/latest/install/#pragmatic-installation-of-pipenv) _(optional, but **recommended**)_
 * [**MongoDB Community Edition installation**](https://docs.mongodb.com/manual/installation/)

#### Installing:

_**With Pipenv**:_

 1. In `./Pipfile`, under the `[requires]` header, check to make sure that the `python_version` is the same as your local version (your local python version: `python3 --version`).

 2. If the `python_version` is not the same and you need to change it then that is fine but you also should delete `./Pipfile.lock`, also if there are any issues with the Lock file it might be usefull to delete the lock then try installing again.

 3. Then simply run `pipenv install`.

_**Without Pipenv:**_

 1. Simply install with `pip install -r requirements.txt`.

#### Running:

 1. If you have `pipenv` then you can start your shell with `pipenv shell`, _**also**_ if you have `pipenv` then you can run the commands normally but just pre-append `pipenv run` _(i.e. `pipenv run uvicorn main:app`)_.

 2. Make sure that **mongodb is running locally** and if you want to setup the DB with some data you can use the `init_db.py` tool. By default it loads data from `./tests/data` into the DB. _But_ you can easily add more json reports by running `python3 init_db.py -f /path/to/report.json`.
 
 3. To start the API simply run `uvicorn main:app`. _(you can learn more about `uvicorn`  and `FastAPI` from the "Additional Dependencies information" below)_

 4. Next you can make requests to the localhost server: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

 5. And you can view the endpoint documentation (SwaggerUI) here: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) or the ReDoc version: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

#### Additional Dependencies information:

 * [**FastAPI**](https://fastapi.tiangolo.com/)
 * [**Meteostat**](https://dev.meteostat.net/)
 * [**Pipenv**](https://pipenv.pypa.io/en/latest/) _(optional, but **recommended**)_

### Running Integration Tests {#running-integration-tests}

To run the integration tests simply run `pytest` from the main directory _(or if you have pipenv then run `pipenv run pytest`)_.

### Improvements {#improvements}

Here are some things I would have done if I had more time:

 * Clean up the code base and add more descriptions for each method/class.
 * Expand and improve the Data validation models. Both `Query` and `Field` have `description` attributes, I probably would have started there.
 * I would improve my data storage and data model. I think I would store the weather data with the incident reports or if I was using SQL I would've created a table for the weather objects that join to the incident reports.
 * Of course I would have expanded on my tests and I would've added unit test sweeps as well.
 * Finally I would have added security features like Authorization Tokens.


### Summary {#summary}

Time spent:
 * `8am - 9am`: researching libraries and reading documentation.
 * `9am - 10am`: Installing and setting up the env. Implenting the weather service. Adding documentation.
 * `10am - 12pm`: Setting up a database and getting the Incident service to query the DB for resutls.
 * `2pm - 4pm`: Connecting the API components with the Weather and incident services.
 * `7pm - 8pm`: Integration tests and any remaining docs.