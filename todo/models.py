from django.db import models
import datetime
# Create your models here.
class todoitem(models.Model):
    contents= models.TextField()
    #date= models.DateTimeField()

    def __str__(self):
        return self.contents

 
