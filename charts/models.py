from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Year(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.city.name} - {self.year}"
    
    class Meta:
        unique_together = ('city', 'year')

class Plan(models.Model):
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.year} - Plan: {self.amount}"
    
class Fact(models.Model):
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.year} - Fact: {self.amount}"