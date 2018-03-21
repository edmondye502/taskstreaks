from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Task

def index(request):
	task_list = Task.objects.order_by('create_date')[:5]
	context = {
		'task_list': task_list,
	}
	return render(request, 'tasks/index.html', context)



def detail(request, task_id):
	task = get_object_or_404(Task, pk=task_id)
	return render(request, 'tasks/detail.html', {'task': task})

def complete(request):
	try:
		selected_tasks = request.POST.getlist('tasks[]')
		completed_tasks = []
		for task_id in selected_tasks:
			completed_tasks.append(Task.objects.get(pk = task_id))
	except (KeyError, Task.DoesNotExist):
		# Redisplay the question voting form.
		return render(request, 'tasks/index.html', {
			'task_list': Task.objects.order_by('create_date')[:5],
			'error_message': "Error updating tasks. Please try again.",
		})
	else:
		for ct in completed_tasks:
			ct.completed =  True
			ct.save()
		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data. This prevents data from being posted twice if a
		# user hits the Back button.
		return HttpResponseRedirect(reverse('tasks:index'))