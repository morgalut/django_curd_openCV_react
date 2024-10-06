# C:\Users\Mor\Desktop\django_curd\my_project\items\tests\pytest\conftest.py
import os
import django
from django.conf import settings

# Set the default settings module for Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'my_project.settings'
django.setup()
