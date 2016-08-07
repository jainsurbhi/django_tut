from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
        #return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    template_name = 'detail.html'
    model = Question

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultView(generic.DetailView):
    template_name = 'result.html'
    model = Question


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


# Create your views here.


# def index(request):
    # return HttpResponse("</h1>List</h1>")
    #instance = Question.objects.order_by('pub_date')[:5]
    # context = {
    #   "object_list": instance,
    #}
    # return render(request, "index.html", context)


# def detail(request, question_id):
    # return HttpResponse("</h1>List</h1>")
 #   question = get_object_or_404(Question, id=question_id)
  #  context = {

   #     "question": question,
    #}
    # return render(request, "detail.html", context)


# def result(request, question_id):
 #   question = get_object_or_404(Question, id=question_id)
  #  context = {
   #     'question': question,
    #}
    # return render(request, "result.html", context)
