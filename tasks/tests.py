import datetime

from django.utils import timezone
from django.test import TestCase
from django.urls import reverse

from .models import Task

class TaskDetailViewTests(TestCase):
	def test_deleted_task(self):
		"""
		The detail view of a task that has been deleted 
		returns a 404 not found.
		"""
		deleted_task = Task.objects.create(task_text='Test Delete.', delete_flag=True)
		url = reverse('tasks:detail', args=(deleted_task.id,))
		response = self.client.get(url)
		self.assertEqual(response.status_code, 404)
