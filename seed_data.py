import os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
django.setup()


from django_seed import Seed
from stamp.models import Stamp, Theme
import random

seeder = Seed.seeder()
seeder.add_entity(Theme, 2000)
seeder.add_entity(Stamp, 1500)

inserted_pks = seeder.execute()