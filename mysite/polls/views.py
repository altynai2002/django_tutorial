from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.urls import reverse

from .models import Question, Choice



def index(request):
    question_list =  Question.objects.all()
    context = {'questions': question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # print(request.POST)
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:    
    #     raise Http404('Question does not exist')
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
    
def vote(request, question_id):
    
    question = get_object_or_404(Question, pk=question_id)
    try:
    # print(request.POST['choice'])
        selected_choice = question.choice_set.get(pk=request.POST['choice']) # вытащит вариант ответа
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {\
            'question':question,
            'error_message': 'You did not select a choice'
            })

    selected_choice.voice += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question':question})