from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Task

class IndexView(generic.ListView):
    template_name = 'tasks/index.html'
    context_object_name = 'task_list'

    def get_queryset(self):
        return Task.objects.filter(delete_flag=False).order_by('create_date')

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
		task_text = request.POST['new_task_text']
		task_completed = True if request.POST['new_task_completion'] == 'true' else False

		task = Task(task_text=task_text, completed=task_completed)
		task.save()

		return JsonResponse({'status':'Success'})
	except:
		return JsonResponse({'status':'Fail'})

def editTask(request):
	try:
		task_id = request.POST['task_id']
		edit_task_text = request.POST['task_text']
		task = Task.objects.get(pk = task_id)
	except (KeyError, Task.DoesNotExist):
		return JsonResponse({'status':'Fail'})
	else:
		task.task_text = edit_task_text
		task.save()
		return JsonResponse({'status':'Success'})

def deleteTask(request):
	try:
		task_id = request.POST['task_id']
		task = Task.objects.get(pk = task_id)
	except (KeyError, Task.DoesNotExist):
		return JsonResponse({'status':'Fail'})
	else:
		task.delete_flag = True
		task.save()
		return JsonResponse({'status':'Success'})