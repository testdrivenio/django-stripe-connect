# Setting up Stripe Connect with Django

## Want to learn how to build this?

Check out the [post](https://testdriven.io/blog/setting-up-stripe-connect-with-django/).

## Want to use this project?

1. Fork/Clone

1. Create a virtual environment and install the dependencies:

    ```sh
    $ pipenv shell
    $ pipenv install
    ```

1. Apply the migrations, create a superuser, and add the fixtures to the DB:

    ```sh
    $ python manage.py migrate
    $ python manage.py createsuperuser
    $ python manage.py loaddata fixtures/users.json
    $ python manage.py loaddata fixtures/courses.json
    ```

1. Add your Stripe test secret and test publishable keys along with your Connect client id to the bottom of the *settings.py* file:

    ```python
    STRIPE_PUBLISHABLE_KEY = '<your test publishable key here>'
    STRIPE_SECRET_KEY = '<your test secret key here>'
    STRIPE_CONNECT_CLIENT_ID = '<your test connect client id here>'
    ```

1. Run the server:

    ```sh
    $ python manage.py runserver
    ```
