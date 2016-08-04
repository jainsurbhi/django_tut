from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from .models import Choice, Question

# Create your views here.


def index(request):
    # return HttpResponse("</h1>List</h1>")
    instance = Question.objects.order_by('pub_date')[:5]
    context = {
        "object_list": instance,
    }
    return render(request, "index.html", context)


def detail(request, question_id):
    # return HttpResponse("</h1>List</h1>")
    question = get_object_or_404(Question, id=question_id)
    context = {

        "question": question,
    }
    return render(request, "detail.html", context)


def result(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    context = {
        'question': question,
    }
    return render(request, "result.html", context)


def vote(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    try:
        selected_choice = question.choice_set.get(id=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context = {
            'question': question,
            'error_message': "You did not selet a choice",
        }
        return render(request, 'detail.html', context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:result', args=(question.id,)))
