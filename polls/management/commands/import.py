from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
import csv

class Command(BaseCommand):
    help = 'Import users from a CSV file: user,email,password'

    def add_arguments(self, parser):
        parser.add_argument('csvfile', nargs='+', type=str)

    def handle(self, *args, **options):
        for csvfile in options['csvfile']:
            with open(csvfile, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    user = User.objects.create_user(row[0], row[1], row[2])
                    user.save()    
