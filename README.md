# Blog_Api

installs django_rest_framework , django-cors-headers

# Cors header set up

    add to installed app, corsheaders
    add to middle ware
    'corsheaders.middleware.CorsMiddleware', # new

heroku addons:create heroku-postgresql:hobby-dev - create db for heroku with cli

### Permission and Auth set up

    include

        'rest_framework.authtoken' to installed apps
        migrate after this is added and tokens will be added to db

    and  add this to rest framework in settings.py

    'DEFAULT_AUTHENTICATION_CLASSES': [ 'rest_framework.authentication.SessionAuthentication', 'rest_framework.authentication.TokenAuthentication', # new

],

pipenv install dj_rest_auth - handles the login/logout feature for django

add -> 'dj_rest_auth' to installed apps

sets up url that allows for login and logout using djrestauth
path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls'))

after this is set it up it gives /logout , /login, /password/reset urls once configured to the urls path

### allauth set up

pipenv install django-allauth

add to installed app settings

• django.contrib.sites
• allauth
• allauth.account
• allauth.socialaccount
• dj_rest_auth.registration
