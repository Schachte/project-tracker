from django.shortcuts import render, render_to_response, redirect, get_object_or_404, Http404
from django.template import RequestContext

# Create your views here.
def indextest(request):
	context = RequestContext(request)
	return render(request, 'home.html', {})