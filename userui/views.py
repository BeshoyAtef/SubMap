#Imports
from userui.models import *
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext

#End Imports


# Create your views here.

def index(request):
    return render(request, 'index.html')

def submitter(request,block,trial,user):
	user = UserProfile.objects.get(pk=user)
	userblock = Block.objects.get(pk=block)
	trial = Trail.objects.get(pk=trial)
	result=save(request,user,userblock,trail)
	trails = Trail.obejcts.filter(block=block).order_by('order')

	return render(request, 'index.html')

def save(request,user,userblock,trail):
	answer = request.POST['answer']
	result = Result(user=user,userblock=userblock,trial=trial,answer=answer)
	result.save()
	return result

