from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View

# Create your views here.

class KirrCBView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Something")