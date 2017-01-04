Mailr
=====


A "microservice" API that accepts a file (at the moment hardcoded to jpg)
as a part of a POST request and subsequently sends that as an attachment
to an email address specified.

It is largely independent of a database (apart from the data needed for Django's
bookkeeping).


Configuring the project
=======================

The project is highly configurable since the decision is to go with this config
stored as environment variables.

The follwing environment variables need to be set (check `Makefile` for
example):

	- `DJANGO_SECRET_KEY` - a secret key that django uses in production
	- `MAILGUN_API_KEY` - the API key given by mailgun
	- `DEFAULT_FROM_EMAIL - the email address you want to show up
	- `RECIPIENTS` - a comma separated list of emails (no spaces)


Running the project locally
===========================

Create a virtualenv and activate it.

Then run:

```
make install
```

and then run

```
make run
```

Note: these commands must be run from the root of the project, that is, from the
same folder that `Makefile` is.


Running the tests
=================

```
make test
```
