# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
	if "data" not in request.session:
		request.session['data']=""
	
	return render(request, "surveyapp/index.html")
	
def result(request):
	if request.method == "POST":

		name = request.POST['name']
		email = request.POST['email']
		location = request.POST['location']
		comments = request.POST['comments']
		context = {
			'name':name,
			'email':email,
			'location':location,
			'comments':comments
		}
		
		request.session['data']=context

		return redirect("/surveyapp/successpage")

def success(request):
	if "data" not in request.session:
		return redirect('/')
	context = request.session['data']
	return render(request, "surveyapp/success.html", context)