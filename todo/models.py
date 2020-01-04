from django.db import models

# Create your models here.
class todoitem(models.Model):
    contents= models.TextField()

    def __str__(self):
        return self.contents
