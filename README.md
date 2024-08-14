# Django Settings Configuration

## Settings Folder Structure

The `settings` folder contains the following files:

- `common.py`
- `dev.example.py`
- `prod.example.py`
- `__init__.py`

## Initial Setup

1. Create a file named `production.py` or `development.py` based on your environment
2. Copy the content from `prod.example.py` or `dev.example.py` to the newly created file (`production.py` or `development.py`).
3. Create `.env` file in root of the project, and add the content of `.template.env` file then set the value for the variables.
4. Make sure you have set `ENVIRONMENT` value as your file name you have created at `1.` 


## Running the Project

To create the containers and run the Django web server, execute the following command:
The command below will also install requirements 

1. It will run the project without nginx, it is designed to run development
```sh
docker-compose -f docker-compose-dev.yml up --build
```

2. It will run the project with nginx, it is designed to run production set up. it will take care of ssl, static and media files.
```sh
docker-compose -f docker-compose.yml up --build
```
