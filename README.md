# Django Settings Configuration

## Settings Folder Structure

The `settings` folder contains the following files:

- `common.py`
- `dev.example.py`
- `prod.example.py`
- `__init__.py`

## Initial Setup

1. In the `settings` folder, the `__init__.py` file should contain the following lines:

    ```python
    from config.settings.development import *
    # from config.settings.production import *
    ```

2. Create a file named `production.py` or `development.py` based on your environment.

3. Copy the content from `prod.example.py` or `dev.example.py` to the newly created file (`production.py` or `development.py`).

4. In the `__init__.py` file, uncomment the appropriate line that matches your environment:

    ```python
    # For development environment
    from config.settings.development import *
    
    # For production environment
    # from config.settings.production import *
    ```

5. Create `.env` file in root of the project, and add the content of `.template.env` file
    then set the value for the variables.


## Running the Project

To create the containers and run the Django web server, execute the following command:
The command below will also install requirements 
```sh
docker-compose up --build
```