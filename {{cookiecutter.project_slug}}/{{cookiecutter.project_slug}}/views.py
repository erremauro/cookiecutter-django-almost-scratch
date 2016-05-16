from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, '{{cookiecutter.project_slug}}/index.html')

def create(request, url_address):
	return HttpResponse("URL \"%s\" will be shorted" % url_address)
