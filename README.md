# labs

Provided you have pyenv and poetry on your pc do the following:

1. locate project directory
2. create virtual environment by typing:
> poetry shell
3. install dependencies by command
> poetry install

lab-4

1. type 
> waitress-serve --port=8000 app:app
2. in web-browser write URL: 
> http://127.0.0.1:8000/api/v1/hello-world-7

lab-6
1. create revision
> alembic stamp head
> alembic revision -m "add models" --autogenerate
2. upgrade head
> alembic upgrade head

lab-7

User requests:
>POST user
>
>>curl -X POST -H "Content-Type:application/json" --data-binary "{\"username\": \"Pax\"}" http://localhost:5000/user
> 
>>curl -X POST -H "Content-Type:application/json" --data-binary "{\"username\": \"the\", \"first_name\": \"Max\"}" http://localhost:5000/user
>
>GET user by username
> 
>>curl -X GET http://localhost:5000/user/Pax
>
>GET user by id
> 
>>curl -X GET http://localhost:5000/user/1
> 
>PUT user
> 
>>curl -X PUT -H "Content-Type:application/json" --data-binary "{\"first_name\": \"NewName\"}" http://localhost:5000/user/17
>
>DELETE user by username
> 
>>curl -X DELETE http://localhost:5000/user/17

Auditorium requests:
>POST auditorium
>
>>curl -X POST -H "Content-Type:application/json" --data-binary "{\"username\": \"Pax\"}" http://localhost:5000/auditorium
> 
>>curl -X POST -H "Content-Type:application/json" --data-binary "{\"username\": \"the\", \"first_name\": \"Max\"}" http://localhost:5000/auditorium
>
>GET user by username
> 
>>curl -X GET http://localhost:5000/auditorium/Pax
>
>PUT user
> 
>>curl -X PUT -H "Content-Type:application/json" --data-binary "{\"first_name\": \"NewName\"}" http://localhost:5000/auditorium/17
>
>DELETE user by username
> 
>>curl -X DELETE http://localhost:5000/auditorium/17