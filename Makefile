run:
	python3 manage.py runserver 9000

migrate:
	python3 manage.py makemigrations && python3 manage.py migrate