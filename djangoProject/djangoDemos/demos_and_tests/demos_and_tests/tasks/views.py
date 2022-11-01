from django.http import HttpResponse
from django.shortcuts import render

from demos_and_tests.tasks.models import Task


# Create your views here.
def index(request):
    tasks_list = Task.objects.all()
    # output = '; '.join(f"{t.task_title}: {t.task_text}"
    #                    for t in tasks_list)
    # if not output:
    #     output = "There are no created tasks!"
    #
    # return HttpResponse(output)
    context = {'tasks_list': tasks_list, 'nums': 12}
    return render(request, 'task/index.html', context)
