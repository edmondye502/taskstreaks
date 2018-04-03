from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic

from .models import Task

class IndexView(generic.ListView):
	template_name = 'tasks/index.html'
	context_object_name = 'task_list'

	def getTaskType(self):
		page_types = {'day': 'Daily', 'month': 'Monthly', 'year': 'Yearly', 'once': 'Once'}
		task_type = page_types[self.kwargs['task_type']] if 'task_type' in self.kwargs and self.kwargs['task_type'] in page_types else 'Daily'
		return task_type
	
	def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)	    
	    context['page_type'] = self.getTaskType()
	    return context

	def get_queryset(self):
		task_type = self.getTaskType()
		return Task.objects.filter(task_type=task_type, delete_flag=False, user=self.request.user).order_by('create_date')


class DetailView(generic.DetailView):
	model = Task
	template_name = 'tasks/detail.html'

	def get_queryset(self):
		return Task.objects.filter(delete_flag=False)

def complete(request):
	try:
		task_id = request.POST['task_id']
		task = Task.objects.get(pk = task_id)
	except (KeyError, Task.DoesNotExist):
		return JsonResponse({'status':'Fail'})
	else:
		task.completed = False if task.completed else True
		task.save()
		return JsonResponse({'status':'Success'})

def addTask(request):
	try:
		task_text = request.POST.get('new_task_text')
		task_completed = True if request.POST.get('new_task_completion') else False

		task_choices = {'Daily': Task.DAILY, 'Monthly': Task.MONTHLY, 'Yearly': Task.YEARLY, 'Once': Task.ONCE}
		task_type = task_choices[request.POST.get('task_type')] if task_choices[request.POST.get('task_type')] else Task.ONCE
		
		task = Task(task_text=task_text, completed=task_completed, task_type=task_type, user=request.user)
		task.save()

		task_choices_redirect = {'Daily': 'day', 'Monthly': 'month', 'Yearly': 'year', 'Once': 'once'}
		task_type_redirect = task_choices_redirect[request.POST.get('task_type')]

		return redirect('/tasks/'+ task_type_redirect)
	except Exception as e:
		return JsonResponse({'status':e})


def editTask(request):
	try:
		task_id = request.POST.get('task_id')
		edit_task_text = request.POST.get('task_text')

		print(task_id, edit_task_text)
		task = Task.objects.get(pk = task_id)
	except Exception as e:
		return JsonResponse({'status':e})
	else:
		task.task_text = edit_task_text
		task.save()
		return redirect('tasks:index')


def deleteTask(request):
	try:
		#verify it is logged in users task
		task_id = request.POST.get('task_id')
		task = Task.objects.get(pk = task_id)
	except Exception as e:
		return JsonResponse({'status':e})
	else:
		task.delete_flag = True
		task.save()
		return redirect('tasks:index')
