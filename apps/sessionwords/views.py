# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
	if 'words' not in request.session:
		print "TEST"
		request.session['words']=[]
	print request.session['words']
	context = {
		'words':request.session['words']
	}
	print request.session['words']
	
	return render(request, "sessionwords/index.html", context)
	
def addword(request):
	if request.method == "POST":
		
		if len(request.POST['text']) == 0:
			return redirect("/sessionwords")
		text = request.POST['text']

		if 'color' not in request.POST:
			color="black"
		else:
			color = request.POST['color']
		
		

		if 'size' not in request.POST:
			size="normal"		
		else:
			size = request.POST['size']
		
		word = {
			'color':color,
			'text':text,
			'size':size,
			'time':strftime("%Y-%m-%d %H:%M %p", gmtime())
		}
		
		request.session['words'].append(word)
		request.session.modified = True
		return redirect("/sessionwords")

def delete(request):
	request.session.clear()		
	return redirect("/sessionwords")

