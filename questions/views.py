from django.shortcuts import render
from .models import Question
# Create your views here.
def question_detail_view(request, id=None):
    quesion_obj = None
    if id is not None:
        quesion_obj = Question.objects.get(id=id)
    context = {
        "object": quesion_obj,
    }
    
    return render(request, "questions/detail.html", context=context)
