import csv

from django.core.management.base import BaseCommand

from charts.models import City, Fact, Plan, Year


class Command(BaseCommand):
  help = 'Load data from CSV file into the database'

  def handle(self, *args, **kwargs):
    with open('data/sales_data.csv', 'r', encoding='UTF-8') as file:
      reader = csv.DictReader(file)
      for row in reader:
        city, created = City.objects.get_or_create(name=row['city'])
        year_obj, created = Year.objects.get_or_create(city=city,
                                                       year=row['year'])
        if row['type'] == "План":
          Plan.objects.get_or_create(year=year_obj, amount=row['amount'])
        elif row['type'] == "Факт":
          Fact.objects.get_or_create(year=year_obj, amount=row['amount'])
