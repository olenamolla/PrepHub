from django.db import models

# Create your models here.

# Each model class is a table in DB
# Each filed is a column in that table
class Problem(models.Model):
    title = models.CharField(max_length=200)
    difficulty = models.CharField(max_length=20)
    topic = models.CharField(max_length=100)
    notes = models.TextField(blank=True)
    solved_date = models.DateTimeField()