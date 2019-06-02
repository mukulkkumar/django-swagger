# install django-rest-swagger
pip install django-rest-swagger

# Add 'rest_framework_swagger' to INSTALLED_APPS in Django settings.
INSTALLED_APPS = [
    ...
    'rest_framework_swagger',
    ...
]

# use the get_swagger_view
from django.urls import re_path
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='API')

urlpatterns = [
    re_path('^$', schema_view)
]
