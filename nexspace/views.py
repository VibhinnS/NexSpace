from django.http import HttpResponse
from questions.models import Question
from django.template.loader import render_to_string
from django.shortcuts import render

def landing_page(request):
    return render(request, 'landing_page.html')

def question_list(request):
    question_obj = Question.objects.get(id=1)
    questions = Question.objects.all()
    context = {
        "my_list": questions,
        "title": question_obj.title,
        "content": question_obj.content
    }
    HTML_STRING = render_to_string("questions.html", context=context)
    return HttpResponse(HTML_STRING)
