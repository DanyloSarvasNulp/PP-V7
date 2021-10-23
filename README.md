# labs

Provided you have pyenv and poetry on your pc do the following:

1. locate project directory
2. install dependencies by command
>>> poetry install
3. create virtual environment by typing:
>>> poetry shell
3. type 
>>> waitress-serve --port=8000 app:app
4. in web-browser write URL: 
>>> http://127.0.0.1:8000/api/v1/hello-world-7
5. to end process type:
>>> ctrl + c
