from django.shortcuts import render, render_to_response, redirect, get_object_or_404, Http404
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
def indextest(request):
	context = RequestContext(request)
	loggedin = False
	# If the request is a HTTP POST, try to pull out the relevant information.
	if request.method == 'POST':

		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)
		if user:
			
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/')
			else:
				return HttpResponseRedirect('/error')
		else:
			loggedin = True
			return render(request,
			'home.html',
			{'loggedin': loggedin} )
	return render_to_response('home.html', {}, context)


