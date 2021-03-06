# Django Learning Log

This Django project was made using the contents of the book *Python Crash Course: A Hands-On, Project-Based Introduction to Programming (2015) by Eric Matthes*.

## Installation

1. Clone this repo

```bash
git clone git@github.com:yesnik/django_learning_log.git
```

2. Create environment `myenv`

```bash
cd django_learning_log
virtualenv myenv
```

3. Activate environment `myenv`

```bash
python myenv/bin/activate
```

4. Install requirements

```bash
pip install -r requirements.txt
```

5. Apply migrations

```bash
python manage.py migrate
```

6. Run development server

```bash
python manage.py runserver
```

7. Visit URL: http://127.0.0.1:8000/
