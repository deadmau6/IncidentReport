# Incident Report

Fetch Emergency incidents with additional data.

## Table of Contents:

 * [**TODOs**](#todos)
 * [**Setup for Ubuntu**](#setup-for-ubuntu)
 * [**Running Integration Tests**](#running-integration-tests)
 * [**Improvements**](#improvements)
 * [**Summary**](#summary)

### TODOs {#todos}

 - [ ] Download and Setup environment
 - [ ] Create Weather API Interface
 - [ ] Create Incident Report Interface
 - [ ] Create Endpoints for API requests
 - [ ] Document installation process
 - [ ] Create Integration tests for API
 - [ ] Security considerations
 - [ ] Data storage considerations
 - [ ] Possible Improvements

### Setup for Ubuntu {#setup-for-ubuntu}

These are the installation instructions for Ubuntu 20.04 but it could work for other distributions either way **Python3.6+ is required**.

There are _two_ ways to install and run the application. **One** is to install and run with a virtual environment like **pipenv** _(Recommended)_. **Option Two**, is to install everything with **pip** and then run everything from the command line normally.

#### Prerequiste:

 * [**Python3.6+**](https://realpython.com/installing-python/)
 * [**pip installation**](https://linuxize.com/post/how-to-install-pip-on-ubuntu-20.04/)
 * [**Pipenv installation**](https://pipenv.pypa.io/en/latest/install/#pragmatic-installation-of-pipenv) _(optional, but **recommended**)_

#### Installing:

_**With Pipenv**:_

 1. In `./Pipfile`, under the `[requires]` header, check to make sure that the `python_version` is the same as your local version (your local python version: `python3 --version`).

 2. If the `python_version` is not the same and you need to change it then that is fine but you also should delete `./Pipfile.lock`, also if there are any issues with the Lock file it might be usefull to delete the lock then try installing again.

 3. Then simply run `pipenv install`.

_**Without Pipenv:**_

 1. Simply install with `pip install -r requirements.txt`.

#### Running:

 1. If you have `pipenv` then you can start your shell with `pipenv shell`, _**also**_ if you have `pipenv` then you can run the commands normally but just pre-append `pipenv run` _(i.e. `pipenv run uvicorn main:app`)_.
 
 2. To start the API simply run `uvicorn main:app`. _(you can learn more about `uvicorn`  and `FastAPI` from the "Additional Dependencies information" below)_

 3. Next you can make requests to the localhost server: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

 4. And you can view the endpoint documentation (SwaggerUI) here: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) or the ReDoc version: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

#### Additional Dependencies information:

 * [**FastAPI**](https://fastapi.tiangolo.com/)
 * [**Meteostat**](https://dev.meteostat.net/)
 * [**Pipenv**](https://pipenv.pypa.io/en/latest/) _(optional, but **recommended**)_

### Running Integration Tests {#running-integration-tests}

blank

### Improvements {#improvements}

blank

### Summary {#summary}

blank