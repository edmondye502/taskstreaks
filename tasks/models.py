from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now

@python_2_unicode_compatible  # only if you need to support Python 2
class Task(models.Model):
	DAILY = 'Daily'
	MONTHLY = 'Monthly'
	YEARLY = 'Yearly'
	ONCE = 'Once'
	TASK_TYPES = ((DAILY, 'Daily'), (MONTHLY, 'Monthly'), (YEARLY, 'Yearly'), (ONCE, 'Once'))

	task_text = models.CharField(max_length = 200)
	task_type = models.CharField(max_length = 10, choices = TASK_TYPES, default = DAILY)
	completed = models.BooleanField(default = False)
	create_date = models.DateTimeField(default=now)

	def __str__(self):
		return self.task_text

	def is_completed(self):
		return self.completed