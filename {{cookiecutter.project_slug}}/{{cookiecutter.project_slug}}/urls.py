from django.conf.urls import url, include
from {{cookiecutter.project_slug}} import views

app_name='{{cookiecutter.project_slug}}'
urlpatterns = [
	url(r'^$', views.index, name='index'),
]
