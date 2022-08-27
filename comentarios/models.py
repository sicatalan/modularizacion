from django.db import models

class comments(models.Model): #this creates a table with the name comments

    name = models.CharField(max_length=255, null = False)
    score = models.IntegerField(default=3)
    comment = models.TextField(max_length=100, null=True)
    date = models.DateField(null=True)
    signature = models.CharField(max_length=100, default="Firma")

    def __str__(self):
        return self.name

