from django.http import HttpResponse
# from django.template import Context, loader
from django.shortcuts import get_object_or_404, render

from polls.models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date') [:5]
    #output = ', '.join([p.question for p in latest_poll_list])
    #template = loader.get_template('polls/index.html')
    #context = Context ({
    #    'latest_poll_list': latest_poll_list,
    #})
    context = {'latest_question_list': latest_question_list}
    #return HttpResponse(template.render(context))
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    return HttpResponse("You're looking at the results of poll %s" % question_id)
def vote(request, question_id):
    return HttpResponse("You're voting on poll %s." % question_id)
