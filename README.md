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
> 
> alembic revision -m "add models" --autogenerate

2. upgrade head

> alembic upgrade head

lab-7

User requests:
> POST user
>
>> curl -X POST -H "Content-Type:application/json" --data-binary "{\"username\": \"Pax\", \"password\": \"abcdefg\"}" http://localhost:5000/user
>
> GET user
>
>> curl -X GET -u Pax:abcdefg http://localhost:5000/user
>
> PUT user
>
>> curl -X PUT -u Pax:abcdefg -H "Content-Type:application/json" --data-binary "{\"first_name\": \"Ivan\"}" http://localhost:5000/user
>
> DELETE user
>
>> curl -X DELETE -u Pax:abcdefg http://localhost:5000/user


Auditorium requests:
> POST auditorium
> 
>> curl -X POST -H "Content-Type:application/json" --data-binary "{\"max_people_count\": \"48\", \"auditorium_num\": \"10\"}" http://localhost:5000/auditorium
>
> GET all auditoriums
> 
>> curl -X GET http://localhost:5000/auditorium
>
> GET auditorium by num
> 
>> curl -X GET http://localhost:5000/auditorium/10
>
> PUT auditorium
>
>> curl -X PUT -H "Content-Type:application/json" --data-binary "{\"max_people_count\": \"100\", \"auditorium_num\": \"10\"}" http://localhost:5000/auditorium/1
>
> DELETE auditorium by num
>
>> curl -X DELETE http://localhost:5000/auditorium/10

Access requests:
> POST access
> 
>> curl -X POST -u Pax:abcdefg -H "Content-Type:application/json" --data-binary "{\"auditorium_num\": \"1\", \"username\": \"Pax\", \"start\": \"2021-01-01 1:00:00\", \"end\": \"2021-01-01 3:00:00\"}" http://localhost:5000/access
> 
>> curl -X POST -H "Content-Type:application/json" --data-binary "{\"auditorium_id\": \"1\", \"user_id\": \"1\", \"start\": \"2021-01-01 2:00:00\", \"end\": \"2021-01-01 4:00:00\"}" http://localhost:5000/access
> 
> GET all accesses
> 
>> curl -X GET http://localhost:5000/access
>
> GET access by ids
> 
>> curl -X GET http://localhost:5000/access/2,2
> 
> DELETE access
> 
>> curl -X DELETE -u Pax:abcdefg -H "Content-Type:application/json" --data-binary "{\"auditorium_num\": \"10\"}" http://localhost:5000/access

lab-9

Testing:

> python -m unittest discover -s tests_unittest -p "*_test.py"
> 
> coverage run -m --source=DataBase,tests_unittest unittest discover -s tests_unittest -p "*_test.py" && coverage report
> 
> 
> coverage run -m app --source=tests_unittest,DataBase,DataBase/Blueprint unittest discover -s tests_uest -p "*_test.py" && coverage report
> 
> coverage report -m
> 
> coverage run --source tests_unittest -m unittest discover && coverage report
