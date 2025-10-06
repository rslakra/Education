# Posts

---

The ```posts``` contains both an internal and external web services of the project.



## Project Structure
```
    /
    ├── <module>                    # The module service
    ├── Posts                       # The posts service
    │    ├── ews                    # An external web-service
    │    ├── iws                    # An internal web-service
    │    ├── .env                   # The .env file
    │    ├── .gitignore             # The .gitignore file
    │    ├── .pylintrc              # The .pylintrc file
    │    ├── README.md              # Instructions and helpful links
    │    ├── robots.txt             # tells which URLs the search engine crawlers can access on your site
    │    ├── robots.txt             # tells which URLs the search engine crawlers can access on your site
    │    ├── runEWSApp.sh           # An EWS run script
    │    └── runIWSApp.sh           # An IWS run script
    └── <module>
```

## Local Development

### Check python settings
```shell
python3 --version
python3 -m pip --version
python3 -m ensurepip --default-pip
```

### Setup a virtual environment
```
python3 -m pip install virtualenv
python3 -m venv venv
source deactivate
source venv/bin/activate
```

### Upgrade PIP Requirements (Dependencies)
```shell
pip install --upgrade pip
```

### Configuration Setup

- Create or update local .env configuration file.

```shell
touch .env
HOST = 127.0.0.1
PORT = 8080
DEBUG = True
DEFAULT_POOL_SIZE = 1
RDS_POOL_SIZE = 1
```

**By default**, Flask will run the application on **port 5000**.

## EWS & IWS Services Instructions
- [EWS Application](./ews/README.md)
- [IWS Application](./iws/README.md)

### Build Service
```shell
python3 -m build
```

### Save Requirements (Dependencies)
```shell
pip freeze > requirements.txt
```

## Unit Tests
```shell
python -m unittest discover -s ./tests -p "test_*.py"
```

# Reference

- [Gunicorn - WSGI server](https://docs.gunicorn.org/en/latest/index.html)
- [Python Packaging User Guide](https://packaging.python.org/en/latest/)

# Author
- Rohtash Lakra