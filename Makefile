install:
	pip install requirements.txt


run:
	DJANGO_SECRET_KEY=abc MAILGUN_API_KEY=dummykey DEFAULT_FROM_EMAIL=a@localhost RECIPIENTS=a@b.com,c@d.com python manage.py runserver

test:
	DJANGO_SECRET_KEY=abc MAILGUN_API_KEY=dummykey DEFAULT_FROM_EMAIL=a@localhost RECIPIENTS=a@b.com,c@d.com python manage.py test
