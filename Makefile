runserver:
	python manage.py runserver 0.0.0.0:8000

makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

shell:
	python manage.py shell

admin:
	python manage.py bloggycreatesuperuser

push:
	git push origin bola

add:
	git add .