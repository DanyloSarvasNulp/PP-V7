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
> POST user
>
>> curl -X POST -H "Content-Type:application/json" --data-binary "{\"username\": \"Pax\"}" http://localhost:5000/user
>
>> curl -X POST -H "Content-Type:application/json" --data-binary "{\"username\": \"theMax0n\", \"first_name\": \"Max\"}" http://localhost:5000/user
>
> GET all users
>
>> curl -X GET http://localhost:5000/user
>
> GET user by username
>
>> curl -X GET http://localhost:5000/user/theMax0n
>
> GET user by id
>
>> curl -X GET http://localhost:5000/user/1
>
> PUT user
>
>> curl -X PUT -H "Content-Type:application/json" --data-binary "{\"first_name\": \"Ivan\"}" http://localhost:5000/user/2
>
> DELETE user by id
>
>> curl -X DELETE http://localhost:5000/user/1

Auditorium requests:
> POST auditorium
>
>> curl -X POST -H "Content-Type:application/json" --data-binary "{\"max_people_count\": \"48\"}" http://localhost:5000/auditorium
>
>> curl -X POST -H "Content-Type:application/json" --data-binary "{\"max_people_count\": \"48\", \"auditorium_num\": \"10\"}" http://localhost:5000/auditorium
>
> GET all auditoriums
> 
>> curl -X GET http://localhost:5000/auditorium
>
> GET auditorium by id
> 
>> curl -X GET http://localhost:5000/auditorium/2
>
> PUT auditorium
>
>> curl -X PUT -H "Content-Type:application/json" --data-binary "{\"max_people_count\": \"100\", \"auditorium_num\": \"3\"}" http://localhost:5000/auditorium/1
>
> DELETE auditorium by id
>
>> curl -X DELETE http://localhost:5000/auditorium/1

Access requests:
> POST access
> 
>> curl -X POST -H "Content-Type:application/json" --data-binary "{\"auditorium_id\": \"2\", \"user_id\": \"2\"}" http://localhost:5000/access
> 
>> curl -X POST -H "Content-Type:application/json" --data-binary "{\"auditorium_id\": \"2\", \"user_id\": \"2\", \"start\": \"2021-04-28 11:15:00\", \"end\": \"2021-04-28 11:45:00\"}" http://localhost:5000/access
> 
> GET all accesses
> 
>> curl -X GET http://localhost:5000/access
>
> GET access by ids
> 
>> curl -X GET http://localhost:5000/access/2,2
> 
> DELETE access by ids
> 
>> curl -X DELETE http://localhost:5000/access/2,2