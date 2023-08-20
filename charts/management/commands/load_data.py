import csv

from django.core.management.base import BaseCommand

from charts.models import City, Sales


class Command(BaseCommand):
  help = 'Load data from CSV file into the database'

  def handle(self, *args, **kwargs):
      with open('data/sales_data.csv', 'r', encoding='UTF-8') as file:
          reader = csv.DictReader(file)
          for row in reader:
              city, created = City.objects.get_or_create(name=row['city'])
              Sales.objects.get_or_create(
                  city=city,
                  year=row['year'],
                  plan=row['plan_amount'],
                  fact=row['fact_amount']
              )

