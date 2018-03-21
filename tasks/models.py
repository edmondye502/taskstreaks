from django.db import models


class Tasks(models.Model):
    tasks_text = models.CharField(max_length = 200)
    completed = models.BooleanField(default = 'false')
    create_date = models.DateTimeField()

