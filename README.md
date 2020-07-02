# Shoe Store

Use of the Django REST framework and a fresh Django server to create an API.

Use the [documentation on creating a custom management command](https://docs.djangoproject.com/en/3.0/howto/custom-management-commands/) to add a 'bootstrap_data' command for manage.py. This command will do the following things:

- Populate the ShoeType table with the following entries:

  - sneaker
  - boot
  - sandal
  - dress
  - other

- Populate the ShoeColor table with the following entries:
  - Red
  - Orange
  - Yellow
  - Green
  - Blue
  - Indigo
  - Violet
  - White
  - Black

## Installation

Use the package manager [poetry](https://python-poetry.org/) to start a virtual environment:

```bash
    poetry shell
```

Then, install all the dependencies required for this project:

```bash
    poetry install
```

Don't forget to run the respective migrations:

```bash
    python manage.py migrate
```

Before move on to run the server don't forget to populate a couple of tables with:

```bash
    python manage.py bootstrap_data
```

Finally, you are ready to run the server with

```bash
    python manage.py runserver
```

and check out the Shoe Store API built with Django in this [link](http://localhost:8000/api/shoe/).
