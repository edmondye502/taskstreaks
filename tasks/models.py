from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now
from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver

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
	delete_flag = models.BooleanField(default = False)
	create_date = models.DateTimeField(default=now)
	user = models.ForeignKey(User, default=1)

	def __str__(self):
		return self.task_text

	def is_completed(self):
		return self.completed


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
