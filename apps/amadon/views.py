# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
	if 'total' not in request.session:
		request.session['total']=0
	if 'items' not in request.session:
		request.session['items']=0
	if 'cart' not in request.session:
		request.session['cart']={}
	

	return render(request, "amadon/index.html")

def checkout(request):
	if not request.method == "POST":
		return redirect("/")
	key=request.POST['product_id']
	prices = {
		'1':19.99,
		'2':29.99,
		'3':4.99,
		'4':49.99
	}
	if key not in prices:
		return redirect("/")
	if int(request.POST['quantity']) <1:
		return redirect("/")


	request.session['total'] += prices[key] * int(request.POST['quantity'])
	request.session['items'] += int(request.POST['quantity'])
	context = { 'price':prices[key], 'total':request.session['total'], 'items':request.session['items']}
	request.session['cart']=context
	return redirect("/amadon/success")

def success(request):
	print "checkout"
	return render(request, "amadon/success.html", request.session['cart'])

