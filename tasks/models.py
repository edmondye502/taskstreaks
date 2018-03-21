from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible  # only if you need to support Python 2
class Task(models.Model):
    task_text = models.CharField(max_length = 200)
    completed = models.BooleanField(default = False)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task_text

    def is_completed(self):
    	return self.completed