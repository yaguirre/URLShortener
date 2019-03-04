from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View

# Create your views here.


def index(request):
    return HttpResponse("Hello, World!. You are at the polls index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." %question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response %question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." %question_id)

'''
class KirrCBView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Something")
'''