'''
Django command to wait for the database to be available
'''
import time

from django.core.management.base import BaseCommand
from django.db.utils import OperationalError
from psycopg2 import OperationalError as pysycopg2_error


class Command(BaseCommand):
    '''Command to wait for the database to be available'''

    def handle(self, *args, **options):
        '''Entry point for command'''
        self.stdout.write('Waiting for database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (pysycopg2_error, OperationalError):
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
