import json
from authlib.integrations.django_client import OAuth
from django.conf import settings
from django.shortcuts import redirect, render, redirect
from django.urls import reverse
from urllib.parse import quote_plus, urlencode
import requests
from django.http import HttpResponse
from questions.models import Question
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login

oauth = OAuth()

oauth.register(
    "auth0",
    client_id=settings.AUTH0_CLIENT_ID,
    client_secret=settings.AUTH0_CLIENT_SECRET,
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f"https://{settings.AUTH0_DOMAIN}/.well-known/openid-configuration",
)

def landing_page(request):
    return render(request, 'landing_page.html')

def callback(request):
    token = oauth.auth0.authorize_access_token(request)
    request.session["user"] = token
    return redirect(request.build_absolute_uri(reverse("landing_page")))


def login(request):
    return oauth.auth0.authorize_redirect(
        request, request.build_absolute_uri(reverse("callback"))
    )


def logout(request):
    request.session.clear()

    return redirect(
        f"https://{settings.AUTH0_DOMAIN}/v2/logout?"
        + urlencode(
            {
                "returnTo": request.build_absolute_uri(reverse("index")),
                "client_id": settings.AUTH0_CLIENT_ID,
            },
            quote_via=quote_plus,
        ),
    )

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
