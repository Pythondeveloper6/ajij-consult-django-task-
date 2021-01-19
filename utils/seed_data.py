# add the django settings module 
import os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
django.setup()

# import the djang_seed library & the project models
from django_seed import Seed
from stamp.models import Stamp, Theme
import random

# create a seeder 
seeder = Seed.seeder()

# seed the Theme & Stamp modules with row counts (Theme , row_count)
seeder.add_entity(Theme, 2000)
seeder.add_entity(Stamp, 1500)

# initiate the seed to seed data 
inserted_pks = seeder.execute()