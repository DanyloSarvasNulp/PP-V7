# labs

Provided you have pyenv and poetry on your pc do the following:

1. locate project directory
2. create virtual environment by typing:
>>> poetry shell
3. install dependencies by command
>>> poetry install

lab-4

1. type 
>>> waitress-serve --port=8000 app:app
2. in web-browser write URL: 
>>> http://127.0.0.1:8000/api/v1/hello-world-7

lab-6

1. create revision
>>> alembic revision -m "add models" --autogenerate
2. upgrade head
>>> alembic upgrade head